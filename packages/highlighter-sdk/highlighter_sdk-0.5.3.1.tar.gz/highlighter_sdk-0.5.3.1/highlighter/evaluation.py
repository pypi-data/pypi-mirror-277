from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, List, Optional, Union
from uuid import UUID

import yaml
from pydantic import BaseModel, Extra, Field, confloat, validator

from highlighter import HLClient

__all__ = [
    "find_or_create_evaluation_metric",
    "create_evaluation_metric_result",
    "EvaluationMetricCodeEnum",
    "EvaluationMetricResult",
    "EvaluationMetric",
]


class EvaluationMetricCodeEnum(Enum):
    Dice = "Dice"
    mAP = "mAP"
    MaAD = "MaAD"
    MeAD = "MeAD"
    Other = "Other"


class EvaluationMetric(BaseModel):
    id: int
    code: EvaluationMetricCodeEnum
    name: str
    description: Optional[str] = None
    iou: Optional[float] = None
    weighted: Optional[bool] = False
    objectClassUuid: Optional[Union[UUID, str]] = None

    class Config:
        use_enum_values = True

    def dict(self, *args, **kwargs):
        d = super().dict(*args, **kwargs)
        if "objectClassUuid" in d:
            d["objectClassUuid"] = str(d["objectClassUuid"])
        return d


class EvaluationMetricResult(BaseModel, extra=Extra.forbid):
    experimentId: Optional[int]
    researchPlanMetricId: int
    result: float
    objectClassId: Optional[int] = None
    objectClassUuid: Optional[Union[UUID, str]] = None

    # iso datetime str will be generated at instantiation
    # if not supplied manually.
    occuredAt: datetime = Field(default_factory=datetime.now)

    @classmethod
    def from_yaml(cls, path: Union[Path, str]):
        path = Path(path)
        with path.open("r") as f:
            data = yaml.safe_load(f)
        return cls(**data)


def get_existing_evaluation_metrics(client: HLClient, evaluation_id: int):
    class QueryReturnType(BaseModel):
        researchPlanMetrics: List[EvaluationMetric]

    query_return_type: QueryReturnType = client.researchPlan(return_type=QueryReturnType, id=evaluation_id)

    return query_return_type.researchPlanMetrics


def find_or_create_evaluation_metric(
    client: HLClient,
    evaluation_id: int,
    code: Union[EvaluationMetricCodeEnum, str],
    name: str,
    description: Optional[str] = None,
    iou: Optional[float] = None,
    weighted: Optional[bool] = False,
    object_class_uuid: Optional[Union[UUID, str]] = None,
) -> EvaluationMetric:
    existing_evaluation_metrics = {r.name: r for r in get_existing_evaluation_metrics(client, evaluation_id)}

    if name in existing_evaluation_metrics:
        return existing_evaluation_metrics[name]
    else:
        # ToDo: Have the GQL accept s uuid not an id
        if isinstance(object_class_uuid, UUID):
            object_class_uuid = str(object_class_uuid)

        code = EvaluationMetricCodeEnum(code) if isinstance(code, str) else code

        class CreateResearchPlanMetricReturnType(BaseModel):
            errors: Any
            researchPlanMetric: Optional[EvaluationMetric] = None

        kwargs = EvaluationMetric(
            id=-1,
            code=code,
            name=name,
            description=description,
            iou=iou,
            weighted=weighted,
            objectClassUuid=object_class_uuid,
        ).dict(exclude_none=True)
        _ = kwargs.pop("id")
        kwargs["researchPlanId"] = evaluation_id

        result = client.createResearchPlanMetric(
            return_type=CreateResearchPlanMetricReturnType, **kwargs
        ).researchPlanMetric
        assert result is not None
        return result


def create_evaluation_metric_result(
    client: HLClient,
    evaluation_id: int,
    result: float,
    object_class_uuid: Optional[UUID] = None,
    evaluation_metric_id: Optional[int] = None,
    evaluation_metric_name: Optional[str] = None,
    occured_at: Optional[Union[datetime, str]] = None,
    baseline_dataset_id: Optional[int] = None,
    comparison_dataset_id: Optional[int] = None,
    overlap_threshold: Optional[confloat(ge=0, le=1)] = None,  # type: ignore
    entity_attribute_id: Optional[UUID] = None,
    experiment_id: Optional[int] = None,
    training_run_id: Optional[int] = None,
):
    if occured_at is None:
        occured_at = datetime.now()
    elif isinstance(occured_at, str):
        occured_at = datetime.fromisoformat(occured_at)

    if evaluation_metric_id is None:
        assert evaluation_metric_name is not None
        existing_evaluation_metrics = {
            e.name: e for e in get_existing_evaluation_metrics(client, evaluation_id)
        }
        evaluation_metric = existing_evaluation_metrics.get(evaluation_metric_name, None)
        if evaluation_metric is None:
            raise KeyError(
                f"Evaluation Metric '{evaluation_metric_name}' not in evaluation {evaluation_id}. Got: {existing_evaluation_metrics}"
            )
        evaluation_metric_id = evaluation_metric.id

    class CreateEvaluationMetricPayload(BaseModel):
        researchPlanMetricId: int
        experimentId: Optional[int]
        trainingRunId: Optional[int]
        occuredAt: datetime
        result: float
        objectClassUuid: Optional[Union[UUID, str]]
        baselineDatasetId: Optional[int]
        comparisonDatasetId: Optional[int]
        overlapThreshold: Optional[confloat(ge=0, le=1)]  # type: ignore
        entityAttributeId: Optional[Union[UUID, str]]

        @validator("objectClassUuid", "entityAttributeId", allow_reuse=True)
        def validate_uuid(cls, v):
            if v is None:
                return v
            if isinstance(v, UUID):
                return str(v)
            try:
                uuid_obj = UUID(v)
            except ValueError:
                raise ValueError("Invalid UUID")
            return str(uuid_obj)

    kwargs = CreateEvaluationMetricPayload(
        researchPlanMetricId=evaluation_metric_id,
        experimentId=experiment_id,
        trainingRunId=training_run_id,
        occuredAt=occured_at,
        result=result,
        objectClassUuid=object_class_uuid,
        baselineDatasetId=baseline_dataset_id,
        comparisonDatasetId=comparison_dataset_id,
        overlapThreshold=overlap_threshold,
        entityAttributeId=entity_attribute_id,
    ).dict(exclude_none=True)

    kwargs["occuredAt"] = kwargs["occuredAt"].isoformat()

    class CreateExperimentResultReturnType(BaseModel):
        errors: Any
        experimentResult: Optional[EvaluationMetricResult]

    result = client.createExperimentResult(return_type=CreateExperimentResultReturnType, **kwargs)

    if result.errors:
        raise ValueError(f"Errors: {result}")

    return result.experimentResult

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union
from uuid import UUID, uuid4
from warnings import warn

import numpy as np
from numpy.typing import NDArray
from pydantic import (
    BaseModel,
    Extra,
    Field,
    StrictBool,
    StrictFloat,
    StrictInt,
    StrictStr,
    confloat,
    validator,
)
from shapely import affinity
from shapely import geometry as geom
from shapely import make_valid
from shapely.ops import unary_union
from shapely.wkt import loads as wkt_loads

from highlighter.const import (
    DATA_FILE_ATTRIBUTE_UUID,
    EMBEDDING_ATTRIBUTE_UUID,
    OBJECT_CLASS_ATTRIBUTE_UUID,
    PIXEL_LOCATION_ATTRIBUTE_UUID,
    TRACK_ATTRIBUTE_UUID,
)
from highlighter.labeled_uuid import LabeledUUID

UUID_STR = Union[str, UUID]


def try_make_polygon_valid_if_invalid(shape):
    if shape.is_valid:
        return shape

    valid_shape = make_valid(shape)
    if not isinstance(valid_shape, (geom.MultiPolygon, geom.Polygon)):
        raise ValueError(f"Invalid Polygon/MultiPolygon {shape}")
    return valid_shape


def _get_uuid_str():
    return str(uuid4())


def _get_now_str():
    return datetime.now().isoformat()


def _validate_uuid(v):
    if isinstance(v, UUID):
        return str(v)

    if v is None:
        warn("entityId was not provided, generating one")
        return _get_uuid_str()

    try:
        _ = UUID(v)
        return v
    except:  # noqa
        raise ValueError("Invalid UUID string")


class PageInfo(BaseModel):
    hasNextPage: bool
    endCursor: Optional[str]


class ObjectClass(BaseModel):
    id: str
    uuid: str
    name: str


class ObjectClassTypeConnection(BaseModel):
    pageInfo: PageInfo
    nodes: List[ObjectClass]


# Because fileUrlOriginal contains
# a presigned url that is generated upon request
# it is not included by default.
# If you need fileUrlOriginal create a new ImageType
# BaseModel where it is being used.


class ImageType(BaseModel):
    id: str
    width: Optional[int]
    height: Optional[int]
    originalSourceUrl: str
    mimeType: str


class ImagePresignedType(ImageType):
    fileUrlOriginal: str


class ImageTypeConnection(BaseModel):
    pageInfo: PageInfo
    nodes: List[ImageType]


class EntityAttributeType(BaseModel):
    id: str
    name: str


class EntityAttributeEnumType(BaseModel):
    id: str
    value: str


class HLBaseModel(BaseModel, extra=Extra.forbid):
    def gql_dict(self, *args, **kwargs):
        def snake2camel(x: str) -> str:
            lst = x.split("_")
            if len(lst) == 1:
                return x
            return lst[0] + "".join(x.capitalize() for x in lst[1:])

        def _apply2key(d, f):
            result = {}
            for k, v in d.items():
                new_key = f(k)
                result[new_key] = v
                if isinstance(v, dict):
                    result[new_key] = _apply2key(v, f)
            return result

        def to_gql_dict(d):
            return _apply2key(d, snake2camel)

        return to_gql_dict(super().dict(*args, **kwargs))


class DatumSource(HLBaseModel):
    """How did a piece-of-data 'datum' come to be."""

    frame_id: Optional[int]
    host_id: Optional[str]
    pipeline_element_name: Optional[str]
    pipeline_id: Optional[int]
    pipeline_element_id: Optional[int]
    training_run_id: Optional[int]
    confidence: float


class EntityAttributeValueType(BaseModel):
    class GQLDatumSource(HLBaseModel):
        confidence: float

    relatedEntityId: Optional[str]
    fileUuid: Optional[str]
    entityAttribute: EntityAttributeType
    entityAttributeId: str
    entityAttributeEnum: Optional[EntityAttributeEnumType]
    value: Optional[Any]
    entityId: Optional[str] = Field(default_factory=_get_uuid_str)
    entityDatumSource: Optional[GQLDatumSource]
    occurredAt: str

    @validator("entityId", allow_reuse=True)
    def is_valid_uuid(cls, v):
        return _validate_uuid(v)


class UserType(BaseModel):
    id: int
    displayName: Optional[str]
    email: str
    uuid: Optional[Union[UUID, str]]


class AnnotationType(BaseModel):
    # location and confidence are guarantee to exist on AnnotationType
    location: str
    confidence: float = 1.0
    agentName: Optional[str]
    dataType: str
    userId: int
    user: UserType
    correlationId: str
    isInference: bool
    objectClass: ObjectClass
    frameId: Optional[int] = 0
    entityId: Optional[str] = Field(default_factory=_get_uuid_str)

    @validator("entityId", allow_reuse=True)
    def is_valid_uuid(cls, v):
        return _validate_uuid(v)


class SubmissionType(BaseModel):
    id: int
    imageId: int
    annotations: List[AnnotationType]
    entityAttributeValues: List[EntityAttributeValueType]
    createdAt: str
    image: ImageType
    hashSignature: Optional[str]
    user: UserType
    backgroundInfoLayerFileData: Optional[Dict[str, Any]]
    backgroundInfoLayerFileCacheableUrl: Optional[str]


class SubmissionTypeConnection(BaseModel):
    pageInfo: PageInfo
    nodes: List[SubmissionType]


class DatasetSubmissionType(BaseModel):
    submission: SubmissionType


class DatasetSubmissionTypeConnection(BaseModel):
    pageInfo: PageInfo
    nodes: List[DatasetSubmissionType]


class ResearchPlanType(BaseModel):
    id: int
    title: str
    # ToDoOk: Probs need more fields


class ExperimentType(BaseModel):
    id: int
    researchPlan: ResearchPlanType
    title: Optional[str]
    description: Optional[str]
    hypothesis: Optional[str]
    observation: Optional[str]
    conclusion: Optional[str]

    def to_markdown(self, save_path: str):
        def add_markdown_heading(s, heading):
            return f"## {heading}\n{s}\n"

        with open(str(save_path), "w") as f:
            f.write(f"# {self.title}\n")
            f.write(f"- **Experiment ID: {self.id}**\n")
            f.write(f"- **Research Plan ID: {self.researchPlan.id}**\n")
            f.write("\n---\n\n")

            f.write(
                add_markdown_heading(
                    self.description,
                    "Description",
                )
            )

            f.write(
                add_markdown_heading(
                    self.hypothesis,
                    "Hypothesis",
                )
            )

            f.write(
                add_markdown_heading(
                    self.observation,
                    "Observation",
                )
            )

            f.write(
                add_markdown_heading(
                    self.conclusion,
                    "Conclusion",
                )
            )


class PresignedUrlType(BaseModel):
    fields: Dict
    key: str
    storage: str
    url: str


class CompleteFileMultipartUploadPayload(BaseModel):
    errors: List[str]
    url: str


class PipelineInstanceType(BaseModel):
    id: str


class PipelineType(BaseModel):
    id: str


class TaskStatusEnum(str, Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"


class StepType(BaseModel):
    id: str


class AgentType(BaseModel):
    id: str
    machineAgentVersionId: Optional[str]


class TaskType(BaseModel):
    id: str
    accountId: int
    createdAt: str
    description: Optional[str]
    image: Optional[ImageType]
    leasedByAgent: Optional[AgentType]
    leasedByPipelineInstance: Optional[PipelineInstanceType]
    leasedUntil: Optional[str]
    message: Optional[str]
    name: Optional[str]
    parameters: Optional[Any]
    pipeline: Optional[PipelineType]
    pipelineId: Optional[str]
    requestedBy: Optional[UserType]
    status: Optional[TaskStatusEnum]
    step: Optional[StepType]
    stepId: Optional[str]
    submission: Optional[SubmissionType]
    tags: Optional[List[str]]
    updatedAt: str

    class Config:
        use_enum_values = True


class ObjectClassType(BaseModel):
    id: int
    name: str
    color: Optional[str]
    annotationsCount: Optional[int]
    accountId: Optional[int]
    default: bool
    parentId: Optional[int]
    entityAttributeEnum: EntityAttributeEnumType
    uuid: str
    createdAt: str
    updatedAt: str


class ProjectObjectClassType(BaseModel):
    id: int
    objectClass: ObjectClassType
    projectId: int
    createdAt: str
    updatedAt: str
    localised: bool
    entityAttributes: List[EntityAttributeType]
    sortOrder: str


class PluginType(BaseModel):
    id: int
    accountId: int
    name: str
    description: str
    url: str
    default: bool
    module: str
    config: Any
    createdAt: str
    updatedAt: str
    projectId: int


class ProjectTypeType(BaseModel):
    id: int
    name: str
    createdAt: str
    updatedAt: str


class AccountType(BaseModel):
    id: int
    name: str
    subdomain: str
    dataUsage: Optional[int]
    organisationName: Optional[str]
    organisationAcn: Optional[str]
    hlServingMqttHost: Optional[str]
    hlServingMqttPort: Optional[int]
    hlServingMqttUsername: Optional[str]
    hlServingMqttSsl: bool
    users: List[UserType]
    createdAt: str
    updatedAt: str


class ImageQueueType(BaseModel):
    id: int
    createdAt: str
    updatedAt: str
    account: AccountType
    projectId: int
    name: str
    projectStageId: str
    objectClasses: List[ObjectClassType]
    submissions: List[SubmissionType]
    latestSubmissions: List[SubmissionType]
    images: List[ImageType]
    allImages: List[ImageType]
    users: List[UserType]
    matchedImageCount: int
    remainingImageCount: int
    lockedImageCount: int
    availableImageCount: int


class ProjectType(BaseModel):
    id: int
    name: str
    description: Optional[str]
    createdById: int
    accountId: int
    parentId: Optional[int]
    objectClasses: List[ObjectClassType]
    projectObjectClasses: List[ProjectObjectClassType]
    plugins: List[PluginType]
    projectType: Optional[ProjectTypeType]
    createdAt: str
    updatedAt: str
    ownedById: int
    modelId: Optional[int]
    activeCheckpointId: Optional[int]
    batchesCount: int
    metadata: Optional[Any]
    settings: Optional[Any]
    requiredAttributes: Optional[Any]
    multilineAttributes: Optional[Any]
    entityAttributeTaxonGroups: Optional[Any]
    ancestry: Optional[str]
    defaultSearchQuery: Optional[str]
    loadMachineSubmissions: bool
    projectTypeId: Optional[int]
    submissions: List[SubmissionType]
    latestSubmissions: List[SubmissionType]
    imageQueues: List[ImageQueueType]


class ProjectOrderType(BaseModel):
    id: str


class ProjectImageType(BaseModel):
    completedAt: Optional[str]
    createdAt: str
    id: int
    image: ImageType
    latestSubmission: Optional[SubmissionType]
    projectId: int
    projectOrder: Optional[ProjectOrderType]
    state: str
    updatedAt: str


class ExperimentResult(BaseModel):
    baselineDatasetId: Optional[int]
    comparisonDatasetId: Optional[int]
    createdAt: str
    entityAttributeId: Optional[str]
    experimentId: int
    objectClassId: Optional[int]
    occuredAt: str
    overlapThreshold: Optional[float]
    researchPlanMetricId: str
    result: float
    updatedAt: str


# TODO: Validate points in polygon are in the right order
# TODO: Validate points do infact make a rectangle (as needed)
class Polygon(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    _compare_tolerance = 0
    _dtype = np.int64
    _to_coordinates = {
        list: lambda x: np.array(x, dtype=Polygon._dtype),
        np.ndarray: lambda x: x.astype(Polygon._dtype),
    }

    coordinates: Union[NDArray[np.int64], List[Tuple[int, int]]]

    @validator("coordinates", pre=True)
    def cast_coords(cls, v):
        """Cast list or wkt_str to np.array coordinates
        pre=True tell the validator to run before the standard validation
        so it potential the v could be a string is taken care of

        """
        if isinstance(v, list):
            v = np.array(v, dtype=cls._dtype)
            assert (len(v.shape) == 2) and (v.shape[1] == 2)
        elif isinstance(v, str):
            from shapely import wkt

            shapely_poly = wkt.loads(v)
            points = [[int(x), int(y)] for x, y in shapely_poly.exterior.coords][:-1]
            v = np.array(points, dtype=cls._dtype)

        assert isinstance(v, np.ndarray) and (len(v.shape) == 2) and (v.shape[1] == 2)
        return v

    def __eq__(self, other):
        if not isinstance(other, Polygon):
            return False
        return np.allclose(self.coordinates, other.coordinates, rtol=0, atol=self._compare_tolerance)

    # Replaces from_numpy and from_list
    @classmethod
    def from_coordinates(cls, coordinates: Union[List[Tuple[int, int]], np.ndarray]):
        """Create Polygon BaseModel from list or np.array of points

        coordinates in form: [[x0,y0],...,[xn,yn]]

        Do not close the polygon. ie: [x0, y0] != [xn, yn]
        """
        to_coords_fn = cls._to_coordinates[type(coordinates)]
        coordinates = to_coords_fn(coordinates)
        return cls(coordinates=coordinates)

    @classmethod
    def from_wkt(cls, wkt_str):
        """Convert well-known text geometry string into HL polygons"""
        # simple polygons only; no interior boundaries
        shapely_poly = wkt_loads(wkt_str)
        points = [[int(x), int(y)] for x, y in shapely_poly.exterior.coords][:-1]
        return cls.from_coordinates(points)

    def to_list(self, t=int):
        return [[t(x), t(y)] for x, y in self.coordinates]

    # Transform into WKT Geometry: "POLYGON ((x0 y0, x1 y0, x1 y1, x0 y1, x0 y0))"
    def to_wkt(self):
        wkt_str = "POLYGON (("
        for x, y in self.coordinates:
            wkt_str += f"{x} {y},"

        # Close the polygon
        wkt_str += f"{self.coordinates[0][0]} {self.coordinates[0][1]}))"
        return wkt_str

    def scale(self, scale: float):
        self.coordinates = self.coordinates * scale
        return self

    def to_shapely_polygon(self, scale: float = 1.0, pad: int = 0) -> geom.Polygon:
        coords = self.coordinates.tolist()
        coords.append(coords[0])

        poly: geom.Polygon = geom.Polygon(coords)
        if scale != 1.0:
            poly = affinity.scale(poly, xfact=scale, yfact=scale, origin=(0, 0, 0))

        if pad != 0:
            poly = poly.buffer(pad, join_style=2)

        return poly

    def get_top_left_bottom_right_coordinates(
        self, scale: float = 1.0, scale_about_origin: bool = True, pad: int = 0
    ) -> Tuple[int, int, int, int]:
        """
        to top left bottom right format

        for embedding
        """
        if len(self.coordinates) < 2:
            raise ValueError(f"self.coordinates is malformed {self.coordinates}")
        if scale_about_origin:
            xs = self.coordinates[:, 0] * scale
            ys = self.coordinates[:, 1] * scale
        else:
            xs = self.coordinates[:, 0]
            ys = self.coordinates[:, 1]

            xmean = xs.mean()
            ymean = ys.mean()

            xs = ((xs - xmean) * scale) + xmean
            ys = ((ys - ymean) * scale) + ymean

        x0 = np.min(xs) - pad
        y0 = np.min(ys) - pad
        x1 = np.max(xs) + pad
        y1 = np.max(ys) + pad
        return x0, y0, x1, y1

    def is_valid(self) -> bool:
        from shapely import geometry

        return geometry.Polygon(self.coordinates).is_valid

    def area(self) -> float:
        from shapely import geometry

        return geometry.Polygon(self.coordinates).area

    def dict(self):
        return dict(
            coordinates=self.to_wkt(),
        )

    def __str__(self):
        return self.to_wkt()

    @classmethod
    def from_tlbr(cls, x: Tuple[int, int, int, int]) -> "Polygon":
        """
        from top left bottom right format
        """
        top_left = x[0], x[1]
        top_right = x[2], x[1]
        bottom_right = x[2], x[3]
        bottom_left = x[0], x[3]
        return Polygon(coordinates=np.array([top_left, top_right, bottom_right, bottom_left]))


class Point2d(BaseModel):
    x: int
    y: int

    @classmethod
    def from_xy(cls, xy: Tuple[int, int]):
        x, y = xy
        return cls(x=x, y=y)

    def to_wkt(self) -> str:
        return f"POINT({self.x} {self.y})"

    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise KeyError(f"Expected 0|1 got: {key}")


class AttributeValue(BaseModel):
    attribute_id: LabeledUUID
    value: Any
    confidence: confloat(ge=0.0, le=1.0) = 1.0

    def attribute_label(self):
        if isinstance(self.attribute_id, LabeledUUID):
            return self.attribute_id.label
        else:
            return str(self.attribute_id)[:8]

    def serialize_value(self):
        return self.value


class ObjectClassAttributeValue(AttributeValue):
    attribute_id: Union[LabeledUUID, UUID] = Field(default_factory=lambda: OBJECT_CLASS_ATTRIBUTE_UUID)
    value: UUID

    def serialize_value(self):
        return str(self.value)


class PixelLocationAttributeValue(AttributeValue):
    class Config:
        arbitrary_types_allowed = True

    attribute_id: Union[LabeledUUID, UUID] = Field(default_factory=lambda: PIXEL_LOCATION_ATTRIBUTE_UUID)

    value: Union[geom.Polygon, geom.MultiPolygon, geom.LineString, geom.Point]

    def serialize_value(self):
        return self.value.wkt

    @validator("value")
    def validate_geometry(cls, v):
        assert v.is_valid, f"Invalid Geometry: {v}"
        return v

    @classmethod
    def from_wkt(
        cls,
        wkt_str: str,
        attribute_id: Union[LabeledUUID, UUID] = PIXEL_LOCATION_ATTRIBUTE_UUID,
        confidence: float = 1.0,
    ):
        return cls(attribute_id=attribute_id, value=wkt_loads(wkt_str), confidence=confidence)

    @classmethod
    def from_point_coords(
        cls,
        coords: Sequence[Union[Tuple[float, float], Tuple[float, float, float], np.ndarray]],
        attribute_id: Union[LabeledUUID, UUID] = PIXEL_LOCATION_ATTRIBUTE_UUID,
        confidence: float = 1.0,
    ):
        """Create a LocationAttributeValue for a polygon

        Args:
            coords: A sequence or array-like of with 2 or 3 values.
        """
        value = geom.Point(coords)
        return cls(attribute_id=attribute_id, value=value, confidence=confidence)

    @classmethod
    def from_line_coords(
        cls,
        coords: Sequence[
            Union[Tuple[float, float], Tuple[float, float, float], np.ndarray, Sequence[geom.Point]]
        ],
        attribute_id: Union[LabeledUUID, UUID] = PIXEL_LOCATION_ATTRIBUTE_UUID,
        confidence: float = 1.0,
    ):
        """Create a LocationAttributeValue for a polygon

        Args:
            coords: A sequence of (x, y [,z]) numeric coordinate pairs or triples, or
            an array-like with shape (N, 2) or (N, 3).
            Also can be a sequence of Point objects.
        """
        value = geom.LineString(coords)
        return cls(attribute_id=attribute_id, value=value, confidence=confidence)

    @classmethod
    def from_left_top_width_height_coords(
        cls,
        coords: Union[Tuple[float, float, float, float], np.ndarray],
        attribute_id: Union[LabeledUUID, UUID] = PIXEL_LOCATION_ATTRIBUTE_UUID,
        confidence: float = 1.0,
    ):
        """Create a LocationAttributeValue for a box in the form [x,y,w,h]

        Args:
            coords: A sequence of box in the form [x,y,w,h]
        """
        x0, y0, w, h = coords
        x1 = x0 + w
        y1 = y0 + h
        _coords = [[x0, y0], [x1, y0], [x1, y1], [x0, y1], [x0, y0]]
        value = geom.Polygon(_coords)
        return cls(attribute_id=attribute_id, value=value, confidence=confidence)

    @classmethod
    def from_polygon_coords(
        cls,
        coords: Sequence[
            Union[Tuple[float, float], Tuple[float, float, float], np.ndarray, Sequence[geom.Point]]
        ],
        attribute_id: Union[LabeledUUID, UUID] = PIXEL_LOCATION_ATTRIBUTE_UUID,
        confidence: float = 1.0,
        fix_invalid_polygons: bool = False,
    ):
        """Create a LocationAttributeValue for a polygon

        Args:
            coords: A sequence of (x, y [,z]) numeric coordinate pairs or triples, or
            an array-like with shape (N, 2) or (N, 3).
            Also can be a sequence of Point objects.
        """
        if len(coords) < 3:
            raise ValueError(f"Polygon must have at least 3 coordinates: {coords}")

        value = geom.Polygon(coords)
        if fix_invalid_polygons:
            value = try_make_polygon_valid_if_invalid(value)

        return cls(attribute_id=attribute_id, value=value, confidence=confidence)

    @classmethod
    def from_multpolygon_coords(
        cls,
        coords: Sequence[Sequence[Tuple[float, float]]],
        attribute_id: Union[LabeledUUID, UUID] = PIXEL_LOCATION_ATTRIBUTE_UUID,
        confidence: float = 1.0,
        fix_invalid_polygons: bool = False,
    ):
        """Create a LocationAttributeValue for a polygon

        Args:
            coords: A nested sequence of (x, y) numeric coordinate pairs, or
            an array-like with shape (N, 2).
        """
        shapes = []
        for poly_xys in coords:
            shape = geom.Polygon(poly_xys)
            if fix_invalid_polygons:
                shape = try_make_polygon_valid_if_invalid(shape)
            shapes.append(shape)

        if len(shapes) == 1:
            value = shapes[0]
        else:
            value = unary_union(shapes)

        return cls(attribute_id=attribute_id, value=value, confidence=confidence)

    def get_top_left_bottom_right_coordinates(
        self, scale: float = 1.0, scale_about_origin: bool = True, pad: int = 0
    ) -> Tuple[int, int, int, int]:
        """
        to top left bottom right format

        for embedding
        """
        bounds: geom.Polygon = geom.box(*self.value.bounds)

        if scale_about_origin:
            bounds = affinity.scale(bounds, xfact=scale, yfact=scale, origin=(0, 0, 0))
        else:
            bounds = affinity.scale(bounds, xfact=scale, yfact=scale, origin="center")

        bounds = bounds.buffer(pad, join_style="bevel")
        return bounds.bounds


class EmbeddingAttributeValue(AttributeValue):
    class Config:
        arbitrary_types_allowed = True

    attribute_id: Union[LabeledUUID, UUID] = Field(default_factory=lambda: EMBEDDING_ATTRIBUTE_UUID)
    value: Union[Sequence[float], np.ndarray]

    def serialize_value(self):
        return [float(i) for i in self.value]


class DataFileAttributeValue(AttributeValue):
    class Config:
        arbitrary_types_allowed = True

    attribute_id: Union[LabeledUUID, UUID] = Field(default_factory=lambda: DATA_FILE_ATTRIBUTE_UUID)
    value: np.ndarray

    def serialize_value(self):
        raise NotImplementedError()


class EnumAttributeValue(AttributeValue):
    attribute_id: Union[LabeledUUID, UUID]
    value: Union[UUID, LabeledUUID]

    def serialize_value(self):
        raise str(self.value)


class ScalarAttributeValue(AttributeValue):
    attribute_id: Union[LabeledUUID, UUID]
    value: Union[float, int]


class HlEavt(BaseModel):
    entity_id: str
    attribute_id: str
    attribute_name: str
    attribute_enum_id: Optional[str]
    attribute_enum_value: Optional[str]
    value: Any
    time: datetime = datetime.now()
    datum_source: DatumSource

    def to_dict(self):
        d = self.dict()
        d["time"] = d["time"].isoformat()
        return d


class EAVT(HLBaseModel):
    """
    entity_id and attribute_id are global
    value is tied to the attribute, and we have unit for it, so it doesn't appear here
    """

    class Config:
        arbitrary_types_allowed = True

    entity_id: UUID
    attribute_id: Union[LabeledUUID, Dict]
    value: Union[
        UUID,
        LabeledUUID,
        Polygon,
        Point2d,
        List[StrictInt],
        StrictStr,
        StrictBool,
        StrictFloat,
        StrictInt,
        List[StrictStr],
        List[StrictFloat],
        np.ndarray,
        PixelLocationAttributeValue,
    ]
    time: datetime
    datum_source: DatumSource
    unit: Optional[str] = None

    def gql_dict(self):
        value = self.value
        if isinstance(value, (UUID, Polygon)):
            value = str(value)

        return dict(
            entityId=str(self.entity_id),
            attributeId=str(self.attribute_id),
            value=value,
            time=self.time.isoformat(),
            datumSource=self.datum_source.dict(),
        )

    @validator("attribute_id")
    def cast_attribute_id_if_dict(cls, v):
        if isinstance(v, dict):
            return LabeledUUID.from_dict(**v)
        assert isinstance(v, UUID)
        return v

    @validator("value", pre=True)
    def cast_value_if_dict(cls, v):
        if isinstance(v, dict):
            return LabeledUUID.from_dict(**v)
        return v

    def dict(self):
        value = self.value
        if isinstance(value, Polygon):
            value = value.dict()

        if isinstance(value, UUID):
            value = str(value)

        return dict(
            entity_id=str(self.entity_id),
            attribute_id=self.attribute_id,
            value=value,
            time=self.time.isoformat(),
            datum_source=self.datum_source.dict(),
        )

    def to_hleavt(self) -> HlEavt:
        attribute_enum_id = None
        attribute_enum_value = None
        value = self.value
        if isinstance(self.value, Polygon):
            value = self.value.to_wkt()
            attribute_type = "geometry"

        elif isinstance(self.value, bool):
            attribute_type = "bool"

        elif isinstance(self.value, UUID):
            attribute_type = "enum"
            attribute_enum_id = str(self.value)
            attribute_enum_value = getattr(self.value, "label", "")
            value = None

        elif isinstance(self.value, List):  # embeddings
            attribute_type = "array"

        return HlEavt(
            entity_id=str(self.entity_id),
            attribute_id=str(self.attribute_id),
            attribute_name=str(self.attribute_id.label),
            attribute_type=attribute_type,  # for now
            attribute_enum_id=attribute_enum_id,
            attribute_enum_value=attribute_enum_value,
            value=value,
            time=self.time,
            datum_source=self.datum_source,
        )

    def is_pixel_location(self):
        return str(self.attribute_id) == PIXEL_LOCATION_ATTRIBUTE_UUID

    def is_object_class(self):
        return str(self.attribute_id) == OBJECT_CLASS_ATTRIBUTE_UUID

    def is_track(self):
        return str(self.attribute_id) == TRACK_ATTRIBUTE_UUID

    def is_embedding(self):
        return str(self.attribute_id) == EMBEDDING_ATTRIBUTE_UUID

    def get_confidence(self):
        return self.datum_source.confidence

    @classmethod
    def make_scalar_eavt(
        cls,
        entity_id: UUID,
        value: Union[int, float],
        attribute_id: LabeledUUID,
        time: datetime,
        pipeline_element_name: Optional[str] = None,
        training_run_id: Optional[int] = None,
        host_id: Optional[int] = None,
        frame_id: Optional[int] = None,
        unit: Optional[str] = None,
    ):
        datum_source = DatumSource(
            confidence=1.0,
            pipeline_element_name=pipeline_element_name,
            training_run_id=training_run_id,
            host_id=host_id,
            frame_id=frame_id,
        )
        return cls(
            entity_id=entity_id,
            attribute_id=attribute_id,
            value=value,
            datum_source=datum_source,
            time=time,
            unit=unit,
        )

    @classmethod
    def make_image_eavt(
        cls,
        entity_id: UUID,
        image: np.ndarray,
        time: datetime,
        pipeline_element_name: Optional[str] = None,
        training_run_id: Optional[int] = None,
        host_id: Optional[int] = None,
        frame_id: Optional[int] = None,
    ):
        datum_source = DatumSource(
            confidence=1.0,
            pipeline_element_name=pipeline_element_name,
            training_run_id=training_run_id,
            host_id=host_id,
            frame_id=frame_id,
        )
        return cls(
            entity_id=entity_id,
            attribute_id=DATA_FILE_ATTRIBUTE_UUID,
            value=image,
            datum_source=datum_source,
            time=time,
        )

    @classmethod
    def make_embedding_eavt(
        cls,
        entity_id: UUID,
        embedding: List[float],
        time: datetime,
        pipeline_element_name: Optional[str] = None,
        training_run_id: Optional[int] = None,
        host_id: Optional[int] = None,
        frame_id: Optional[int] = None,
    ):
        if not isinstance(embedding, list):
            t = type(embedding)
            raise ValueError(f"embedding must be list of float not {t}")

        datum_source = DatumSource(
            confidence=1.0,
            pipeline_element_name=pipeline_element_name,
            training_run_id=training_run_id,
            host_id=host_id,
            frame_id=frame_id,
        )
        return cls(
            entity_id=entity_id,
            attribute_id=EMBEDDING_ATTRIBUTE_UUID,
            value=embedding,
            datum_source=datum_source,
            time=time,
        )

    @classmethod
    def make_pixel_location_eavt(
        cls,
        location_points: Union[
            Polygon, List[Tuple[int, int]], Point2d, Tuple[int, int], geom.Polygon, geom.MultiPolygon, str
        ],
        confidence: float,
        time: datetime,
        pipeline_element_name: Optional[str] = None,
        training_run_id: Optional[int] = None,
        host_id: Optional[int] = None,
        frame_id: Optional[int] = None,
        entity_id: Optional[Union[str, UUID]] = None,
    ):
        """Create a new entity_id and assign a pixel_location
        attribute to the EAVT.

        The make_pixel_location_eavt is the only make_*
        method that will create a new entity_id.
        """
        if entity_id is None:
            entity_id = uuid4()

        if isinstance(location_points, Polygon):
            value = PixelLocationAttributeValue.from_wkt(location_points.to_wkt())
        elif isinstance(location_points, (geom.Polygon, geom.MultiPolygon)):
            value = PixelLocationAttributeValue(value=location_points)
        elif isinstance(location_points, list):
            value = PixelLocationAttributeValue.from_polygon_coords(location_points)

        elif isinstance(location_points, Point2d):
            value = PixelLocationAttributeValue.from_wkt(location_points.to_wkt())
        elif isinstance(location_points, tuple):
            value = PixelLocationAttributeValue.from_point_coords(location_points)
        elif isinstance(location_points, str):
            value = PixelLocationAttributeValue.from_wkt(location_points)
        else:
            raise ValueError(f"Invalid location_points: {location_points}")

        datum_source = DatumSource(
            confidence=confidence,
            pipeline_element_name=pipeline_element_name,
            training_run_id=training_run_id,
            host_id=host_id,
            frame_id=frame_id,
        )

        return cls(
            entity_id=entity_id,
            attribute_id=PIXEL_LOCATION_ATTRIBUTE_UUID,
            value=value,
            datum_source=datum_source,
            time=time,
        )

    @classmethod
    def make_enum_eavt(
        cls,
        entity_id: UUID,
        attribute_uuid: UUID,
        attribute_label: str,
        enum_value: str,
        enum_id: UUID,
        confidence: float,
        time: datetime,
        pipeline_element_name: Optional[str] = None,
        training_run_id: Optional[int] = None,
        host_id: Optional[int] = None,
        frame_id: Optional[int] = None,
    ):
        """Make an EAVT with an enum attribute for the given entity_id"""
        datum_source = DatumSource(
            confidence=confidence,
            pipeline_element_name=pipeline_element_name,
            training_run_id=training_run_id,
            host_id=host_id,
            frame_id=frame_id,
        )

        return cls(
            entity_id=entity_id,
            attribute_id=LabeledUUID(
                attribute_uuid,
                label=attribute_label,
            ),
            value=LabeledUUID(
                enum_id,
                label=enum_value,
            ),
            datum_source=datum_source,
            time=time,
        )

    @classmethod
    def make_object_class_eavt(
        cls,
        entity_id: UUID,
        object_class_uuid: UUID,
        object_class_value: str,
        confidence: float,
        time: datetime,
        pipeline_element_name: Optional[str] = None,
        training_run_id: Optional[int] = None,
        host_id: Optional[int] = None,
        frame_id: Optional[int] = None,
    ):
        """Convienence method to make an EAVT with an object_class attribute
        for the given entity_id
        """
        datum_source = DatumSource(
            confidence=confidence,
            pipeline_element_name=pipeline_element_name,
            training_run_id=training_run_id,
            host_id=host_id,
            frame_id=frame_id,
        )

        return cls(
            entity_id=entity_id,
            attribute_id=OBJECT_CLASS_ATTRIBUTE_UUID,
            value=LabeledUUID(
                object_class_uuid,
                label=object_class_value,
            ),
            datum_source=datum_source,
            time=time,
        )

    @classmethod
    def make_boolean_eavt(
        cls,
        entity_id: UUID,
        attribute_uuid: UUID,
        attribute_label: str,
        value: bool,
        confidence: float,
        time: datetime,
        pipeline_element_name: Optional[str] = None,
        training_run_id: Optional[int] = None,
        host_id: Optional[int] = None,
        frame_id: Optional[int] = None,
    ):
        """Convienence method to make an EAVT with an object_class attribute
        for the given entity_id
        """
        if not isinstance(value, bool):
            raise ValueError(
                "make_boolean_eavt expects value arg to be of type bool "
                f"got: {value} of type: {type(value)}"
            )

        datum_source = DatumSource(
            confidence=confidence,
            pipeline_element_name=pipeline_element_name,
            training_run_id=training_run_id,
            host_id=host_id,
            frame_id=frame_id,
        )

        return cls(
            entity_id=entity_id,
            attribute_id=LabeledUUID(
                attribute_uuid,
                label=attribute_label,
            ),
            value=value,
            datum_source=datum_source,
            time=time,
        )

    @classmethod
    def make_detection_eavt_pair(
        cls,
        location_points: Union[
            Polygon, List[Tuple[int, int]], Point2d, Tuple[int, int], geom.Polygon, geom.MultiPolygon, str
        ],
        object_class_value: str,
        object_class_uuid: UUID,
        confidence: float,
        time: datetime,
        pipeline_element_name: Optional[str] = None,
        training_run_id: Optional[int] = None,
        host_id: Optional[int] = None,
        frame_id: Optional[int] = None,
    ):
        """Convienence method to make both a pixel_location and
        object_class attribute, returning them both in a list
        """
        pixel_location_eavt = EAVT.make_pixel_location_eavt(
            location_points,
            confidence,
            pipeline_element_name=pipeline_element_name,
            training_run_id=training_run_id,
            host_id=host_id,
            frame_id=frame_id,
            time=time,
        )

        entity_id = pixel_location_eavt.entity_id

        object_class_eavt = EAVT.make_object_class_eavt(
            entity_id,
            object_class_uuid,
            object_class_value,
            confidence,
            pipeline_element_name=pipeline_element_name,
            training_run_id=training_run_id,
            host_id=host_id,
            frame_id=frame_id,
            time=time,
        )
        return [pixel_location_eavt, object_class_eavt]

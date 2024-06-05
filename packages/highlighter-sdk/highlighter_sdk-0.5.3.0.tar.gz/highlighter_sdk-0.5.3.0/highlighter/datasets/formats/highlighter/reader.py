import mimetypes
from pathlib import Path
from typing import List, Tuple
from warnings import warn

from highlighter.base_models import PixelLocationAttributeValue
from highlighter.const import OBJECT_CLASS_ATTRIBUTE_UUID, PIXEL_LOCATION_ATTRIBUTE_UUID
from highlighter.datasets.base_models import AttributeRecord, ImageRecord
from highlighter.datasets.interfaces import IReader

__all__ = [
    "HighlighterAssessmentsReader",
]


class HighlighterAssessmentsReader(IReader):
    format_name = "highlighter_assessments"

    def __init__(self, assessments_gen):
        self.assessments_gen = assessments_gen

    def read(self) -> Tuple[List[AttributeRecord], List[ImageRecord]]:
        attribute_records = []
        data_file_records = []
        for i, assessment in enumerate(self.assessments_gen):
            data_file = assessment.image
            assessment_id = assessment.id
            hash_signature = assessment.hashSignature
            data_file_id = data_file.id
            filename_original = Path(data_file.originalSourceUrl)

            ext = filename_original.suffix
            if ext == "":
                ext = mimetypes.guess_extension(data_file.mimeType).lower()

            filename = f"{data_file_id}{ext}"
            data_file_records.append(
                ImageRecord(
                    data_file_id=data_file_id,
                    width=data_file.width,
                    height=data_file.height,
                    filename=filename,
                    extra_fields={"filename_original": str(filename_original)},
                    assessment_id=assessment_id,
                    hash_signature=hash_signature,
                )
            )

            for eavt in assessment.entityAttributeValues:
                value = eavt.value
                if value is None:
                    value = eavt.entityAttributeEnum.id

                datum_source = eavt.entityDatumSource
                if datum_source is None:
                    conf = 1.0
                else:
                    conf = datum_source.confidence

                attribute_records.append(
                    AttributeRecord(
                        data_file_id=data_file_id,
                        entity_id=eavt.entityId,
                        attribute_id=eavt.entityAttribute.id,
                        attribute_name=eavt.entityAttribute.name,
                        value=value,
                        confidence=conf,
                    )
                )

            for annotation in assessment.annotations:
                if annotation.location is None:
                    warn("Null value found in location. Get it together bro.")
                    continue

                confidence = getattr(annotation, "confidence", None)
                object_class = annotation.objectClass
                attribute_records.append(
                    AttributeRecord(
                        data_file_id=data_file_id,
                        entity_id=annotation.entityId,
                        attribute_id=str(OBJECT_CLASS_ATTRIBUTE_UUID),
                        attribute_name=OBJECT_CLASS_ATTRIBUTE_UUID.label,
                        value=object_class.uuid,
                        frame_id=annotation.frameId,
                        confidence=confidence,
                    )
                )

                pixel_location_attribute_value = PixelLocationAttributeValue.from_wkt(
                    annotation.location, confidence=confidence
                )
                attribute_records.append(
                    AttributeRecord.from_attribute_value(
                        data_file_id,
                        pixel_location_attribute_value,
                        entity_id=annotation.entityId,
                        frame_id=annotation.frameId,
                    )
                )

        return data_file_records, attribute_records

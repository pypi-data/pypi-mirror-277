from dataclasses import dataclass, field
from typing import Any, Self

from dbnomics_data_model.model.identifiers.attribute_code import AttributeCode
from dbnomics_data_model.model.identifiers.types import AttributeValueCode
from dbnomics_data_model.model.periods import Period

from .types import ObservationValue

__all__ = ["Observation"]


@dataclass(frozen=True, kw_only=True)
class Observation:
    period: Period
    value: ObservationValue

    attributes: dict[AttributeCode, AttributeValueCode] = field(default_factory=dict)

    @classmethod
    def create(
        cls,
        *,
        attributes: dict[str, str] | None = None,
        period: Period | str,
        value: ObservationValue,
    ) -> Self:
        if attributes is None:
            attributes = {}
        parsed_attributes = {
            AttributeCode.parse(code): AttributeValueCode.parse(value_code) for code, value_code in attributes.items()
        }

        if isinstance(period, str):
            period = Period.parse(period)

        return cls(attributes=parsed_attributes, period=period, value=value)

    @property
    def __match_key__(self) -> Any:
        return self.period

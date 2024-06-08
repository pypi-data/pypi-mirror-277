from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .ingredient import Ingredient
from .measurement import Measurement


class IncompatibleComponentError(ValueError):
    pass


@dataclass(frozen=True, slots=True)
class Component:
    """
    Collection of details surrounding an ingredient.
    Ex: 10 cloves peeled garlic
    """

    extra_comment: str
    id: int
    ingredient: Ingredient
    measurements: list[Measurement]
    position: int
    raw_text: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Component:
        return Component(
            extra_comment=data["extra_comment"],
            id=data["id"],
            ingredient=Ingredient.from_dict(data["ingredient"]),
            measurements=[
                Measurement.from_dict(measurement)
                for measurement in data["measurements"]
            ],
            position=data["position"],
            raw_text=data["raw_text"],
        )

    def __add__(self, other: Component) -> Component:
        if self.ingredient.id != other.ingredient.id:
            raise IncompatibleComponentError(
                "Components must be the same in order to add their amounts."
            )

        ret = Component(
            extra_comment="",
            id=self.id,
            ingredient=self.ingredient,
            measurements=[],
            position=0,
            raw_text="",
        )

        for measurement in self.measurements:
            other_measurement_quantity = 0
            for other_measurement in other.measurements:
                if measurement.unit.name != other_measurement.unit.name:
                    continue
                other_measurement_quantity = other_measurement.quantity
                break

            ret.measurements.append(
                Measurement(
                    id=measurement.id,
                    quantity=measurement.quantity + other_measurement_quantity,
                    unit=measurement.unit,
                )
            )

        return ret

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from unicodedata import numeric


def parse_number(number: str) -> float:
    if number.isascii() and number.isnumeric():
        return float(number)
    elif len(number) > 1:
        # stole this code from stackoverflow: https://stackoverflow.com/a/50264056
        return float(number[:-1]) + numeric(number[-1])
    return numeric(number)


@dataclass(frozen=True, slots=True)
class Unit:
    """Represents the unit of a `Measurement`."""

    abbreviation: str
    display_plural: str
    display_singular: str
    name: str
    system: str | None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Unit:
        return Unit(
            abbreviation=data["abbreviation"],
            display_plural=data["display_plural"],
            display_singular=data["display_singular"],
            name=data["name"],
            system=data.get("system"),
        )


@dataclass(frozen=True, slots=True)
class Measurement:
    """Represents the amount of a `Component`."""

    id: int
    quantity: float
    unit: Unit

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Measurement:
        return Measurement(
            id=data["id"],
            quantity=parse_number(data["quantity"]),
            unit=Unit.from_dict(data["unit"]),
        )

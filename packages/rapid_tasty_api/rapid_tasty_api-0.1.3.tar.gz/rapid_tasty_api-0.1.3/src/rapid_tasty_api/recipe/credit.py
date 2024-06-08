from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class Credit:
    """Represents a credit (eg. author) of the recipe."""

    name: str | None
    type: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Credit:
        return Credit(
            name=data["name"],
            type=data["type"],
        )

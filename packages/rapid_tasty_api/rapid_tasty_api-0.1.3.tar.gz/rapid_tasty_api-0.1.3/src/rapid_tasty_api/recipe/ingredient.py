from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass(frozen=True, slots=True)
class Ingredient:
    """Represents an ingredient."""

    created_at: datetime
    display_plural: str
    display_singular: str
    id: int
    name: str
    updated_at: datetime

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Ingredient:
        return Ingredient(
            created_at=datetime.fromtimestamp(data["created_at"]),
            display_plural=data["display_plural"],
            display_singular=data["display_singular"],
            id=data["id"],
            name=data["name"],
            updated_at=datetime.fromtimestamp(data["updated_at"]),
        )

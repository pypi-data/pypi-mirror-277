from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass(frozen=True, slots=True)
class Nutrition:
    """Represents the nutrition facts of a recipe. All values are in grams."""

    calories: int | None
    carbohydrates: int | None
    fat: int | None
    fiber: int | None
    protein: int | None
    sugar: int | None
    updated_at: datetime | None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Nutrition:
        return Nutrition(
            calories=data.get("calories"),
            carbohydrates=data.get("carbohydrates"),
            fat=data.get("fat"),
            fiber=data.get("fiber"),
            protein=data.get("protein"),
            sugar=data.get("sugar"),
            updated_at=datetime.fromisoformat(data["updated_at"])
            if data.get("updated_at") is not None
            else None,
        )

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from rapid_tasty_api.recipe import Recipe


@dataclass(frozen=True, slots=True)
class Feed:
    """Represents one of Tasty's feeds (e.g. Popular Recipes This Week)"""

    type: str
    items: list[Recipe]
    name: str | None = None
    category: str | None = None
    min_items: int | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Feed:
        if data["type"] in ("item", "featured"):
            return Feed(
                type=data["type"],
                items=[Recipe.from_dict(data["item"])],
            )

        # Uses .get() because sometimes the values don't exist.

        return Feed(
            type=data["type"],
            items=[Recipe.from_dict(item) for item in data["items"]],
            name=data.get("name"),
            category=data.get("category"),
            min_items=data.get("min_items"),
        )

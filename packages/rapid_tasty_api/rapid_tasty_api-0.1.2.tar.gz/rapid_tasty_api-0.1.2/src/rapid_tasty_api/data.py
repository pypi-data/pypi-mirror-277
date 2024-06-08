from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from rapid_tasty_api.recipe import Completion, Recipe
from rapid_tasty_api.tag import Tag
from rapid_tasty_api.tip import Tip


@dataclass(frozen=True, slots=True)
class CompletionData:
    """Custom class to destructure auto complete requests."""

    results: list[Completion]

    @classmethod
    def from_dict(cls, data: dict[str, list[dict[str, str]]]) -> CompletionData:
        return CompletionData(
            [Completion.from_dict(result) for result in data["results"]]
        )


@dataclass(frozen=True, slots=True)
class RecipeListData:
    """Custom class to destructure recipes/list requests."""

    count: int
    results: list[Recipe]

    # TODO (maybe): Replace the Any with the full type of the dictionary. Big maybe.
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> RecipeListData:
        return RecipeListData(
            data["count"], [Recipe.from_dict(result) for result in data["results"]]
        )


@dataclass(frozen=True, slots=True)
class TagListData:
    """Custom class to destructure recipes/list requests."""

    count: int
    results: list[Tag]

    # Can someone figure out how to use these? The endpoints don't seem to exist.
    prev: str | None
    next: str | None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TagListData:
        return TagListData(
            data["count"],
            [Tag.from_dict(result) for result in data["results"]],
            data["prev"],
            data["next"],
        )


@dataclass(frozen=True, slots=True)
class TipListData:
    """Custom class to destructure recipes/list requests."""

    count: int
    results: list[Tip]

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TipListData:
        return TipListData(
            data["count"], [Tip.from_dict(result) for result in data["results"]]
        )

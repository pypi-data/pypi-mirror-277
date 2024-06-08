from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass(frozen=True, slots=True)
class TipMetadata:
    """Represents the metadata of a Tip object."""

    author_avatar_url: str
    author_rating: int
    author_user_id: int
    author_is_verified: int
    is_flagged: bool
    recipe_id: int
    status_id: int
    comment_id: int
    comment_count: int
    tip_id: int
    created_at: datetime | None
    updated_at: datetime

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TipMetadata:
        return TipMetadata(
            author_avatar_url=data["author_avatar_url"],
            author_rating=data["author_rating"],
            author_user_id=data["author_user_id"],
            author_is_verified=data["author_is_verified"],
            is_flagged=data["is_flagged"],
            recipe_id=data["recipe_id"],
            status_id=data["status_id"],
            comment_id=data["comment_id"],
            comment_count=data["comment_count"],
            tip_id=data["tip_id"],
            created_at=(
                datetime.fromtimestamp(data["created_at"])
                if data["created_at"] is not None
                else None
            ),
            updated_at=datetime.fromtimestamp(data["updated_at"]),
        )


@dataclass(frozen=True, slots=True)
class Tip:
    """Represents a tip (review) for a specific recipe."""

    metadata: TipMetadata
    author_name: str
    author_username: str
    tip_body: str
    upvotes_total: int

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Tip:
        author_name: str = data.pop("author_name")
        author_username: str = data.pop("author_username")
        tip_body: str = data.pop("tip_body")
        upvotes_total: int = data.pop("upvotes_total")
        metadata: TipMetadata = TipMetadata.from_dict(data)

        return Tip(metadata, author_name, author_username, tip_body, upvotes_total)

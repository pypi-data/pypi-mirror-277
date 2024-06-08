from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any

import iso639
import pycountry
import pycountry.db

from rapid_tasty_api.tag import Tag

from .credit import Credit
from .instruction import Instruction
from .nutrition import Nutrition
from .price import Price
from .ratings import Ratings
from .section import Section
from .topic import Topic


@dataclass(frozen=True, slots=True)
class RecipeMetadata:
    """Represents the metadata of a recipe."""

    approved_at: datetime
    aspect_ratio: str
    beauty_url: str | None
    brand: str | None
    brand_id: int | None
    buzz_id: int | None
    canonical_id: str
    # TODO (when I find an example): compilations: list[SOMETHING]
    country: pycountry.db.Country
    created_at: datetime
    credits: list[Credit]
    draft_status: str
    # TODO (when I find an example): facebook_posts: list[SOMETHING]
    id: int
    inspired_by_url: str | None
    is_app_only: bool
    is_one_top: bool
    is_shoppable: bool
    is_subscriber_content: bool
    keywords: str
    language: iso639.Language
    nutrition_visibility: str
    original_video_url: str | None
    promotion: str
    # TODO (when I find an example): renditions: list[SOMETHING]
    seo_path: str
    seo_title: str
    servings_noun_plural: str
    servings_noun_singular: str
    show_name: str
    show_id: int
    slug: str
    thumbnail_alt_text: str
    thumbnail_url: str
    tips_and_ratings_enabled: bool
    # TODO (when I find an example): total_time_tier: SOMETHING | None
    updated_at: datetime
    # TODO (when I find an example): video_ad_content: SOMETHING | None
    video_id: int | None
    video_url: str | None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> RecipeMetadata:
        return RecipeMetadata(
            approved_at=datetime.fromtimestamp(data["approved_at"]),
            aspect_ratio=data["aspect_ratio"],
            beauty_url=data["beauty_url"],
            brand=data["brand"],
            brand_id=data["brand_id"],
            buzz_id=data["buzz_id"],
            canonical_id=data["canonical_id"],
            country=pycountry.countries.get(alpha_2=data["country"]),  # type: ignore
            created_at=datetime.fromtimestamp(data["created_at"]),
            credits=[Credit.from_dict(credit) for credit in data["credits"]],
            draft_status=data["draft_status"],
            id=data["id"],
            inspired_by_url=data["inspired_by_url"],
            is_app_only=data["is_app_only"],
            is_one_top=data["is_one_top"],
            is_shoppable=data["is_shoppable"],
            is_subscriber_content=data["is_subscriber_content"],
            keywords=data["keywords"],
            language=iso639.Language.from_part3(data["language"]),
            nutrition_visibility=data["nutrition_visibility"],
            original_video_url=data["original_video_url"],
            promotion=data["promotion"],
            seo_path=data["seo_path"],
            seo_title=data["seo_title"],
            servings_noun_plural=data["servings_noun_plural"],
            servings_noun_singular=data["servings_noun_singular"],
            show_name=data["show"]["name"],
            show_id=data["show_id"],
            slug=data["slug"],
            thumbnail_alt_text=data["thumbnail_alt_text"],
            thumbnail_url=data["thumbnail_url"],
            tips_and_ratings_enabled=data["tips_and_ratings_enabled"],
            updated_at=datetime.fromtimestamp(data["updated_at"]),
            video_id=data["video_id"],
            video_url=data["video_url"],
        )


@dataclass(frozen=True, slots=True)
class Recipe:
    """Represents a recipe."""

    metadata: RecipeMetadata
    cook_time_minutes: int | None
    description: str
    instructions: list[Instruction]
    name: str
    num_servings: int
    nutrition: Nutrition
    prep_time_minutes: int | None
    price: Price
    sections: list[Section]
    tags: list[Tag]
    topics: list[Topic]
    total_time_minutes: int | None
    user_ratings: Ratings
    yields: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Recipe:
        cook_time_minutes: int | None = data.pop("cook_time_minutes")
        desciption: str = data.pop("description")
        instructions: list[Instruction] = [
            Instruction.from_dict(instruction)
            for instruction in data.pop("instructions")
        ]
        name: str = data.pop("name")
        num_servings: int = data.pop("num_servings")
        nutrition: Nutrition = Nutrition.from_dict(data.pop("nutrition"))
        prep_time_minutes: int | None = data.pop("prep_time_minutes")
        price: Price = Price.from_dict(data.pop("price"))
        sections: list[Section] = [
            Section.from_dict(section) for section in data.pop("sections")
        ]
        tags: list[Tag] = [Tag.from_dict(tag) for tag in data.pop("tags")]
        topics: list[Topic] = [Topic.from_dict(topic) for topic in data.pop("topics")]
        total_time_minutes: int | None = data.pop("total_time_minutes")
        user_ratings: Ratings = Ratings.from_dict(data.pop("user_ratings"))
        yields: str = data.pop("yields")
        metadata: RecipeMetadata = RecipeMetadata.from_dict(data)

        return Recipe(
            metadata,
            cook_time_minutes,
            desciption,
            instructions,
            name,
            num_servings,
            nutrition,
            prep_time_minutes,
            price,
            sections,
            tags,
            topics,
            total_time_minutes,
            user_ratings,
            yields,
        )

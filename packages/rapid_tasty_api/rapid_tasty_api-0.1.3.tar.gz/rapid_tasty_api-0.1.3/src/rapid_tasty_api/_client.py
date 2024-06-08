from datetime import UTC, time, tzinfo
from enum import StrEnum

import requests

from rapid_tasty_api._constants import TASTY_HOST
from rapid_tasty_api.data import (
    CompletionData,
    RecipeListData,
    TagListData,
    TipListData,
)
from rapid_tasty_api.feed import Feed
from rapid_tasty_api.recipe import Completion, Recipe
from rapid_tasty_api.tag import Tag, tag_list_to_str
from rapid_tasty_api.tip import Tip


class SortingMethod(StrEnum):
    POPULAR = "popular"
    DESCENDING = "approved_at:desc"
    ASCENDING = "approved_at:asc"


def _timezone_to_utc_offset(timezone_: tzinfo) -> str:
    return time(tzinfo=timezone_).strftime("%z")


class Client:
    """A client to send requests to the Tasty API."""

    __slots__ = "_session"

    def __init__(self, rapid_api_key: str) -> None:
        """
        A client to send requests to the Tasty API.

        :param str rapid_api_key: Your API key. Get one from https://rapidapi.com/apidojo/api/tasty.
        """

        self._session = requests.Session()
        self._session.headers.update(
            {
                "X-RapidAPI-Key": rapid_api_key,
                "X-RapidAPI-Host": TASTY_HOST,
            }
        )

    def get_recipes_auto_complete(self, prefix: str) -> list[Completion]:
        """
        Get auto complete suggestions by name or ingredients.

        :param str prefix: The text to be auto completed.
        :return list[Completion]: A list of possible auto completions.
        """

        url = "https://tasty.p.rapidapi.com/recipes/auto-complete"

        querystring = {"prefix": prefix}

        response = self._session.get(url, params=querystring)

        data = CompletionData.from_dict(response.json())

        return data.results

    def get_recipes_list(
        self,
        offset: int,
        size: int,
        tags: list[Tag] | None = None,
        query: str | None = None,
        sort: SortingMethod = SortingMethod.POPULAR,
    ) -> list[Recipe]:
        """
        Get a list of recipes.

        :param int offset: The amount of recipes to skip.
        :param int size: The amount of recipes to get.
        :param list[Tag] | None tags: A list of tags you want to search for, defaults to None
        :param str | None query: Name of food or ingredients to search by, defaults to None
        :param SortingMethod sort: The method of sorting the results, defaults to SortingMethod.POPULAR
        :return list[Recipe]: The list of recipes.
        """

        url = "https://tasty.p.rapidapi.com/recipes/list"

        querystring = {"from": str(offset), "size": str(size)}

        if tags is not None:
            querystring.update({"tags": tag_list_to_str(tags)})

        if query is not None:
            querystring.update({"q": query})

        if sort != SortingMethod.POPULAR:
            querystring.update({"sort": sort})

        response = self._session.get(url, params=querystring)

        data = RecipeListData.from_dict(response.json())

        return data.results

    def get_recipes_list_similarities(self, recipe_id: int) -> list[Recipe]:
        """
        Get a list of recipes similar to a given recipe.

        :param int recipe_id: The recipe to get similar recipes to.
        :return list[Recipe]: The list of similar recipes.
        """

        url = "https://tasty.p.rapidapi.com/recipes/list-similarities"

        querystring = {"recipe_id": str(recipe_id)}

        response = self._session.get(url, params=querystring)

        data = RecipeListData.from_dict(response.json())

        return data.results

    def get_recipes_more_info(self, recipe_id: int) -> Recipe:
        """
        Get a specific recipe.

        :param int recipe_id: The recipe to get information on.
        :return Recipe: The recipe.
        """

        url = "https://tasty.p.rapidapi.com/recipes/get-more-info"

        querystring = {"recipe_id": recipe_id}

        response = self._session.get(url, params=querystring)

        recipe = Recipe.from_dict(response.json())

        return recipe

    def get_feeds_list(
        self,
        vegetarian: bool,
        timezone: tzinfo = UTC,
        offset: int = 0,
        size: int = 5,
    ) -> list[Feed]:
        """
        Get a list of the latests feeds.

        Feeds are lists of specifically categorized recipes.

        :param int offset: The amount of feeds to skip.
        :param int size: The amount of feeds to get.
        :param bool vegetarian: List vegetarian recipes only.
        :param tzinfo timezone: Your timezone. Defaults to UTC.
        :return list[Feed]: The list of feeds.
        """

        url = "https://tasty.p.rapidapi.com/feeds/list"

        querystring = {
            "size": str(size),
            "timezone": _timezone_to_utc_offset(timezone),
            "vegetarian": "true" if vegetarian else "false",
            "from": str(offset),
        }

        response = self._session.get(url, params=querystring)

        data = [Feed.from_dict(result) for result in response.json()["results"]]

        return data

    def get_tags_list(self) -> list[Tag]:
        """
        Get a list of all tags.

        :return list[Tag]: The list of tags.
        """

        url = "https://tasty.p.rapidapi.com/tags/list"

        response = self._session.get(url)

        data = TagListData.from_dict(response.json())

        return data.results

    def get_tips_list(
        self, recipe_id: int, offset: int = 0, size: int = 30
    ) -> list[Tip]:
        """
        Get a list of tips (reviews) pertaining to a recipe.

        :param int recipe_id: The recipe ID.
        :param int offset: The amount of tips to skip.
        :param int size: The amount of tips to get.

        :return list[Tip]: The list of tips.
        """

        url = "https://tasty.p.rapidapi.com/tips/list"

        querystring = {
            "id": str(recipe_id),
            "from": str(offset),
            "size": str(size),
        }

        response = self._session.get(url, params=querystring)

        data = TipListData.from_dict(response.json())

        return data.results

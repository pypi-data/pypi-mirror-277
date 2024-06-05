from datetime import date, datetime, time, timezone
from typing import Annotated

from bson import ObjectId
from pydantic import BaseModel, ConfigDict
from pydantic.functional_serializers import PlainSerializer


def camel_case(string: str) -> str:
    assert isinstance(string, str), "Input must be of type str"

    first_alphabetic_character_index = -1
    for index, character in enumerate(string):
        if character.isalpha():
            first_alphabetic_character_index = index
            break

    empty = ""

    if first_alphabetic_character_index == -1:
        return empty

    string = string[first_alphabetic_character_index:]

    titled_string_generator = (character for character in string.title() if character.isalnum())

    try:
        return next(titled_string_generator).lower() + empty.join(titled_string_generator)

    except StopIteration:
        return empty


def to_camel(string):
    if string == "id":
        return "_id"
    if string.startswith("_"):  # "_id"
        return string
    return camel_case(string)


DatetimeType = Annotated[
    datetime,
    PlainSerializer(
        lambda dt: dt.replace(microsecond=0, tzinfo=timezone.utc).isoformat(),
        return_type=str,
        when_used="json",
    ),
]
DateType = Annotated[date, PlainSerializer(lambda dt: dt.isoformat(), return_type=str, when_used="json")]
TimeType = Annotated[
    time,
    PlainSerializer(
        lambda dt: dt.replace(microsecond=0, tzinfo=timezone.utc).isoformat(),
        return_type=str,
        when_used="json",
    ),
]
ObjectIdType = Annotated[ObjectId, PlainSerializer(lambda oid: str(oid), return_type=str, when_used="json")]


class CamelModel(BaseModel):
    """
    Replacement for pydanitc BaseModel which simply adds a camel case alias to every field
    NOTE: This has been updated for Pydantic 2 to remove some common encoding helpers
    """

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class FileDownloadRef(CamelModel):
    name: str
    url: str
    extension: str
    size: int

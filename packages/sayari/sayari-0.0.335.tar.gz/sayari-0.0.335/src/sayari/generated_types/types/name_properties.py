# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .language import Language


class NameProperties(pydantic_v1.BaseModel):
    context: typing.Optional[str] = None
    date: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    as-of date
    """

    from_date: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    start date
    """

    language: typing.Optional[Language] = pydantic_v1.Field(default=None)
    """
    The language that the name is in
    """

    to_date: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    end date
    """

    translated: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    The name value translated to English
    """

    transliterated: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    The name value transliterated to English
    """

    value: str = pydantic_v1.Field()
    """
    The name, as text
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}

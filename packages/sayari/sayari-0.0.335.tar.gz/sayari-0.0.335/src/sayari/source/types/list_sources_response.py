# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...base_types.types.paginated_response import PaginatedResponse
from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .source import Source


class ListSourcesResponse(PaginatedResponse):
    """
    OK

    Examples
    --------
    from sayari import ListSourcesResponse, QualifiedCount, Source

    ListSourcesResponse(
        offset=0,
        limit=2,
        size=QualifiedCount(
            count=547,
            qualifier="eq",
        ),
        next=True,
        data=[
            Source(
                id="e85d865943ee6d8369307569d2ad9de0",
                label="Acuris Risk Intelligence Adverse Media Data",
                description="Contains PDFs and URLs to adverse media reporting for PEPs, SOEs, sanctioned entities, and entities linked to financial regulatory and law enforcement actions. Available for millions of entities from 'Acuris Risk Intelligence KYC6 (3rd Party Data)' in 'Records' section.",
                country="XXX",
                region="international_(multi-region_coverage)",
                date_added="2022-04-11",
                source_type="adverse_media_/_negative_news_data",
                record_type="adverse_media_record",
                structure="unstructured",
                source_url="https://www.acurisriskintelligence.com/",
                pep=False,
                watchlist=False,
            ),
            Source(
                id="a8c6ee1cd4dfc952105ee8c0e4836f08",
                label="Acuris Risk Intelligence KYC6 (3rd Party Data)",
                description="Contains profiles of PEPs, sanctioned entities, SOEs, and entities linked to financial regulatory and law enforcement actions from hundreds of international watchlists. Provides identifying information on individuals and companies as available.",
                country="XXX",
                region="international_(multi-region_coverage)",
                date_added="2022-02-09",
                source_type="risk_intelligence_data",
                record_type="risk_intelligence_record",
                structure="unstructured",
                source_url="https://www.acurisriskintelligence.com/",
                pep=False,
                watchlist=False,
            ),
        ],
    )
    """

    offset: int
    next: bool
    data: typing.List[Source]

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
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}

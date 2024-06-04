# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field
from lusid.models.lusid_trade_ticket import LusidTradeTicket
from lusid.models.resource_id import ResourceId

class PortfolioTradeTicket(BaseModel):
    """
    Response for querying trade tickets  # noqa: E501
    """
    source_portfolio_id: Optional[ResourceId] = Field(None, alias="sourcePortfolioId")
    trade_ticket: Optional[LusidTradeTicket] = Field(None, alias="tradeTicket")
    __properties = ["sourcePortfolioId", "tradeTicket"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> PortfolioTradeTicket:
        """Create an instance of PortfolioTradeTicket from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of source_portfolio_id
        if self.source_portfolio_id:
            _dict['sourcePortfolioId'] = self.source_portfolio_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of trade_ticket
        if self.trade_ticket:
            _dict['tradeTicket'] = self.trade_ticket.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PortfolioTradeTicket:
        """Create an instance of PortfolioTradeTicket from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PortfolioTradeTicket.parse_obj(obj)

        _obj = PortfolioTradeTicket.parse_obj({
            "source_portfolio_id": ResourceId.from_dict(obj.get("sourcePortfolioId")) if obj.get("sourcePortfolioId") is not None else None,
            "trade_ticket": LusidTradeTicket.from_dict(obj.get("tradeTicket")) if obj.get("tradeTicket") is not None else None
        })
        return _obj

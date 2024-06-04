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

from datetime import datetime
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from lusid.models.currency_and_amount import CurrencyAndAmount
from lusid.models.perpetual_property import PerpetualProperty
from lusid.models.resource_id import ResourceId

class OrderInstructionRequest(BaseModel):
    """
    A request to create or update a Order Instruction.  # noqa: E501
    """
    id: ResourceId = Field(...)
    created_date: datetime = Field(..., alias="createdDate", description="The active date of this order instruction.")
    portfolio_id: Optional[ResourceId] = Field(None, alias="portfolioId")
    instrument_identifiers: Optional[Dict[str, StrictStr]] = Field(None, alias="instrumentIdentifiers", description="The instrument ordered.")
    quantity: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The quantity of given instrument ordered.")
    weight: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The weight of given instrument ordered.")
    price: Optional[CurrencyAndAmount] = None
    properties: Optional[Dict[str, PerpetualProperty]] = Field(None, description="Client-defined properties associated with this execution.")
    __properties = ["id", "createdDate", "portfolioId", "instrumentIdentifiers", "quantity", "weight", "price", "properties"]

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
    def from_json(cls, json_str: str) -> OrderInstructionRequest:
        """Create an instance of OrderInstructionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of portfolio_id
        if self.portfolio_id:
            _dict['portfolioId'] = self.portfolio_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of price
        if self.price:
            _dict['price'] = self.price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in properties (dict)
        _field_dict = {}
        if self.properties:
            for _key in self.properties:
                if self.properties[_key]:
                    _field_dict[_key] = self.properties[_key].to_dict()
            _dict['properties'] = _field_dict
        # set to None if instrument_identifiers (nullable) is None
        # and __fields_set__ contains the field
        if self.instrument_identifiers is None and "instrument_identifiers" in self.__fields_set__:
            _dict['instrumentIdentifiers'] = None

        # set to None if quantity (nullable) is None
        # and __fields_set__ contains the field
        if self.quantity is None and "quantity" in self.__fields_set__:
            _dict['quantity'] = None

        # set to None if weight (nullable) is None
        # and __fields_set__ contains the field
        if self.weight is None and "weight" in self.__fields_set__:
            _dict['weight'] = None

        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrderInstructionRequest:
        """Create an instance of OrderInstructionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrderInstructionRequest.parse_obj(obj)

        _obj = OrderInstructionRequest.parse_obj({
            "id": ResourceId.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "created_date": obj.get("createdDate"),
            "portfolio_id": ResourceId.from_dict(obj.get("portfolioId")) if obj.get("portfolioId") is not None else None,
            "instrument_identifiers": obj.get("instrumentIdentifiers"),
            "quantity": obj.get("quantity"),
            "weight": obj.get("weight"),
            "price": CurrencyAndAmount.from_dict(obj.get("price")) if obj.get("price") is not None else None,
            "properties": dict(
                (_k, PerpetualProperty.from_dict(_v))
                for _k, _v in obj.get("properties").items()
            )
            if obj.get("properties") is not None
            else None
        })
        return _obj

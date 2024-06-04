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
from pydantic.v1 import BaseModel, StrictStr
from lusid.models.client import Client

class DataScope(BaseModel):
    """
    DataScope
    """
    client: Optional[Client] = None
    scope: Optional[StrictStr] = None
    __properties = ["client", "scope"]

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
    def from_json(cls, json_str: str) -> DataScope:
        """Create an instance of DataScope from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of client
        if self.client:
            _dict['client'] = self.client.to_dict()
        # set to None if scope (nullable) is None
        # and __fields_set__ contains the field
        if self.scope is None and "scope" in self.__fields_set__:
            _dict['scope'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DataScope:
        """Create an instance of DataScope from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DataScope.parse_obj(obj)

        _obj = DataScope.parse_obj({
            "client": Client.from_dict(obj.get("client")) if obj.get("client") is not None else None,
            "scope": obj.get("scope")
        })
        return _obj

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


from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class FeeAccrual(BaseModel):
    """
    FeeAccrual
    """
    name: Optional[StrictStr] = None
    calculation_base: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="calculationBase")
    amount: Optional[Union[StrictFloat, StrictInt]] = None
    previous_accrual: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="previousAccrual")
    total_accrual: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalAccrual")
    __properties = ["name", "calculationBase", "amount", "previousAccrual", "totalAccrual"]

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
    def from_json(cls, json_str: str) -> FeeAccrual:
        """Create an instance of FeeAccrual from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "total_accrual",
                          },
                          exclude_none=True)
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FeeAccrual:
        """Create an instance of FeeAccrual from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FeeAccrual.parse_obj(obj)

        _obj = FeeAccrual.parse_obj({
            "name": obj.get("name"),
            "calculation_base": obj.get("calculationBase"),
            "amount": obj.get("amount"),
            "previous_accrual": obj.get("previousAccrual"),
            "total_accrual": obj.get("totalAccrual")
        })
        return _obj

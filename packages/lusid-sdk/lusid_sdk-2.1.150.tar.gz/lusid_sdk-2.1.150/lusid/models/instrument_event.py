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


from typing import Any, Dict, Union
from pydantic.v1 import BaseModel, Field, StrictStr, validator
import lusid.models

class InstrumentEvent(BaseModel):
    """
    Base class for representing instrument events in LUSID, such as dividends, stock splits, and option exercises.  This base class should not be directly instantiated; each supported InstrumentEventType has a corresponding inherited class.  # noqa: E501
    """
    instrument_event_type: StrictStr = Field(..., alias="instrumentEventType", description="The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent")
    __properties = ["instrumentEventType"]

    @validator('instrument_event_type')
    def instrument_event_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('TransitionEvent', 'InformationalEvent', 'OpenEvent', 'CloseEvent', 'StockSplitEvent', 'BondDefaultEvent', 'CashDividendEvent', 'AmortisationEvent', 'CashFlowEvent', 'ExerciseEvent', 'ResetEvent', 'TriggerEvent', 'RawVendorEvent', 'InformationalErrorEvent', 'BondCouponEvent', 'DividendReinvestmentEvent', 'AccumulationEvent', 'BondPrincipalEvent', 'DividendOptionEvent', 'MaturityEvent', 'FxForwardSettlementEvent', 'ExpiryEvent', 'ScripDividendEvent', 'StockDividendEvent', 'ReverseStockSplitEvent', 'CapitalDistributionEvent', 'SpinOffEvent'):
            raise ValueError("must be one of enum values ('TransitionEvent', 'InformationalEvent', 'OpenEvent', 'CloseEvent', 'StockSplitEvent', 'BondDefaultEvent', 'CashDividendEvent', 'AmortisationEvent', 'CashFlowEvent', 'ExerciseEvent', 'ResetEvent', 'TriggerEvent', 'RawVendorEvent', 'InformationalErrorEvent', 'BondCouponEvent', 'DividendReinvestmentEvent', 'AccumulationEvent', 'BondPrincipalEvent', 'DividendOptionEvent', 'MaturityEvent', 'FxForwardSettlementEvent', 'ExpiryEvent', 'ScripDividendEvent', 'StockDividendEvent', 'ReverseStockSplitEvent', 'CapitalDistributionEvent', 'SpinOffEvent')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    # JSON field name that stores the object type
    __discriminator_property_name = 'instrumentEventType'

    # discriminator mappings
    __discriminator_value_class_map = {
        'AccumulationEvent': 'AccumulationEvent',
        'AmortisationEvent': 'AmortisationEvent',
        'BondCouponEvent': 'BondCouponEvent',
        'BondDefaultEvent': 'BondDefaultEvent',
        'BondPrincipalEvent': 'BondPrincipalEvent',
        'CapitalDistributionEvent': 'CapitalDistributionEvent',
        'CashDividendEvent': 'CashDividendEvent',
        'CashFlowEvent': 'CashFlowEvent',
        'CloseEvent': 'CloseEvent',
        'DividendOptionEvent': 'DividendOptionEvent',
        'DividendReinvestmentEvent': 'DividendReinvestmentEvent',
        'ExerciseEvent': 'ExerciseEvent',
        'ExpiryEvent': 'ExpiryEvent',
        'FxForwardSettlementEvent': 'FxForwardSettlementEvent',
        'InformationalErrorEvent': 'InformationalErrorEvent',
        'InformationalEvent': 'InformationalEvent',
        'MaturityEvent': 'MaturityEvent',
        'OpenEvent': 'OpenEvent',
        'RawVendorEvent': 'RawVendorEvent',
        'ResetEvent': 'ResetEvent',
        'ReverseStockSplitEvent': 'ReverseStockSplitEvent',
        'ScripDividendEvent': 'ScripDividendEvent',
        'SpinOffEvent': 'SpinOffEvent',
        'StockDividendEvent': 'StockDividendEvent',
        'StockSplitEvent': 'StockSplitEvent',
        'TransitionEvent': 'TransitionEvent',
        'TriggerEvent': 'TriggerEvent'
    }

    @classmethod
    def get_discriminator_value(cls, obj: dict) -> str:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Union(AccumulationEvent, AmortisationEvent, BondCouponEvent, BondDefaultEvent, BondPrincipalEvent, CapitalDistributionEvent, CashDividendEvent, CashFlowEvent, CloseEvent, DividendOptionEvent, DividendReinvestmentEvent, ExerciseEvent, ExpiryEvent, FxForwardSettlementEvent, InformationalErrorEvent, InformationalEvent, MaturityEvent, OpenEvent, RawVendorEvent, ResetEvent, ReverseStockSplitEvent, ScripDividendEvent, SpinOffEvent, StockDividendEvent, StockSplitEvent, TransitionEvent, TriggerEvent):
        """Create an instance of InstrumentEvent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Union(AccumulationEvent, AmortisationEvent, BondCouponEvent, BondDefaultEvent, BondPrincipalEvent, CapitalDistributionEvent, CashDividendEvent, CashFlowEvent, CloseEvent, DividendOptionEvent, DividendReinvestmentEvent, ExerciseEvent, ExpiryEvent, FxForwardSettlementEvent, InformationalErrorEvent, InformationalEvent, MaturityEvent, OpenEvent, RawVendorEvent, ResetEvent, ReverseStockSplitEvent, ScripDividendEvent, SpinOffEvent, StockDividendEvent, StockSplitEvent, TransitionEvent, TriggerEvent):
        """Create an instance of InstrumentEvent from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = getattr(lusid.models, object_type)
            return klass.from_dict(obj)
        else:
            raise ValueError("InstrumentEvent failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

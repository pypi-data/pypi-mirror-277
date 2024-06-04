# coding: utf-8

"""
    Edge Impulse API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field
from edgeimpulse_api.models.dsp_performance_all_variants_response_all_of_performance import DspPerformanceAllVariantsResponseAllOfPerformance

class DspPerformanceAllVariantsResponseAllOf(BaseModel):
    performance: Optional[List[DspPerformanceAllVariantsResponseAllOfPerformance]] = Field(None, description="List of performance estimates for each supported MCU.")
    __properties = ["performance"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = False

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> DspPerformanceAllVariantsResponseAllOf:
        """Create an instance of DspPerformanceAllVariantsResponseAllOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in performance (list)
        _items = []
        if self.performance:
            for _item in self.performance:
                if _item:
                    _items.append(_item.to_dict())
            _dict['performance'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DspPerformanceAllVariantsResponseAllOf:
        """Create an instance of DspPerformanceAllVariantsResponseAllOf from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DspPerformanceAllVariantsResponseAllOf.construct(**obj)

        _obj = DspPerformanceAllVariantsResponseAllOf.construct(**{
            "performance": [DspPerformanceAllVariantsResponseAllOfPerformance.from_dict(_item) for _item in obj.get("performance")] if obj.get("performance") is not None else None
        })
        return _obj


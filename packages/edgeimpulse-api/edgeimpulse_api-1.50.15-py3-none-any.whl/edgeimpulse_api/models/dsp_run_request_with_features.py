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


from typing import Dict, List
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

class DspRunRequestWithFeatures(BaseModel):
    features: List[StrictInt] = Field(..., description="Array of features. If you have multiple axes the data should be interleaved (e.g. [ax0_val0, ax1_val0, ax2_val0, ax0_val1, ax1_val1, ax2_val1]).")
    params: Dict[str, StrictStr] = Field(..., description="DSP parameters with values")
    draw_graphs: StrictBool = Field(..., alias="drawGraphs", description="Whether to generate graphs (will take longer)")
    request_performance: StrictBool = Field(..., alias="requestPerformance", description="Whether to request performance info (will take longer unless cached)")
    __properties = ["features", "params", "drawGraphs", "requestPerformance"]

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
    def from_json(cls, json_str: str) -> DspRunRequestWithFeatures:
        """Create an instance of DspRunRequestWithFeatures from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DspRunRequestWithFeatures:
        """Create an instance of DspRunRequestWithFeatures from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DspRunRequestWithFeatures.construct(**obj)

        _obj = DspRunRequestWithFeatures.construct(**{
            "features": obj.get("features"),
            "params": obj.get("params"),
            "draw_graphs": obj.get("drawGraphs"),
            "request_performance": obj.get("requestPerformance")
        })
        return _obj


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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

class DSPInfoFeatures(BaseModel):
    generated: StrictBool = Field(..., description="Whether this block has generated features")
    count: Optional[StrictInt] = Field(None, description="Number of generated features")
    labels: Optional[List[StrictStr]] = Field(None, description="Names of the features")
    classes: Optional[List[StrictStr]] = Field(None, description="Classes that the features were generated on")
    __properties = ["generated", "count", "labels", "classes"]

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
    def from_json(cls, json_str: str) -> DSPInfoFeatures:
        """Create an instance of DSPInfoFeatures from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DSPInfoFeatures:
        """Create an instance of DSPInfoFeatures from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DSPInfoFeatures.construct(**obj)

        _obj = DSPInfoFeatures.construct(**{
            "generated": obj.get("generated"),
            "count": obj.get("count"),
            "labels": obj.get("labels"),
            "classes": obj.get("classes")
        })
        return _obj


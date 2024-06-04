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


from typing import Dict, Optional
from pydantic import BaseModel, Field

class AnomalyTrainedFeaturesResponseAllOfData(BaseModel):
    x: Dict[str, float] = Field(..., alias="X", description="Data by feature index for this window. Note that this data was scaled by the StandardScaler, use the anomaly metadata to unscale if needed.")
    label: Optional[float] = Field(None, description="Label used for datapoint colorscale in anomaly explorer (for gmm only). Is currently the result of the scoring function.")
    __properties = ["X", "label"]

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
    def from_json(cls, json_str: str) -> AnomalyTrainedFeaturesResponseAllOfData:
        """Create an instance of AnomalyTrainedFeaturesResponseAllOfData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AnomalyTrainedFeaturesResponseAllOfData:
        """Create an instance of AnomalyTrainedFeaturesResponseAllOfData from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AnomalyTrainedFeaturesResponseAllOfData.construct(**obj)

        _obj = AnomalyTrainedFeaturesResponseAllOfData.construct(**{
            "x": obj.get("X"),
            "label": obj.get("label")
        })
        return _obj


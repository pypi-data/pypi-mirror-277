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
from pydantic import BaseModel, Field, StrictBool
from edgeimpulse_api.models.get_pretrained_model_response_all_of_model import GetPretrainedModelResponseAllOfModel
from edgeimpulse_api.models.get_pretrained_model_response_all_of_model_info import GetPretrainedModelResponseAllOfModelInfo
from edgeimpulse_api.models.keras_model_type_enum import KerasModelTypeEnum

class GetPretrainedModelResponseAllOf(BaseModel):
    specific_device_selected: StrictBool = Field(..., alias="specificDeviceSelected", description="Whether a specific device was selected for performance profiling")
    available_model_types: List[KerasModelTypeEnum] = Field(..., alias="availableModelTypes", description="The types of model that are available")
    model: Optional[GetPretrainedModelResponseAllOfModel] = None
    model_info: Optional[GetPretrainedModelResponseAllOfModelInfo] = Field(None, alias="modelInfo")
    __properties = ["specificDeviceSelected", "availableModelTypes", "model", "modelInfo"]

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
    def from_json(cls, json_str: str) -> GetPretrainedModelResponseAllOf:
        """Create an instance of GetPretrainedModelResponseAllOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of model
        if self.model:
            _dict['model'] = self.model.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model_info
        if self.model_info:
            _dict['modelInfo'] = self.model_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetPretrainedModelResponseAllOf:
        """Create an instance of GetPretrainedModelResponseAllOf from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return GetPretrainedModelResponseAllOf.construct(**obj)

        _obj = GetPretrainedModelResponseAllOf.construct(**{
            "specific_device_selected": obj.get("specificDeviceSelected"),
            "available_model_types": obj.get("availableModelTypes"),
            "model": GetPretrainedModelResponseAllOfModel.from_dict(obj.get("model")) if obj.get("model") is not None else None,
            "model_info": GetPretrainedModelResponseAllOfModelInfo.from_dict(obj.get("modelInfo")) if obj.get("modelInfo") is not None else None
        })
        return _obj


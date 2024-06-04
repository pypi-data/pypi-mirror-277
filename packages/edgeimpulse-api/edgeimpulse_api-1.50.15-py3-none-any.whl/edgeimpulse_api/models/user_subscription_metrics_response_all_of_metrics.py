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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class UserSubscriptionMetricsResponseAllOfMetrics(BaseModel):
    compute_minutes_cpu: float = Field(..., alias="computeMinutesCpu", description="Total compute of all user jobs, running on CPU, in the current billing period.")
    compute_minutes_gpu: float = Field(..., alias="computeMinutesGpu", description="Total compute of all user jobs, running on GPU, in the current billing period.")
    compute_minutes_total: float = Field(..., alias="computeMinutesTotal", description="Total compute of all user jobs in the current billing period, calculated as CPU + 3*GPU compute.")
    compute_minutes_limit: float = Field(..., alias="computeMinutesLimit", description="Overall compute limit for the current billing period.")
    compute_reset_date: Optional[datetime] = Field(None, alias="computeResetDate", description="The date at which the current compute billing period will reset.")
    __properties = ["computeMinutesCpu", "computeMinutesGpu", "computeMinutesTotal", "computeMinutesLimit", "computeResetDate"]

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
    def from_json(cls, json_str: str) -> UserSubscriptionMetricsResponseAllOfMetrics:
        """Create an instance of UserSubscriptionMetricsResponseAllOfMetrics from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserSubscriptionMetricsResponseAllOfMetrics:
        """Create an instance of UserSubscriptionMetricsResponseAllOfMetrics from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return UserSubscriptionMetricsResponseAllOfMetrics.construct(**obj)

        _obj = UserSubscriptionMetricsResponseAllOfMetrics.construct(**{
            "compute_minutes_cpu": obj.get("computeMinutesCpu"),
            "compute_minutes_gpu": obj.get("computeMinutesGpu"),
            "compute_minutes_total": obj.get("computeMinutesTotal"),
            "compute_minutes_limit": obj.get("computeMinutesLimit"),
            "compute_reset_date": obj.get("computeResetDate")
        })
        return _obj


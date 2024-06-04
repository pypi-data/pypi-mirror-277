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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class UpdateOrganizationBucketRequest(BaseModel):
    access_key: Optional[StrictStr] = Field(None, alias="accessKey", description="S3 access key")
    secret_key: Optional[StrictStr] = Field(None, alias="secretKey", description="S3 secret key")
    endpoint: Optional[StrictStr] = Field(None, description="S3 endpoint")
    bucket: Optional[StrictStr] = Field(None, description="S3 bucket")
    region: Optional[StrictStr] = Field(None, description="S3 region")
    check_connectivity_prefix: Optional[StrictStr] = Field(None, alias="checkConnectivityPrefix", description="Set this if you don't have access to the root of this bucket. Only used to verify connectivity to this bucket.")
    __properties = ["accessKey", "secretKey", "endpoint", "bucket", "region", "checkConnectivityPrefix"]

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
    def from_json(cls, json_str: str) -> UpdateOrganizationBucketRequest:
        """Create an instance of UpdateOrganizationBucketRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateOrganizationBucketRequest:
        """Create an instance of UpdateOrganizationBucketRequest from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return UpdateOrganizationBucketRequest.construct(**obj)

        _obj = UpdateOrganizationBucketRequest.construct(**{
            "access_key": obj.get("accessKey"),
            "secret_key": obj.get("secretKey"),
            "endpoint": obj.get("endpoint"),
            "bucket": obj.get("bucket"),
            "region": obj.get("region"),
            "check_connectivity_prefix": obj.get("checkConnectivityPrefix")
        })
        return _obj


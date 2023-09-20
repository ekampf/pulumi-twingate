# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetTwingateUserResult',
    'AwaitableGetTwingateUserResult',
    'get_twingate_user',
    'get_twingate_user_output',
]

@pulumi.output_type
class GetTwingateUserResult:
    """
    A collection of values returned by getTwingateUser.
    """
    def __init__(__self__, email=None, first_name=None, id=None, is_admin=None, last_name=None, role=None, type=None):
        if email and not isinstance(email, str):
            raise TypeError("Expected argument 'email' to be a str")
        pulumi.set(__self__, "email", email)
        if first_name and not isinstance(first_name, str):
            raise TypeError("Expected argument 'first_name' to be a str")
        pulumi.set(__self__, "first_name", first_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_admin and not isinstance(is_admin, bool):
            raise TypeError("Expected argument 'is_admin' to be a bool")
        pulumi.set(__self__, "is_admin", is_admin)
        if last_name and not isinstance(last_name, str):
            raise TypeError("Expected argument 'last_name' to be a str")
        pulumi.set(__self__, "last_name", last_name)
        if role and not isinstance(role, str):
            raise TypeError("Expected argument 'role' to be a str")
        pulumi.set(__self__, "role", role)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def email(self) -> str:
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> str:
        return pulumi.get(self, "first_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isAdmin")
    def is_admin(self) -> bool:
        warnings.warn("""This read-only Boolean value will be deprecated in a future release. You may use the `role` value instead.""", DeprecationWarning)
        pulumi.log.warn("""is_admin is deprecated: This read-only Boolean value will be deprecated in a future release. You may use the `role` value instead.""")

        return pulumi.get(self, "is_admin")

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> str:
        return pulumi.get(self, "last_name")

    @property
    @pulumi.getter
    def role(self) -> str:
        return pulumi.get(self, "role")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")


class AwaitableGetTwingateUserResult(GetTwingateUserResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTwingateUserResult(
            email=self.email,
            first_name=self.first_name,
            id=self.id,
            is_admin=self.is_admin,
            last_name=self.last_name,
            role=self.role,
            type=self.type)


def get_twingate_user(id: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTwingateUserResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('twingate:index/getTwingateUser:getTwingateUser', __args__, opts=opts, typ=GetTwingateUserResult).value

    return AwaitableGetTwingateUserResult(
        email=pulumi.get(__ret__, 'email'),
        first_name=pulumi.get(__ret__, 'first_name'),
        id=pulumi.get(__ret__, 'id'),
        is_admin=pulumi.get(__ret__, 'is_admin'),
        last_name=pulumi.get(__ret__, 'last_name'),
        role=pulumi.get(__ret__, 'role'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_twingate_user)
def get_twingate_user_output(id: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTwingateUserResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...

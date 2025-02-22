# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'TwingateResourceProtocolsArgs',
    'TwingateResourceProtocolsTcpArgs',
    'TwingateResourceProtocolsUdpArgs',
]

@pulumi.input_type
class TwingateResourceProtocolsArgs:
    def __init__(__self__, *,
                 tcp: pulumi.Input['TwingateResourceProtocolsTcpArgs'],
                 udp: pulumi.Input['TwingateResourceProtocolsUdpArgs'],
                 allow_icmp: Optional[pulumi.Input[bool]] = None):
        pulumi.set(__self__, "tcp", tcp)
        pulumi.set(__self__, "udp", udp)
        if allow_icmp is not None:
            pulumi.set(__self__, "allow_icmp", allow_icmp)

    @property
    @pulumi.getter
    def tcp(self) -> pulumi.Input['TwingateResourceProtocolsTcpArgs']:
        return pulumi.get(self, "tcp")

    @tcp.setter
    def tcp(self, value: pulumi.Input['TwingateResourceProtocolsTcpArgs']):
        pulumi.set(self, "tcp", value)

    @property
    @pulumi.getter
    def udp(self) -> pulumi.Input['TwingateResourceProtocolsUdpArgs']:
        return pulumi.get(self, "udp")

    @udp.setter
    def udp(self, value: pulumi.Input['TwingateResourceProtocolsUdpArgs']):
        pulumi.set(self, "udp", value)

    @property
    @pulumi.getter(name="allowIcmp")
    def allow_icmp(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "allow_icmp")

    @allow_icmp.setter
    def allow_icmp(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_icmp", value)


@pulumi.input_type
class TwingateResourceProtocolsTcpArgs:
    def __init__(__self__, *,
                 policy: pulumi.Input[str],
                 ports: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        pulumi.set(__self__, "policy", policy)
        if ports is not None:
            pulumi.set(__self__, "ports", ports)

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Input[str]:
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter
    def ports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "ports")

    @ports.setter
    def ports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ports", value)


@pulumi.input_type
class TwingateResourceProtocolsUdpArgs:
    def __init__(__self__, *,
                 policy: pulumi.Input[str],
                 ports: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        pulumi.set(__self__, "policy", policy)
        if ports is not None:
            pulumi.set(__self__, "ports", ports)

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Input[str]:
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter
    def ports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "ports")

    @ports.setter
    def ports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ports", value)



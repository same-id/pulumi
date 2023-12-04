# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'TestResult',
    'AwaitableTestResult',
    'test',
    'test_output',
]

@pulumi.output_type
class TestResult:
    def __init__(__self__, id=None, urn=None):
        if id and not isinstance(id, float):
            raise TypeError("Expected argument 'id' to be a float")
        pulumi.set(__self__, "id", id)
        if urn and not isinstance(urn, float):
            raise TypeError("Expected argument 'urn' to be a float")
        pulumi.set(__self__, "urn", urn)

    @property
    @pulumi.getter
    def id(self) -> Optional[float]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def urn(self) -> float:
        return pulumi.get(self, "urn")


class AwaitableTestResult(TestResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return TestResult(
            id=self.id,
            urn=self.urn)


def test(id: Optional[float] = None,
         urn: Optional[float] = None,
         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableTestResult:
    """
    It's fine for invokes to use urn and id
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['urn'] = urn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('urnid:index:Test', __args__, opts=opts, typ=TestResult).value

    return AwaitableTestResult(
        id=pulumi.get(__ret__, 'id'),
        urn=pulumi.get(__ret__, 'urn'))


@_utilities.lift_output_func(test)
def test_output(id: Optional[pulumi.Input[float]] = None,
                urn: Optional[pulumi.Input[float]] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[TestResult]:
    """
    It's fine for invokes to use urn and id
    """
    ...
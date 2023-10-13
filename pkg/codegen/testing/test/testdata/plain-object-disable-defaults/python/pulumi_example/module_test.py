# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import mod1 as _mod1
from . import mod2 as _mod2
from ._inputs import *

__all__ = ['ModuleTestArgs', 'ModuleTest']

@pulumi.input_type
class ModuleTestArgs:
    def __init__(__self__, *,
                 mod1: Optional[pulumi.Input['_mod1.TypArgs']] = None,
                 val: Optional[pulumi.Input['TypArgs']] = None):
        """
        The set of arguments for constructing a ModuleTest resource.
        """
        ModuleTestArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            mod1=mod1,
            val=val,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             mod1: Optional[pulumi.Input['_mod1.TypArgs']] = None,
             val: Optional[pulumi.Input['TypArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):

        if mod1 is not None:
            _setter("mod1", mod1)
        if val is not None:
            _setter("val", val)

    @property
    @pulumi.getter
    def mod1(self) -> Optional[pulumi.Input['_mod1.TypArgs']]:
        return pulumi.get(self, "mod1")

    @mod1.setter
    def mod1(self, value: Optional[pulumi.Input['_mod1.TypArgs']]):
        pulumi.set(self, "mod1", value)

    @property
    @pulumi.getter
    def val(self) -> Optional[pulumi.Input['TypArgs']]:
        return pulumi.get(self, "val")

    @val.setter
    def val(self, value: Optional[pulumi.Input['TypArgs']]):
        pulumi.set(self, "val", value)


class ModuleTest(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 mod1: Optional[pulumi.Input[pulumi.InputType['_mod1.TypArgs']]] = None,
                 val: Optional[pulumi.Input[pulumi.InputType['TypArgs']]] = None,
                 __props__=None):
        """
        Create a ModuleTest resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ModuleTestArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ModuleTest resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ModuleTestArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ModuleTestArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ModuleTestArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 mod1: Optional[pulumi.Input[pulumi.InputType['_mod1.TypArgs']]] = None,
                 val: Optional[pulumi.Input[pulumi.InputType['TypArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ModuleTestArgs.__new__(ModuleTestArgs)

            if mod1 is not None and not isinstance(mod1, _mod1.TypArgs):
                mod1 = mod1 or {}
                def _setter(key, value):
                    mod1[key] = value
                _mod1.TypArgs._configure(_setter, **mod1)
            __props__.__dict__["mod1"] = mod1
            if val is not None and not isinstance(val, TypArgs):
                val = val or {}
                def _setter(key, value):
                    val[key] = value
                TypArgs._configure(_setter, **val)
            __props__.__dict__["val"] = val
        super(ModuleTest, __self__).__init__(
            'example:index:moduleTest',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ModuleTest':
        """
        Get an existing ModuleTest resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ModuleTestArgs.__new__(ModuleTestArgs)

        return ModuleTest(resource_name, opts=opts, __props__=__props__)


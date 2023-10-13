# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from .cat import Cat
from .dog import Dog

__all__ = ['ToyStoreArgs', 'ToyStore']

@pulumi.input_type
class ToyStoreArgs:
    def __init__(__self__):
        """
        The set of arguments for constructing a ToyStore resource.
        """
        pass
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        pass



class ToyStore(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 __props__=None):
        """
        Create a ToyStore resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ToyStoreArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ToyStore resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ToyStoreArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ToyStoreArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ToyStoreArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ToyStoreArgs.__new__(ToyStoreArgs)

            __props__.__dict__["chew"] = None
            __props__.__dict__["laser"] = None
            __props__.__dict__["stuff"] = None
            __props__.__dict__["wanted"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["chew.owner", "laser.batteries", "stuff[*].associated.color", "stuff[*].color", "wanted[*]"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ToyStore, __self__).__init__(
            'example::ToyStore',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ToyStore':
        """
        Get an existing ToyStore resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ToyStoreArgs.__new__(ToyStoreArgs)

        __props__.__dict__["chew"] = None
        __props__.__dict__["laser"] = None
        __props__.__dict__["stuff"] = None
        __props__.__dict__["wanted"] = None
        return ToyStore(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def chew(self) -> pulumi.Output[Optional['outputs.Chew']]:
        return pulumi.get(self, "chew")

    @property
    @pulumi.getter
    def laser(self) -> pulumi.Output[Optional['outputs.Laser']]:
        return pulumi.get(self, "laser")

    @property
    @pulumi.getter
    def stuff(self) -> pulumi.Output[Optional[Sequence['outputs.Toy']]]:
        return pulumi.get(self, "stuff")

    @property
    @pulumi.getter
    def wanted(self) -> pulumi.Output[Optional[Sequence['outputs.Toy']]]:
        return pulumi.get(self, "wanted")


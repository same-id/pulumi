# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['ConfigGroupArgs', 'ConfigGroup']

@pulumi.input_type
class ConfigGroupArgs:
    def __init__(__self__, *,
                 files: Optional[pulumi.Input[Union[str, Sequence[pulumi.Input[str]]]]] = None,
                 objs: Optional[pulumi.Input[Union[Any, Sequence[Any]]]] = None,
                 resource_prefix: Optional[pulumi.Input[str]] = None,
                 yaml: Optional[pulumi.Input[Union[str, Sequence[pulumi.Input[str]]]]] = None):
        """
        The set of arguments for constructing a ConfigGroup resource.
        :param pulumi.Input[Union[str, Sequence[pulumi.Input[str]]]] files: Set of paths or a URLs that uniquely identify files.
        :param pulumi.Input[Union[Any, Sequence[Any]]] objs: Objects representing Kubernetes resources.
        :param pulumi.Input[str] resource_prefix: An optional prefix for the auto-generated resource names. Example: A resource created with resourcePrefix="foo" would produce a resource named "foo-resourceName".
        :param pulumi.Input[Union[str, Sequence[pulumi.Input[str]]]] yaml: YAML text containing Kubernetes resource definitions.
        """
        if files is not None:
            pulumi.set(__self__, "files", files)
        if objs is not None:
            pulumi.set(__self__, "objs", objs)
        if resource_prefix is not None:
            pulumi.set(__self__, "resource_prefix", resource_prefix)
        if yaml is not None:
            pulumi.set(__self__, "yaml", yaml)

    @property
    @pulumi.getter
    def files(self) -> Optional[pulumi.Input[Union[str, Sequence[pulumi.Input[str]]]]]:
        """
        Set of paths or a URLs that uniquely identify files.
        """
        return pulumi.get(self, "files")

    @files.setter
    def files(self, value: Optional[pulumi.Input[Union[str, Sequence[pulumi.Input[str]]]]]):
        pulumi.set(self, "files", value)

    @property
    @pulumi.getter
    def objs(self) -> Optional[pulumi.Input[Union[Any, Sequence[Any]]]]:
        """
        Objects representing Kubernetes resources.
        """
        return pulumi.get(self, "objs")

    @objs.setter
    def objs(self, value: Optional[pulumi.Input[Union[Any, Sequence[Any]]]]):
        pulumi.set(self, "objs", value)

    @property
    @pulumi.getter(name="resourcePrefix")
    def resource_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        An optional prefix for the auto-generated resource names. Example: A resource created with resourcePrefix="foo" would produce a resource named "foo-resourceName".
        """
        return pulumi.get(self, "resource_prefix")

    @resource_prefix.setter
    def resource_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_prefix", value)

    @property
    @pulumi.getter
    def yaml(self) -> Optional[pulumi.Input[Union[str, Sequence[pulumi.Input[str]]]]]:
        """
        YAML text containing Kubernetes resource definitions.
        """
        return pulumi.get(self, "yaml")

    @yaml.setter
    def yaml(self, value: Optional[pulumi.Input[Union[str, Sequence[pulumi.Input[str]]]]]):
        pulumi.set(self, "yaml", value)


class ConfigGroup(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 files: Optional[pulumi.Input[Union[str, Sequence[pulumi.Input[str]]]]] = None,
                 objs: Optional[pulumi.Input[Union[Any, Sequence[Any]]]] = None,
                 resource_prefix: Optional[pulumi.Input[str]] = None,
                 yaml: Optional[pulumi.Input[Union[str, Sequence[pulumi.Input[str]]]]] = None,
                 __props__=None):
        """
        A non-overlay component resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, Sequence[pulumi.Input[str]]]] files: Set of paths or a URLs that uniquely identify files.
        :param pulumi.Input[Union[Any, Sequence[Any]]] objs: Objects representing Kubernetes resources.
        :param pulumi.Input[str] resource_prefix: An optional prefix for the auto-generated resource names. Example: A resource created with resourcePrefix="foo" would produce a resource named "foo-resourceName".
        :param pulumi.Input[Union[str, Sequence[pulumi.Input[str]]]] yaml: YAML text containing Kubernetes resource definitions.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ConfigGroupArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A non-overlay component resource.

        :param str resource_name: The name of the resource.
        :param ConfigGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConfigGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 files: Optional[pulumi.Input[Union[str, Sequence[pulumi.Input[str]]]]] = None,
                 objs: Optional[pulumi.Input[Union[Any, Sequence[Any]]]] = None,
                 resource_prefix: Optional[pulumi.Input[str]] = None,
                 yaml: Optional[pulumi.Input[Union[str, Sequence[pulumi.Input[str]]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConfigGroupArgs.__new__(ConfigGroupArgs)

            __props__.__dict__["files"] = files
            __props__.__dict__["objs"] = objs
            __props__.__dict__["resource_prefix"] = resource_prefix
            __props__.__dict__["yaml"] = yaml
            __props__.__dict__["resources"] = None
        super(ConfigGroup, __self__).__init__(
            'kubernetes:yaml/v2:ConfigGroup',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter
    def resources(self) -> pulumi.Output[Optional[Sequence[Any]]]:
        """
        Resources created by the ConfigGroup.
        """
        return pulumi.get(self, "resources")


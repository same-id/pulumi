# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_gcp.compute.instance as __instance
    instance = __instance
    import pulumi_gcp.compute.instancebootdisk as __instancebootdisk
    instancebootdisk = __instancebootdisk
    import pulumi_gcp.compute.instancebootdiskinitializeparams as __instancebootdiskinitializeparams
    instancebootdiskinitializeparams = __instancebootdiskinitializeparams
else:
    instance = _utilities.lazy_import('pulumi_gcp.compute.instance')
    instancebootdisk = _utilities.lazy_import('pulumi_gcp.compute.instancebootdisk')
    instancebootdiskinitializeparams = _utilities.lazy_import('pulumi_gcp.compute.instancebootdiskinitializeparams')


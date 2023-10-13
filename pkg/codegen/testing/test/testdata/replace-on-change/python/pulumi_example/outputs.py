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

__all__ = [
    'Chew',
    'Laser',
    'Rec',
    'Toy',
]

@pulumi.output_type
class Chew(dict):
    """
    A toy for a dog
    """
    def __init__(__self__, *,
                 owner: Optional['Dog'] = None):
        """
        A toy for a dog
        """
        Chew._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            owner=owner,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             owner: Optional['Dog'] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):

        if owner is not None:
            _setter("owner", owner)

    @property
    @pulumi.getter
    def owner(self) -> Optional['Dog']:
        return pulumi.get(self, "owner")


@pulumi.output_type
class Laser(dict):
    """
    A Toy for a cat
    """
    def __init__(__self__, *,
                 animal: Optional['Cat'] = None,
                 batteries: Optional[bool] = None,
                 light: Optional[float] = None):
        """
        A Toy for a cat
        """
        Laser._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            animal=animal,
            batteries=batteries,
            light=light,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             animal: Optional['Cat'] = None,
             batteries: Optional[bool] = None,
             light: Optional[float] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):

        if animal is not None:
            _setter("animal", animal)
        if batteries is not None:
            _setter("batteries", batteries)
        if light is not None:
            _setter("light", light)

    @property
    @pulumi.getter
    def animal(self) -> Optional['Cat']:
        return pulumi.get(self, "animal")

    @property
    @pulumi.getter
    def batteries(self) -> Optional[bool]:
        return pulumi.get(self, "batteries")

    @property
    @pulumi.getter
    def light(self) -> Optional[float]:
        return pulumi.get(self, "light")


@pulumi.output_type
class Rec(dict):
    def __init__(__self__, *,
                 rec1: Optional['outputs.Rec'] = None):
        Rec._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            rec1=rec1,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             rec1: Optional['outputs.Rec'] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):

        if rec1 is not None:
            _setter("rec1", rec1)

    @property
    @pulumi.getter
    def rec1(self) -> Optional['outputs.Rec']:
        return pulumi.get(self, "rec1")


@pulumi.output_type
class Toy(dict):
    """
    This is a toy
    """
    def __init__(__self__, *,
                 associated: Optional['outputs.Toy'] = None,
                 color: Optional[str] = None,
                 wear: Optional[float] = None):
        """
        This is a toy
        """
        Toy._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            associated=associated,
            color=color,
            wear=wear,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             associated: Optional['outputs.Toy'] = None,
             color: Optional[str] = None,
             wear: Optional[float] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):

        if associated is not None:
            _setter("associated", associated)
        if color is not None:
            _setter("color", color)
        if wear is not None:
            _setter("wear", wear)

    @property
    @pulumi.getter
    def associated(self) -> Optional['outputs.Toy']:
        return pulumi.get(self, "associated")

    @property
    @pulumi.getter
    def color(self) -> Optional[str]:
        return pulumi.get(self, "color")

    @property
    @pulumi.getter
    def wear(self) -> Optional[float]:
        return pulumi.get(self, "wear")



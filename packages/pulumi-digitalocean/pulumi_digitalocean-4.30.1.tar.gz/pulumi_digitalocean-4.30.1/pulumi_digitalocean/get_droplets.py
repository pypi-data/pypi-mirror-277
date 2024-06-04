# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetDropletsResult',
    'AwaitableGetDropletsResult',
    'get_droplets',
    'get_droplets_output',
]

@pulumi.output_type
class GetDropletsResult:
    """
    A collection of values returned by getDroplets.
    """
    def __init__(__self__, droplets=None, filters=None, id=None, sorts=None):
        if droplets and not isinstance(droplets, list):
            raise TypeError("Expected argument 'droplets' to be a list")
        pulumi.set(__self__, "droplets", droplets)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if sorts and not isinstance(sorts, list):
            raise TypeError("Expected argument 'sorts' to be a list")
        pulumi.set(__self__, "sorts", sorts)

    @property
    @pulumi.getter
    def droplets(self) -> Sequence['outputs.GetDropletsDropletResult']:
        """
        A list of Droplets satisfying any `filter` and `sort` criteria. Each Droplet has the following attributes:
        """
        return pulumi.get(self, "droplets")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetDropletsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def sorts(self) -> Optional[Sequence['outputs.GetDropletsSortResult']]:
        return pulumi.get(self, "sorts")


class AwaitableGetDropletsResult(GetDropletsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDropletsResult(
            droplets=self.droplets,
            filters=self.filters,
            id=self.id,
            sorts=self.sorts)


def get_droplets(filters: Optional[Sequence[pulumi.InputType['GetDropletsFilterArgs']]] = None,
                 sorts: Optional[Sequence[pulumi.InputType['GetDropletsSortArgs']]] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDropletsResult:
    """
    Get information on Droplets for use in other resources, with the ability to filter and sort the results.
    If no filters are specified, all Droplets will be returned.

    This data source is useful if the Droplets in question are not managed by the provider or you need to
    utilize any of the Droplets' data.

    Note: You can use the `Droplet` data source to obtain metadata
    about a single Droplet if you already know the `id`, unique `name`, or unique `tag` to retrieve.

    ## Example Usage

    Use the `filter` block with a `key` string and `values` list to filter images.

    For example to find all Droplets with size `s-1vcpu-1gb`:

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    small = digitalocean.get_droplets(filters=[digitalocean.GetDropletsFilterArgs(
        key="size",
        values=["s-1vcpu-1gb"],
    )])
    ```

    You can filter on multiple fields and sort the results as well:

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    small_with_backups = digitalocean.get_droplets(filters=[
            digitalocean.GetDropletsFilterArgs(
                key="size",
                values=["s-1vcpu-1gb"],
            ),
            digitalocean.GetDropletsFilterArgs(
                key="backups",
                values=["true"],
            ),
        ],
        sorts=[digitalocean.GetDropletsSortArgs(
            key="created_at",
            direction="desc",
        )])
    ```


    :param Sequence[pulumi.InputType['GetDropletsFilterArgs']] filters: Filter the results.
           The `filter` block is documented below.
    :param Sequence[pulumi.InputType['GetDropletsSortArgs']] sorts: Sort the results.
           The `sort` block is documented below.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['sorts'] = sorts
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('digitalocean:index/getDroplets:getDroplets', __args__, opts=opts, typ=GetDropletsResult).value

    return AwaitableGetDropletsResult(
        droplets=pulumi.get(__ret__, 'droplets'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        sorts=pulumi.get(__ret__, 'sorts'))


@_utilities.lift_output_func(get_droplets)
def get_droplets_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetDropletsFilterArgs']]]]] = None,
                        sorts: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetDropletsSortArgs']]]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDropletsResult]:
    """
    Get information on Droplets for use in other resources, with the ability to filter and sort the results.
    If no filters are specified, all Droplets will be returned.

    This data source is useful if the Droplets in question are not managed by the provider or you need to
    utilize any of the Droplets' data.

    Note: You can use the `Droplet` data source to obtain metadata
    about a single Droplet if you already know the `id`, unique `name`, or unique `tag` to retrieve.

    ## Example Usage

    Use the `filter` block with a `key` string and `values` list to filter images.

    For example to find all Droplets with size `s-1vcpu-1gb`:

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    small = digitalocean.get_droplets(filters=[digitalocean.GetDropletsFilterArgs(
        key="size",
        values=["s-1vcpu-1gb"],
    )])
    ```

    You can filter on multiple fields and sort the results as well:

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    small_with_backups = digitalocean.get_droplets(filters=[
            digitalocean.GetDropletsFilterArgs(
                key="size",
                values=["s-1vcpu-1gb"],
            ),
            digitalocean.GetDropletsFilterArgs(
                key="backups",
                values=["true"],
            ),
        ],
        sorts=[digitalocean.GetDropletsSortArgs(
            key="created_at",
            direction="desc",
        )])
    ```


    :param Sequence[pulumi.InputType['GetDropletsFilterArgs']] filters: Filter the results.
           The `filter` block is documented below.
    :param Sequence[pulumi.InputType['GetDropletsSortArgs']] sorts: Sort the results.
           The `sort` block is documented below.
    """
    ...

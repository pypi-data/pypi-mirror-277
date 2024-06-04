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
    'GetSpacesBucketsResult',
    'AwaitableGetSpacesBucketsResult',
    'get_spaces_buckets',
    'get_spaces_buckets_output',
]

@pulumi.output_type
class GetSpacesBucketsResult:
    """
    A collection of values returned by getSpacesBuckets.
    """
    def __init__(__self__, buckets=None, filters=None, id=None, sorts=None):
        if buckets and not isinstance(buckets, list):
            raise TypeError("Expected argument 'buckets' to be a list")
        pulumi.set(__self__, "buckets", buckets)
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
    def buckets(self) -> Sequence['outputs.GetSpacesBucketsBucketResult']:
        """
        A list of Spaces buckets satisfying any `filter` and `sort` criteria. Each bucket has the following attributes:
        """
        return pulumi.get(self, "buckets")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetSpacesBucketsFilterResult']]:
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
    def sorts(self) -> Optional[Sequence['outputs.GetSpacesBucketsSortResult']]:
        return pulumi.get(self, "sorts")


class AwaitableGetSpacesBucketsResult(GetSpacesBucketsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSpacesBucketsResult(
            buckets=self.buckets,
            filters=self.filters,
            id=self.id,
            sorts=self.sorts)


def get_spaces_buckets(filters: Optional[Sequence[pulumi.InputType['GetSpacesBucketsFilterArgs']]] = None,
                       sorts: Optional[Sequence[pulumi.InputType['GetSpacesBucketsSortArgs']]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSpacesBucketsResult:
    """
    Get information on Spaces buckets for use in other resources, with the ability to filter and sort the results.
    If no filters are specified, all Spaces buckets will be returned.

    Note: You can use the `SpacesBucket` data source to
    obtain metadata about a single bucket if you already know its `name` and `region`.

    ## Example Usage

    Use the `filter` block with a `key` string and `values` list to filter buckets.

    Get all buckets in a region:

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    nyc3 = digitalocean.get_spaces_buckets(filters=[digitalocean.GetSpacesBucketsFilterArgs(
        key="region",
        values=["nyc3"],
    )])
    ```
    You can sort the results as well:

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    nyc3 = digitalocean.get_spaces_buckets(filters=[digitalocean.GetSpacesBucketsFilterArgs(
            key="region",
            values=["nyc3"],
        )],
        sorts=[digitalocean.GetSpacesBucketsSortArgs(
            key="name",
            direction="desc",
        )])
    ```


    :param Sequence[pulumi.InputType['GetSpacesBucketsFilterArgs']] filters: Filter the results.
           The `filter` block is documented below.
    :param Sequence[pulumi.InputType['GetSpacesBucketsSortArgs']] sorts: Sort the results.
           The `sort` block is documented below.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['sorts'] = sorts
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('digitalocean:index/getSpacesBuckets:getSpacesBuckets', __args__, opts=opts, typ=GetSpacesBucketsResult).value

    return AwaitableGetSpacesBucketsResult(
        buckets=pulumi.get(__ret__, 'buckets'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        sorts=pulumi.get(__ret__, 'sorts'))


@_utilities.lift_output_func(get_spaces_buckets)
def get_spaces_buckets_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetSpacesBucketsFilterArgs']]]]] = None,
                              sorts: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetSpacesBucketsSortArgs']]]]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSpacesBucketsResult]:
    """
    Get information on Spaces buckets for use in other resources, with the ability to filter and sort the results.
    If no filters are specified, all Spaces buckets will be returned.

    Note: You can use the `SpacesBucket` data source to
    obtain metadata about a single bucket if you already know its `name` and `region`.

    ## Example Usage

    Use the `filter` block with a `key` string and `values` list to filter buckets.

    Get all buckets in a region:

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    nyc3 = digitalocean.get_spaces_buckets(filters=[digitalocean.GetSpacesBucketsFilterArgs(
        key="region",
        values=["nyc3"],
    )])
    ```
    You can sort the results as well:

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    nyc3 = digitalocean.get_spaces_buckets(filters=[digitalocean.GetSpacesBucketsFilterArgs(
            key="region",
            values=["nyc3"],
        )],
        sorts=[digitalocean.GetSpacesBucketsSortArgs(
            key="name",
            direction="desc",
        )])
    ```


    :param Sequence[pulumi.InputType['GetSpacesBucketsFilterArgs']] filters: Filter the results.
           The `filter` block is documented below.
    :param Sequence[pulumi.InputType['GetSpacesBucketsSortArgs']] sorts: Sort the results.
           The `sort` block is documented below.
    """
    ...

# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetVpcPeeringResult',
    'AwaitableGetVpcPeeringResult',
    'get_vpc_peering',
    'get_vpc_peering_output',
]

@pulumi.output_type
class GetVpcPeeringResult:
    """
    A collection of values returned by getVpcPeering.
    """
    def __init__(__self__, created_at=None, id=None, name=None, status=None, vpc_ids=None):
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if vpc_ids and not isinstance(vpc_ids, list):
            raise TypeError("Expected argument 'vpc_ids' to be a list")
        pulumi.set(__self__, "vpc_ids", vpc_ids)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        The date and time of when the VPC Peering was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The unique identifier for the VPC Peering.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the VPC Peering.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the VPC Peering.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="vpcIds")
    def vpc_ids(self) -> Sequence[str]:
        """
        The list of VPC IDs involved in the peering.
        """
        return pulumi.get(self, "vpc_ids")


class AwaitableGetVpcPeeringResult(GetVpcPeeringResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVpcPeeringResult(
            created_at=self.created_at,
            id=self.id,
            name=self.name,
            status=self.status,
            vpc_ids=self.vpc_ids)


def get_vpc_peering(id: Optional[str] = None,
                    name: Optional[str] = None,
                    vpc_ids: Optional[Sequence[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVpcPeeringResult:
    """
    ## Example Usage

    ### VPC Peering By Id

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    example = digitalocean.get_vpc_peering(id="example-id")
    ```

    Reuse the data about a VPC Peering in other resources:

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    example = digitalocean.get_vpc_peering(id="example-id")
    example_droplet = digitalocean.Droplet("example",
        name="example-01",
        size=digitalocean.DropletSlug.DROPLET_S1_VCPU1_GB,
        image="ubuntu-18-04-x64",
        region=digitalocean.Region.NYC3,
        vpc_uuid=example.vpc_ids[0])
    ```

    ### VPC Peering By Name

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    example = digitalocean.get_vpc_peering(name="example-peering")
    ```

    Reuse the data about a VPC Peering in other resources:

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    example = digitalocean.get_vpc_peering(name="example-peering")
    example_droplet = digitalocean.Droplet("example",
        name="example-01",
        size=digitalocean.DropletSlug.DROPLET_S1_VCPU1_GB,
        image="ubuntu-18-04-x64",
        region=digitalocean.Region.NYC3,
        vpc_uuid=example.vpc_ids[0])
    ```


    :param str id: The unique identifier of an existing VPC Peering.
    :param str name: The name of an existing VPC Peering.
    :param Sequence[str] vpc_ids: The list of VPC IDs involved in the peering.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['vpcIds'] = vpc_ids
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('digitalocean:index/getVpcPeering:getVpcPeering', __args__, opts=opts, typ=GetVpcPeeringResult).value

    return AwaitableGetVpcPeeringResult(
        created_at=pulumi.get(__ret__, 'created_at'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        status=pulumi.get(__ret__, 'status'),
        vpc_ids=pulumi.get(__ret__, 'vpc_ids'))


@_utilities.lift_output_func(get_vpc_peering)
def get_vpc_peering_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                           name: Optional[pulumi.Input[Optional[str]]] = None,
                           vpc_ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVpcPeeringResult]:
    """
    ## Example Usage

    ### VPC Peering By Id

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    example = digitalocean.get_vpc_peering(id="example-id")
    ```

    Reuse the data about a VPC Peering in other resources:

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    example = digitalocean.get_vpc_peering(id="example-id")
    example_droplet = digitalocean.Droplet("example",
        name="example-01",
        size=digitalocean.DropletSlug.DROPLET_S1_VCPU1_GB,
        image="ubuntu-18-04-x64",
        region=digitalocean.Region.NYC3,
        vpc_uuid=example.vpc_ids[0])
    ```

    ### VPC Peering By Name

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    example = digitalocean.get_vpc_peering(name="example-peering")
    ```

    Reuse the data about a VPC Peering in other resources:

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    example = digitalocean.get_vpc_peering(name="example-peering")
    example_droplet = digitalocean.Droplet("example",
        name="example-01",
        size=digitalocean.DropletSlug.DROPLET_S1_VCPU1_GB,
        image="ubuntu-18-04-x64",
        region=digitalocean.Region.NYC3,
        vpc_uuid=example.vpc_ids[0])
    ```


    :param str id: The unique identifier of an existing VPC Peering.
    :param str name: The name of an existing VPC Peering.
    :param Sequence[str] vpc_ids: The list of VPC IDs involved in the peering.
    """
    ...

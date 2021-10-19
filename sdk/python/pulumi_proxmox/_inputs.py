# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'LXCContainerFeaturesArgs',
    'LXCContainerMountpointArgs',
    'LXCContainerNetworkArgs',
    'LXCContainerRootfsArgs',
    'LXCDiskMountoptionsArgs',
    'QemuVMDiskArgs',
    'QemuVMNetworkArgs',
    'QemuVMSerialArgs',
    'QemuVMUnusedDiskArgs',
    'QemuVMVgaArgs',
]

@pulumi.input_type
class LXCContainerFeaturesArgs:
    def __init__(__self__, *,
                 fuse: Optional[pulumi.Input[bool]] = None,
                 keyctl: Optional[pulumi.Input[bool]] = None,
                 mount: Optional[pulumi.Input[str]] = None,
                 nesting: Optional[pulumi.Input[bool]] = None):
        if fuse is not None:
            pulumi.set(__self__, "fuse", fuse)
        if keyctl is not None:
            pulumi.set(__self__, "keyctl", keyctl)
        if mount is not None:
            pulumi.set(__self__, "mount", mount)
        if nesting is not None:
            pulumi.set(__self__, "nesting", nesting)

    @property
    @pulumi.getter
    def fuse(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "fuse")

    @fuse.setter
    def fuse(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "fuse", value)

    @property
    @pulumi.getter
    def keyctl(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "keyctl")

    @keyctl.setter
    def keyctl(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "keyctl", value)

    @property
    @pulumi.getter
    def mount(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "mount")

    @mount.setter
    def mount(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mount", value)

    @property
    @pulumi.getter
    def nesting(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "nesting")

    @nesting.setter
    def nesting(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "nesting", value)


@pulumi.input_type
class LXCContainerMountpointArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 mp: pulumi.Input[str],
                 size: pulumi.Input[str],
                 slot: pulumi.Input[int],
                 storage: pulumi.Input[str],
                 acl: Optional[pulumi.Input[bool]] = None,
                 backup: Optional[pulumi.Input[bool]] = None,
                 file: Optional[pulumi.Input[str]] = None,
                 quota: Optional[pulumi.Input[bool]] = None,
                 replicate: Optional[pulumi.Input[bool]] = None,
                 shared: Optional[pulumi.Input[bool]] = None,
                 volume: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "mp", mp)
        pulumi.set(__self__, "size", size)
        pulumi.set(__self__, "slot", slot)
        pulumi.set(__self__, "storage", storage)
        if acl is not None:
            pulumi.set(__self__, "acl", acl)
        if backup is not None:
            pulumi.set(__self__, "backup", backup)
        if file is not None:
            pulumi.set(__self__, "file", file)
        if quota is not None:
            pulumi.set(__self__, "quota", quota)
        if replicate is not None:
            pulumi.set(__self__, "replicate", replicate)
        if shared is not None:
            pulumi.set(__self__, "shared", shared)
        if volume is not None:
            pulumi.set(__self__, "volume", volume)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def mp(self) -> pulumi.Input[str]:
        return pulumi.get(self, "mp")

    @mp.setter
    def mp(self, value: pulumi.Input[str]):
        pulumi.set(self, "mp", value)

    @property
    @pulumi.getter
    def size(self) -> pulumi.Input[str]:
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: pulumi.Input[str]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def slot(self) -> pulumi.Input[int]:
        return pulumi.get(self, "slot")

    @slot.setter
    def slot(self, value: pulumi.Input[int]):
        pulumi.set(self, "slot", value)

    @property
    @pulumi.getter
    def storage(self) -> pulumi.Input[str]:
        return pulumi.get(self, "storage")

    @storage.setter
    def storage(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage", value)

    @property
    @pulumi.getter
    def acl(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "acl")

    @acl.setter
    def acl(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "acl", value)

    @property
    @pulumi.getter
    def backup(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "backup")

    @backup.setter
    def backup(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "backup", value)

    @property
    @pulumi.getter
    def file(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "file")

    @file.setter
    def file(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file", value)

    @property
    @pulumi.getter
    def quota(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "quota")

    @quota.setter
    def quota(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "quota", value)

    @property
    @pulumi.getter
    def replicate(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "replicate")

    @replicate.setter
    def replicate(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "replicate", value)

    @property
    @pulumi.getter
    def shared(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "shared")

    @shared.setter
    def shared(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "shared", value)

    @property
    @pulumi.getter
    def volume(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "volume")

    @volume.setter
    def volume(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume", value)


@pulumi.input_type
class LXCContainerNetworkArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 bridge: Optional[pulumi.Input[str]] = None,
                 firewall: Optional[pulumi.Input[bool]] = None,
                 gw: Optional[pulumi.Input[str]] = None,
                 gw6: Optional[pulumi.Input[str]] = None,
                 hwaddr: Optional[pulumi.Input[str]] = None,
                 ip: Optional[pulumi.Input[str]] = None,
                 ip6: Optional[pulumi.Input[str]] = None,
                 mtu: Optional[pulumi.Input[str]] = None,
                 rate: Optional[pulumi.Input[int]] = None,
                 tag: Optional[pulumi.Input[int]] = None,
                 trunks: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "name", name)
        if bridge is not None:
            pulumi.set(__self__, "bridge", bridge)
        if firewall is not None:
            pulumi.set(__self__, "firewall", firewall)
        if gw is not None:
            pulumi.set(__self__, "gw", gw)
        if gw6 is not None:
            pulumi.set(__self__, "gw6", gw6)
        if hwaddr is not None:
            pulumi.set(__self__, "hwaddr", hwaddr)
        if ip is not None:
            pulumi.set(__self__, "ip", ip)
        if ip6 is not None:
            pulumi.set(__self__, "ip6", ip6)
        if mtu is not None:
            pulumi.set(__self__, "mtu", mtu)
        if rate is not None:
            pulumi.set(__self__, "rate", rate)
        if tag is not None:
            pulumi.set(__self__, "tag", tag)
        if trunks is not None:
            pulumi.set(__self__, "trunks", trunks)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def bridge(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "bridge")

    @bridge.setter
    def bridge(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bridge", value)

    @property
    @pulumi.getter
    def firewall(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "firewall")

    @firewall.setter
    def firewall(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "firewall", value)

    @property
    @pulumi.getter
    def gw(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "gw")

    @gw.setter
    def gw(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gw", value)

    @property
    @pulumi.getter
    def gw6(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "gw6")

    @gw6.setter
    def gw6(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gw6", value)

    @property
    @pulumi.getter
    def hwaddr(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "hwaddr")

    @hwaddr.setter
    def hwaddr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hwaddr", value)

    @property
    @pulumi.getter
    def ip(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ip")

    @ip.setter
    def ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip", value)

    @property
    @pulumi.getter
    def ip6(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ip6")

    @ip6.setter
    def ip6(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip6", value)

    @property
    @pulumi.getter
    def mtu(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "mtu")

    @mtu.setter
    def mtu(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mtu", value)

    @property
    @pulumi.getter
    def rate(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "rate")

    @rate.setter
    def rate(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "rate", value)

    @property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "tag")

    @tag.setter
    def tag(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "tag", value)

    @property
    @pulumi.getter
    def trunks(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "trunks")

    @trunks.setter
    def trunks(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "trunks", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class LXCContainerRootfsArgs:
    def __init__(__self__, *,
                 size: pulumi.Input[str],
                 storage: pulumi.Input[str],
                 volume: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "size", size)
        pulumi.set(__self__, "storage", storage)
        if volume is not None:
            pulumi.set(__self__, "volume", volume)

    @property
    @pulumi.getter
    def size(self) -> pulumi.Input[str]:
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: pulumi.Input[str]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def storage(self) -> pulumi.Input[str]:
        return pulumi.get(self, "storage")

    @storage.setter
    def storage(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage", value)

    @property
    @pulumi.getter
    def volume(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "volume")

    @volume.setter
    def volume(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume", value)


@pulumi.input_type
class LXCDiskMountoptionsArgs:
    def __init__(__self__, *,
                 noatime: Optional[pulumi.Input[bool]] = None,
                 nodev: Optional[pulumi.Input[bool]] = None,
                 noexec: Optional[pulumi.Input[str]] = None,
                 nosuid: Optional[pulumi.Input[bool]] = None):
        if noatime is not None:
            pulumi.set(__self__, "noatime", noatime)
        if nodev is not None:
            pulumi.set(__self__, "nodev", nodev)
        if noexec is not None:
            pulumi.set(__self__, "noexec", noexec)
        if nosuid is not None:
            pulumi.set(__self__, "nosuid", nosuid)

    @property
    @pulumi.getter
    def noatime(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "noatime")

    @noatime.setter
    def noatime(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "noatime", value)

    @property
    @pulumi.getter
    def nodev(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "nodev")

    @nodev.setter
    def nodev(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "nodev", value)

    @property
    @pulumi.getter
    def noexec(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "noexec")

    @noexec.setter
    def noexec(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "noexec", value)

    @property
    @pulumi.getter
    def nosuid(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "nosuid")

    @nosuid.setter
    def nosuid(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "nosuid", value)


@pulumi.input_type
class QemuVMDiskArgs:
    def __init__(__self__, *,
                 size: pulumi.Input[str],
                 storage: pulumi.Input[str],
                 type: pulumi.Input[str],
                 backup: Optional[pulumi.Input[int]] = None,
                 cache: Optional[pulumi.Input[str]] = None,
                 discard: Optional[pulumi.Input[str]] = None,
                 file: Optional[pulumi.Input[str]] = None,
                 format: Optional[pulumi.Input[str]] = None,
                 iothread: Optional[pulumi.Input[int]] = None,
                 mbps: Optional[pulumi.Input[int]] = None,
                 mbps_rd: Optional[pulumi.Input[int]] = None,
                 mbps_rd_max: Optional[pulumi.Input[int]] = None,
                 mbps_wr: Optional[pulumi.Input[int]] = None,
                 mbps_wr_max: Optional[pulumi.Input[int]] = None,
                 media: Optional[pulumi.Input[str]] = None,
                 replicate: Optional[pulumi.Input[int]] = None,
                 slot: Optional[pulumi.Input[int]] = None,
                 ssd: Optional[pulumi.Input[int]] = None,
                 storage_type: Optional[pulumi.Input[str]] = None,
                 volume: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "size", size)
        pulumi.set(__self__, "storage", storage)
        pulumi.set(__self__, "type", type)
        if backup is not None:
            pulumi.set(__self__, "backup", backup)
        if cache is not None:
            pulumi.set(__self__, "cache", cache)
        if discard is not None:
            pulumi.set(__self__, "discard", discard)
        if file is not None:
            pulumi.set(__self__, "file", file)
        if format is not None:
            pulumi.set(__self__, "format", format)
        if iothread is not None:
            pulumi.set(__self__, "iothread", iothread)
        if mbps is not None:
            pulumi.set(__self__, "mbps", mbps)
        if mbps_rd is not None:
            pulumi.set(__self__, "mbps_rd", mbps_rd)
        if mbps_rd_max is not None:
            pulumi.set(__self__, "mbps_rd_max", mbps_rd_max)
        if mbps_wr is not None:
            pulumi.set(__self__, "mbps_wr", mbps_wr)
        if mbps_wr_max is not None:
            pulumi.set(__self__, "mbps_wr_max", mbps_wr_max)
        if media is not None:
            pulumi.set(__self__, "media", media)
        if replicate is not None:
            pulumi.set(__self__, "replicate", replicate)
        if slot is not None:
            pulumi.set(__self__, "slot", slot)
        if ssd is not None:
            pulumi.set(__self__, "ssd", ssd)
        if storage_type is not None:
            pulumi.set(__self__, "storage_type", storage_type)
        if volume is not None:
            pulumi.set(__self__, "volume", volume)

    @property
    @pulumi.getter
    def size(self) -> pulumi.Input[str]:
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: pulumi.Input[str]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def storage(self) -> pulumi.Input[str]:
        return pulumi.get(self, "storage")

    @storage.setter
    def storage(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def backup(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "backup")

    @backup.setter
    def backup(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "backup", value)

    @property
    @pulumi.getter
    def cache(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cache")

    @cache.setter
    def cache(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cache", value)

    @property
    @pulumi.getter
    def discard(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "discard")

    @discard.setter
    def discard(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "discard", value)

    @property
    @pulumi.getter
    def file(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "file")

    @file.setter
    def file(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file", value)

    @property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "format")

    @format.setter
    def format(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "format", value)

    @property
    @pulumi.getter
    def iothread(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "iothread")

    @iothread.setter
    def iothread(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "iothread", value)

    @property
    @pulumi.getter
    def mbps(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "mbps")

    @mbps.setter
    def mbps(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "mbps", value)

    @property
    @pulumi.getter(name="mbpsRd")
    def mbps_rd(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "mbps_rd")

    @mbps_rd.setter
    def mbps_rd(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "mbps_rd", value)

    @property
    @pulumi.getter(name="mbpsRdMax")
    def mbps_rd_max(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "mbps_rd_max")

    @mbps_rd_max.setter
    def mbps_rd_max(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "mbps_rd_max", value)

    @property
    @pulumi.getter(name="mbpsWr")
    def mbps_wr(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "mbps_wr")

    @mbps_wr.setter
    def mbps_wr(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "mbps_wr", value)

    @property
    @pulumi.getter(name="mbpsWrMax")
    def mbps_wr_max(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "mbps_wr_max")

    @mbps_wr_max.setter
    def mbps_wr_max(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "mbps_wr_max", value)

    @property
    @pulumi.getter
    def media(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "media")

    @media.setter
    def media(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "media", value)

    @property
    @pulumi.getter
    def replicate(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "replicate")

    @replicate.setter
    def replicate(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "replicate", value)

    @property
    @pulumi.getter
    def slot(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "slot")

    @slot.setter
    def slot(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "slot", value)

    @property
    @pulumi.getter
    def ssd(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "ssd")

    @ssd.setter
    def ssd(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ssd", value)

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "storage_type")

    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_type", value)

    @property
    @pulumi.getter
    def volume(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "volume")

    @volume.setter
    def volume(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume", value)


@pulumi.input_type
class QemuVMNetworkArgs:
    def __init__(__self__, *,
                 model: pulumi.Input[str],
                 bridge: Optional[pulumi.Input[str]] = None,
                 firewall: Optional[pulumi.Input[bool]] = None,
                 link_down: Optional[pulumi.Input[bool]] = None,
                 macaddr: Optional[pulumi.Input[str]] = None,
                 queues: Optional[pulumi.Input[int]] = None,
                 rate: Optional[pulumi.Input[int]] = None,
                 tag: Optional[pulumi.Input[int]] = None):
        pulumi.set(__self__, "model", model)
        if bridge is not None:
            pulumi.set(__self__, "bridge", bridge)
        if firewall is not None:
            pulumi.set(__self__, "firewall", firewall)
        if link_down is not None:
            pulumi.set(__self__, "link_down", link_down)
        if macaddr is not None:
            pulumi.set(__self__, "macaddr", macaddr)
        if queues is not None:
            pulumi.set(__self__, "queues", queues)
        if rate is not None:
            pulumi.set(__self__, "rate", rate)
        if tag is not None:
            pulumi.set(__self__, "tag", tag)

    @property
    @pulumi.getter
    def model(self) -> pulumi.Input[str]:
        return pulumi.get(self, "model")

    @model.setter
    def model(self, value: pulumi.Input[str]):
        pulumi.set(self, "model", value)

    @property
    @pulumi.getter
    def bridge(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "bridge")

    @bridge.setter
    def bridge(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bridge", value)

    @property
    @pulumi.getter
    def firewall(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "firewall")

    @firewall.setter
    def firewall(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "firewall", value)

    @property
    @pulumi.getter(name="linkDown")
    def link_down(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "link_down")

    @link_down.setter
    def link_down(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "link_down", value)

    @property
    @pulumi.getter
    def macaddr(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "macaddr")

    @macaddr.setter
    def macaddr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "macaddr", value)

    @property
    @pulumi.getter
    def queues(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "queues")

    @queues.setter
    def queues(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "queues", value)

    @property
    @pulumi.getter
    def rate(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "rate")

    @rate.setter
    def rate(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "rate", value)

    @property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "tag")

    @tag.setter
    def tag(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "tag", value)


@pulumi.input_type
class QemuVMSerialArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[int],
                 type: pulumi.Input[str]):
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[int]:
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[int]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class QemuVMUnusedDiskArgs:
    def __init__(__self__, *,
                 file: Optional[pulumi.Input[str]] = None,
                 slot: Optional[pulumi.Input[int]] = None,
                 storage: Optional[pulumi.Input[str]] = None):
        if file is not None:
            pulumi.set(__self__, "file", file)
        if slot is not None:
            pulumi.set(__self__, "slot", slot)
        if storage is not None:
            pulumi.set(__self__, "storage", storage)

    @property
    @pulumi.getter
    def file(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "file")

    @file.setter
    def file(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file", value)

    @property
    @pulumi.getter
    def slot(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "slot")

    @slot.setter
    def slot(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "slot", value)

    @property
    @pulumi.getter
    def storage(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "storage")

    @storage.setter
    def storage(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage", value)


@pulumi.input_type
class QemuVMVgaArgs:
    def __init__(__self__, *,
                 memory: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        if memory is not None:
            pulumi.set(__self__, "memory", memory)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def memory(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "memory")

    @memory.setter
    def memory(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "memory", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)



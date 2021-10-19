# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'LXCContainerFeatures',
    'LXCContainerMountpoint',
    'LXCContainerNetwork',
    'LXCContainerRootfs',
    'LXCDiskMountoptions',
    'QemuVMDisk',
    'QemuVMNetwork',
    'QemuVMSerial',
    'QemuVMUnusedDisk',
    'QemuVMVga',
]

@pulumi.output_type
class LXCContainerFeatures(dict):
    def __init__(__self__, *,
                 fuse: Optional[bool] = None,
                 keyctl: Optional[bool] = None,
                 mount: Optional[str] = None,
                 nesting: Optional[bool] = None):
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
    def fuse(self) -> Optional[bool]:
        return pulumi.get(self, "fuse")

    @property
    @pulumi.getter
    def keyctl(self) -> Optional[bool]:
        return pulumi.get(self, "keyctl")

    @property
    @pulumi.getter
    def mount(self) -> Optional[str]:
        return pulumi.get(self, "mount")

    @property
    @pulumi.getter
    def nesting(self) -> Optional[bool]:
        return pulumi.get(self, "nesting")


@pulumi.output_type
class LXCContainerMountpoint(dict):
    def __init__(__self__, *,
                 key: str,
                 mp: str,
                 size: str,
                 slot: int,
                 storage: str,
                 acl: Optional[bool] = None,
                 backup: Optional[bool] = None,
                 file: Optional[str] = None,
                 quota: Optional[bool] = None,
                 replicate: Optional[bool] = None,
                 shared: Optional[bool] = None,
                 volume: Optional[str] = None):
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
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def mp(self) -> str:
        return pulumi.get(self, "mp")

    @property
    @pulumi.getter
    def size(self) -> str:
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def slot(self) -> int:
        return pulumi.get(self, "slot")

    @property
    @pulumi.getter
    def storage(self) -> str:
        return pulumi.get(self, "storage")

    @property
    @pulumi.getter
    def acl(self) -> Optional[bool]:
        return pulumi.get(self, "acl")

    @property
    @pulumi.getter
    def backup(self) -> Optional[bool]:
        return pulumi.get(self, "backup")

    @property
    @pulumi.getter
    def file(self) -> Optional[str]:
        return pulumi.get(self, "file")

    @property
    @pulumi.getter
    def quota(self) -> Optional[bool]:
        return pulumi.get(self, "quota")

    @property
    @pulumi.getter
    def replicate(self) -> Optional[bool]:
        return pulumi.get(self, "replicate")

    @property
    @pulumi.getter
    def shared(self) -> Optional[bool]:
        return pulumi.get(self, "shared")

    @property
    @pulumi.getter
    def volume(self) -> Optional[str]:
        return pulumi.get(self, "volume")


@pulumi.output_type
class LXCContainerNetwork(dict):
    def __init__(__self__, *,
                 name: str,
                 bridge: Optional[str] = None,
                 firewall: Optional[bool] = None,
                 gw: Optional[str] = None,
                 gw6: Optional[str] = None,
                 hwaddr: Optional[str] = None,
                 ip: Optional[str] = None,
                 ip6: Optional[str] = None,
                 mtu: Optional[str] = None,
                 rate: Optional[int] = None,
                 tag: Optional[int] = None,
                 trunks: Optional[str] = None,
                 type: Optional[str] = None):
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
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def bridge(self) -> Optional[str]:
        return pulumi.get(self, "bridge")

    @property
    @pulumi.getter
    def firewall(self) -> Optional[bool]:
        return pulumi.get(self, "firewall")

    @property
    @pulumi.getter
    def gw(self) -> Optional[str]:
        return pulumi.get(self, "gw")

    @property
    @pulumi.getter
    def gw6(self) -> Optional[str]:
        return pulumi.get(self, "gw6")

    @property
    @pulumi.getter
    def hwaddr(self) -> Optional[str]:
        return pulumi.get(self, "hwaddr")

    @property
    @pulumi.getter
    def ip(self) -> Optional[str]:
        return pulumi.get(self, "ip")

    @property
    @pulumi.getter
    def ip6(self) -> Optional[str]:
        return pulumi.get(self, "ip6")

    @property
    @pulumi.getter
    def mtu(self) -> Optional[str]:
        return pulumi.get(self, "mtu")

    @property
    @pulumi.getter
    def rate(self) -> Optional[int]:
        return pulumi.get(self, "rate")

    @property
    @pulumi.getter
    def tag(self) -> Optional[int]:
        return pulumi.get(self, "tag")

    @property
    @pulumi.getter
    def trunks(self) -> Optional[str]:
        return pulumi.get(self, "trunks")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        return pulumi.get(self, "type")


@pulumi.output_type
class LXCContainerRootfs(dict):
    def __init__(__self__, *,
                 size: str,
                 storage: str,
                 volume: Optional[str] = None):
        pulumi.set(__self__, "size", size)
        pulumi.set(__self__, "storage", storage)
        if volume is not None:
            pulumi.set(__self__, "volume", volume)

    @property
    @pulumi.getter
    def size(self) -> str:
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def storage(self) -> str:
        return pulumi.get(self, "storage")

    @property
    @pulumi.getter
    def volume(self) -> Optional[str]:
        return pulumi.get(self, "volume")


@pulumi.output_type
class LXCDiskMountoptions(dict):
    def __init__(__self__, *,
                 noatime: Optional[bool] = None,
                 nodev: Optional[bool] = None,
                 noexec: Optional[str] = None,
                 nosuid: Optional[bool] = None):
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
    def noatime(self) -> Optional[bool]:
        return pulumi.get(self, "noatime")

    @property
    @pulumi.getter
    def nodev(self) -> Optional[bool]:
        return pulumi.get(self, "nodev")

    @property
    @pulumi.getter
    def noexec(self) -> Optional[str]:
        return pulumi.get(self, "noexec")

    @property
    @pulumi.getter
    def nosuid(self) -> Optional[bool]:
        return pulumi.get(self, "nosuid")


@pulumi.output_type
class QemuVMDisk(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "mbpsRd":
            suggest = "mbps_rd"
        elif key == "mbpsRdMax":
            suggest = "mbps_rd_max"
        elif key == "mbpsWr":
            suggest = "mbps_wr"
        elif key == "mbpsWrMax":
            suggest = "mbps_wr_max"
        elif key == "storageType":
            suggest = "storage_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in QemuVMDisk. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        QemuVMDisk.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        QemuVMDisk.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 size: str,
                 storage: str,
                 type: str,
                 backup: Optional[int] = None,
                 cache: Optional[str] = None,
                 discard: Optional[str] = None,
                 file: Optional[str] = None,
                 format: Optional[str] = None,
                 iothread: Optional[int] = None,
                 mbps: Optional[int] = None,
                 mbps_rd: Optional[int] = None,
                 mbps_rd_max: Optional[int] = None,
                 mbps_wr: Optional[int] = None,
                 mbps_wr_max: Optional[int] = None,
                 media: Optional[str] = None,
                 replicate: Optional[int] = None,
                 slot: Optional[int] = None,
                 ssd: Optional[int] = None,
                 storage_type: Optional[str] = None,
                 volume: Optional[str] = None):
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
    def size(self) -> str:
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def storage(self) -> str:
        return pulumi.get(self, "storage")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def backup(self) -> Optional[int]:
        return pulumi.get(self, "backup")

    @property
    @pulumi.getter
    def cache(self) -> Optional[str]:
        return pulumi.get(self, "cache")

    @property
    @pulumi.getter
    def discard(self) -> Optional[str]:
        return pulumi.get(self, "discard")

    @property
    @pulumi.getter
    def file(self) -> Optional[str]:
        return pulumi.get(self, "file")

    @property
    @pulumi.getter
    def format(self) -> Optional[str]:
        return pulumi.get(self, "format")

    @property
    @pulumi.getter
    def iothread(self) -> Optional[int]:
        return pulumi.get(self, "iothread")

    @property
    @pulumi.getter
    def mbps(self) -> Optional[int]:
        return pulumi.get(self, "mbps")

    @property
    @pulumi.getter(name="mbpsRd")
    def mbps_rd(self) -> Optional[int]:
        return pulumi.get(self, "mbps_rd")

    @property
    @pulumi.getter(name="mbpsRdMax")
    def mbps_rd_max(self) -> Optional[int]:
        return pulumi.get(self, "mbps_rd_max")

    @property
    @pulumi.getter(name="mbpsWr")
    def mbps_wr(self) -> Optional[int]:
        return pulumi.get(self, "mbps_wr")

    @property
    @pulumi.getter(name="mbpsWrMax")
    def mbps_wr_max(self) -> Optional[int]:
        return pulumi.get(self, "mbps_wr_max")

    @property
    @pulumi.getter
    def media(self) -> Optional[str]:
        return pulumi.get(self, "media")

    @property
    @pulumi.getter
    def replicate(self) -> Optional[int]:
        return pulumi.get(self, "replicate")

    @property
    @pulumi.getter
    def slot(self) -> Optional[int]:
        return pulumi.get(self, "slot")

    @property
    @pulumi.getter
    def ssd(self) -> Optional[int]:
        return pulumi.get(self, "ssd")

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[str]:
        return pulumi.get(self, "storage_type")

    @property
    @pulumi.getter
    def volume(self) -> Optional[str]:
        return pulumi.get(self, "volume")


@pulumi.output_type
class QemuVMNetwork(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "linkDown":
            suggest = "link_down"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in QemuVMNetwork. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        QemuVMNetwork.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        QemuVMNetwork.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 model: str,
                 bridge: Optional[str] = None,
                 firewall: Optional[bool] = None,
                 link_down: Optional[bool] = None,
                 macaddr: Optional[str] = None,
                 queues: Optional[int] = None,
                 rate: Optional[int] = None,
                 tag: Optional[int] = None):
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
    def model(self) -> str:
        return pulumi.get(self, "model")

    @property
    @pulumi.getter
    def bridge(self) -> Optional[str]:
        return pulumi.get(self, "bridge")

    @property
    @pulumi.getter
    def firewall(self) -> Optional[bool]:
        return pulumi.get(self, "firewall")

    @property
    @pulumi.getter(name="linkDown")
    def link_down(self) -> Optional[bool]:
        return pulumi.get(self, "link_down")

    @property
    @pulumi.getter
    def macaddr(self) -> Optional[str]:
        return pulumi.get(self, "macaddr")

    @property
    @pulumi.getter
    def queues(self) -> Optional[int]:
        return pulumi.get(self, "queues")

    @property
    @pulumi.getter
    def rate(self) -> Optional[int]:
        return pulumi.get(self, "rate")

    @property
    @pulumi.getter
    def tag(self) -> Optional[int]:
        return pulumi.get(self, "tag")


@pulumi.output_type
class QemuVMSerial(dict):
    def __init__(__self__, *,
                 id: int,
                 type: str):
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> int:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")


@pulumi.output_type
class QemuVMUnusedDisk(dict):
    def __init__(__self__, *,
                 file: Optional[str] = None,
                 slot: Optional[int] = None,
                 storage: Optional[str] = None):
        if file is not None:
            pulumi.set(__self__, "file", file)
        if slot is not None:
            pulumi.set(__self__, "slot", slot)
        if storage is not None:
            pulumi.set(__self__, "storage", storage)

    @property
    @pulumi.getter
    def file(self) -> Optional[str]:
        return pulumi.get(self, "file")

    @property
    @pulumi.getter
    def slot(self) -> Optional[int]:
        return pulumi.get(self, "slot")

    @property
    @pulumi.getter
    def storage(self) -> Optional[str]:
        return pulumi.get(self, "storage")


@pulumi.output_type
class QemuVMVga(dict):
    def __init__(__self__, *,
                 memory: Optional[int] = None,
                 type: Optional[str] = None):
        if memory is not None:
            pulumi.set(__self__, "memory", memory)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def memory(self) -> Optional[int]:
        return pulumi.get(self, "memory")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        return pulumi.get(self, "type")


from pynutanix.lib.nutanix import NutanixAPI
from pynutanix.lib.utils import object_to_dict_converter
import json


class VM:
    def __init__(
        self,
        name=None,
        memory_mb=None,
        num_vcpus=None,
        num_cores_per_vcpu=None,
        vm_disk_uid=None,
        image_disk_uid=None,
        network_uid=None,
        ip_address=None,
        userdata=None,
        uuid=None,
    ) -> None:
        self.name = name
        self.memory_mb = memory_mb
        self.num_vcpus = num_vcpus
        self.num_cores_per_vcpu = num_cores_per_vcpu
        self.vm_disks = [
            dict(is_cdrom=True, is_empty=True),
            dict(
                is_cdrom=False,
                disk_address=dict(device_bus="scsi", vmdisk_uuid=vm_disk_uid),
                vm_disk_clone=dict(disk_address=dict(vmdisk_uuid=image_disk_uid)),
            ),
        ]
        self.vm_nics = [
            dict(
                network_uuid=network_uid,
                requested_ip_address=ip_address,
                is_connected=True,
            )
        ]
        self.vm_customization_config = dict(userdata=userdata)
        self.uuid = uuid
        self.uri = "vms"
        self.nutanix_api = NutanixAPI()

    def create(self):
        count = 0
        vms = self.list()

        for vm in vms.get("entities"):
            if vm["name"] == self.name:
                count += 1
                break
        response = dict()
        payload = json.dumps(object_to_dict_converter(self))

        if count <= 0:
            response = self.nutanix_api.create(
                data=object_to_dict_converter(self), uri=self.uri
            )

        else:
            print(f"Vms {self.name} already exists, nothing to do")

        return response

    def list(self, params=None):
        response = self.nutanix_api.list(uri=self.uri, params=params)

        return response

    def get(self):
        response = self.nutanix_api.get(uri=f"{self.uri}/{self.uuid}")

        return response

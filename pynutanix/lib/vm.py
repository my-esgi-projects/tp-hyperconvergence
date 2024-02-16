from pynutanix.lib.nutanix import NutanixAPI
from pynutanix.lib.utils import object_to_dict_converter


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
                vm_disk_clone=dict(disk_address=dict(vmdisk_uuid=image_disk_uid))
            )
        ]
        self.vm_nics = [
            dict(network_uuid=network_uid, requested_ip_address=ip_address, is_connected=True)
        ]
        self.vm_customization_config = dict(userdata=userdata)
        self.uuid = uuid
        self.uri = "vms"
        self.nutanix_api = NutanixAPI()

    def create(self):
        response = self.nutanix_api.create(
            data=object_to_dict_converter(self), uri=self.uri
        )

        return object_to_dict_converter(self)

    def update(self):
        response = self.nutanix_api.create(
            data=object_to_dict_converter(self), uri=f"{self.uri}/{self.uuid}"
        )

        return response

    def list(self):
        response = self.nutanix_api.list(uri=self.uri)

        return response

    def get(self):
        response = self.nutanix_api.get(uri=f"{self.uri}/{self.uuid}")

        return response

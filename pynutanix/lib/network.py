from pynutanix.lib.nutanix import NutanixAPI
from pynutanix.lib.utils import object_to_dict_converter


class Network():
    def __init__(self, name=None, vlan_id=None, ip_config=None, uuid=None) -> None:
        self.name = name
        self.vlan_id = vlan_id
        self.ip_config = ip_config
        self.uuid = uuid
        self.uri = "networks"
        self.nutanix_api = NutanixAPI()

    def create(self):
        response = self.nutanix_api.create(
            data=object_to_dict_converter(self), uri=self.uri
        )
        response = {"network_uuid": "string"}
        
        return response

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

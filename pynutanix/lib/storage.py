from pynutanix.lib.nutanix import NutanixAPI
from pynutanix.lib.utils import object_to_dict_converter


class Storage():
    def __init__(self, name=None, capacity=None, uuid=None) -> None:
        self.name = name
        self.capacity = capacity
        self.uuid = uuid
        self.uri = "storage_containers"
        self.nutanix_api = NutanixAPI()

    def create(self):
        response = self.nutanix_api.create(
            data=object_to_dict_converter(self), uri=self.uri
        )
        return response

    def update(self):
        response = self.nutanix_api.create(
            data=object_to_dict_converter(self), uri=f"{self.uri}/{self.uuid}"
        )

        return response

    def list(self, params=None):
        response = self.nutanix_api.list(uri=self.uri, params=params)
        
        response = dict(
            entities=[
                dict(container_uuid="toto")
            ]
        )
        
        return response

    def get(self):
        response = self.nutanix_api.get(uri=f"{self.uri}/{self.uuid}")

        return response

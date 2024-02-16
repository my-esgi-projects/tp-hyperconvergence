from pynutanix.lib.nutanix import NutanixAPI
from pynutanix.lib.utils import object_to_dict_converter


class Storage():
    def __init__(self, name=None, capacity=None, uuid=None) -> None:
        self.name = name
        self.advertised_capacity = capacity
        self.uuid = uuid
        self.uri = "storage_containers"
        self.nutanix_api = NutanixAPI()

    def create(self):
        params = {"search_string": self.name}
        storages = self.list(params=params)
    
        #response = self.nutanix_api.create(
        #    data=object_to_dict_converter(self), uri=self.uri
        #)
        return storages

    def update(self):
        response = self.nutanix_api.create(
            data=object_to_dict_converter(self), uri=f"{self.uri}/{self.uuid}"
        )

        return response

    def list(self, params=None):
        response = self.nutanix_api.list(uri=self.uri, params=params)
        
        return response

    def get(self):
        response = self.nutanix_api.get(uri=f"{self.uri}/{self.uuid}")

        return response

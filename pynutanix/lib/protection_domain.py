from pynutanix.lib.nutanix import NutanixAPI
from pynutanix.lib.utils import object_to_dict_converter


class ProtectionDomain:
    def __init__(self, annotations=None, value=None) -> None:
        self.annotations = annotations
        self.value = value
        self.uri = "protection_domains"
        self.nutanix_api = NutanixAPI()

    def create(self):
        protection_domains = self.list()
        count = 0
        response = dict()

        for protection_domain in protection_domains.get("entities"):
            if protection_domain["name"] == self.value:
                count += 1
                break

        if count <= 0:
            response = self.nutanix_api.create(
                data=object_to_dict_converter(self), uri=self.uri
            )
        else:
            print("Protection domains already exists, nothing to do")

        return response, object_to_dict_converter(self)


    def add_vms_and_snapshot_schedules(self, vms:list):
        add_vms_payload = {"names": vms}
        response_adding_vms = self.nutanix_api.create(data=add_vms_payload, uri=f"{self.uri}/{self.value}/protect_vms")
        
        # snapshot_schedule_payload = {"type": "HOURLY", "every_nth": 4}
        # response_snapshot_schedule = self.nutanix_api.create(data=snapshot_schedule_payload, uri=f"{self.uri}/{self.value}/schedules")

        return response_adding_vms


    def list(self, params=None):
        response = self.nutanix_api.list(uri=self.uri, params=params)

        return response


    def get(self):
        response = self.nutanix_api.get(uri=f"{self.uri}/{self.uuid}")

        return response

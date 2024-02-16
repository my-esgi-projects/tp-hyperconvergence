from abc import ABC, abstractmethod
import json
import requests
from pynutanix import config


class NutanixAPI:
    def __init__(self) -> None:
        self.base_url = config.nutanix_api_endpoint
        self.nutanix_api = requests.Session()
        self.nutanix_api.headers = {
            "Accept": "application/json",
        }

        self.nutanix_api.auth = (config.nutanix_user, config.nutanix_password)

    def call(self, method, uri, data=None, params=None, ssl_verify=False):
        response = self.nutanix_api.request(
            method=method,
            url=f"{config.nutanix_api_endpoint}/{uri}",
            json=data,
            params=params,
            verify=ssl_verify,
        )
        try:
            if not response.ok:
                raise Exception(response)
            return response.json()
        except json.decoder.JSONDecodeError:
            raise Exception(f"Could not reach {self.base_url}.")

    def create(self, data: dict, uri: str, params=None):
        response = self.call(method="POST", uri=uri, data=data, params=params)

        return response

    def update(self, data: dict, uri: str, params=None):
        response = self.call(method="PATCH", uri=uri, data=data, params=params)

        return response

    def get(self, uri: str, params=None):
        response = self.call(method="GET", uri=f"{uri}", params=params)

        return response

    def list(self, uri: str, params=None):
        response = self.call(method="GET", uri=f"{uri}", params=params)
        # response = {"value": True}
        return response

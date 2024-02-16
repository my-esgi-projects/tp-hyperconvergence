import os


def get_required_environment(variable: str, is_required=True):
    value = os.environ.get(variable)
    if is_required and not value:
        raise Exception(f"{variable} is required")
    else:
        return value


nutanix_api_endpoint = os.environ.get(
    "NUTANIX_ENDPOINT_API", "https://10.38.4.199:9440/PrismGateway/services/rest/v2.0/"
)
nutanix_user = get_required_environment(variable="NUTANIX_USER")
nutanix_password = get_required_environment(variable="NUTANIX_PASS")

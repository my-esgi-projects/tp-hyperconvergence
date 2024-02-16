"""
    Functions for preprocessing data before utilization
"""


def object_to_dict_converter(object):
    excluded_attributes = ["uri", "nutanix_api", "uuid"]
    return {key: value for key, value in object.__dict__.items() if value is not None and key not in excluded_attributes}

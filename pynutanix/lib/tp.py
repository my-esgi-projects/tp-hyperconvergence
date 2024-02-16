from pynutanix.lib.storage import Storage
from pynutanix.lib.vm import VM
from pynutanix.lib.network import Network
from pynutanix.lib.protection_domain import ProtectionDomain

def create_storage(prefix: str):
    storage = Storage(name=f"{prefix}-Storage", capacity=500000000000)
    storage_params = {"search_string": storage.name}
    storage_response = storage.create()
    storage_found = storage.list(params=storage_params)
    storage_uuid = storage_found["entities"][0]["storage_container_uuid"]

    return dict(
        object=storage, 
        params=storage_params, 
        response=storage_response,
        object_found=storage_found,
        object_uuid=storage_uuid
    )


def create_network(prefix: str):
    network = Network(
        name=f"{prefix}-Network",
        vlan_id=1,
        ip_config={"network_address": "10.0.6.0", "prefix_length": 24},
    )
    network_params = {"search_string": network.name}
    network_response = network.create()
    networks = network.list(params=network_params)
    network_found = dict()

    for net in networks.get("entities"):
        if net["name"] == network.name:
            network_found = net
            break

    return dict(
        object=network, 
        params=network_params, 
        response=network_response,
        object_found=network_found,
        object_uuid=network_found.get("uuid")
    )
  

def create_vm(prefix: str, suffix:str, ip:str):

    storage = create_storage(prefix=prefix)
    network = create_network(prefix=prefix)

    vm = VM(
        memory_mb=1024,
        num_vcpus=1,
        num_cores_per_vcpu=1,
        vm_disk_uid=storage.get("object_uuid"),
        name=f"{prefix}-{suffix}",
        image_disk_uid="934d5738-06fd-4ea2-a8f8-43ee5d9313b0",
        ip_address=ip,
        network_uid=network.get("object_uuid"),
        userdata="yum update -y && yum install -y nginx",
    )
    vm_response = vm.create()
    vms = vm.list()
    vm_found = {}

    for machine in vms.get("entities"):
        if machine["name"] == vm.name:
            vm_found = machine
            break

    return dict(
        object=vm, 
        response=vm_response,
        object_found=vm_found,
        object_uuid=vm_found.get("uuid")
    )


def create_protection_domain(prefix: str):
    protection_domain = ProtectionDomain(
        value=f"{prefix}-pd"
    )

    protection_domain_params = {"names": protection_domain.value}
    protection_domain_response = protection_domain.create()
    protection_domains = protection_domain.list(params=protection_domain_params)
    protection_domain_found = dict()

    for pd in protection_domains.get("entities"):
        if pd["name"] == protection_domain.name:
            protection_domain_found = pd
            break

    
    return dict(
        object=protection_domain, 
        params=protection_domain_params, 
        response=protection_domain_response,
        object_found=protection_domain_found,
    )

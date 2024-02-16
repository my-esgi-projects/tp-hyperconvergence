import click
from pynutanix.lib.storage import Storage
from pynutanix.lib.vm import VM
from pynutanix.lib.network import Network


@click.command()
def launch():
    prefix = "tp-esgi-SRC2-GRP6"
    storage = Storage(name=f"{prefix}-Storage", capacity=500000000000)
    storage_params = {"search_string": storage.name}
    storage_found = storage.list(params=storage_params)
    storage_uuid = storage_found['entities'][0]['storage_container_uuid']

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

    
    web_vm = VM(
            memory_mb=1024,
            num_vcpus=1,
            num_cores_per_vcpu=1,
            vm_disk_uid=storage_uuid,
            name=f"{prefix}-web",
            image_disk_uid="934d5738-06fd-4ea2-a8f8-43ee5d9313b0",
            ip_address="10.0.6.3",
            network_uid=network_found.get("uuid"),
            userdata="yum update -y && yum install -y nginx",
        )

    
    click.echo(f"response = {network_found}, {network_response}")

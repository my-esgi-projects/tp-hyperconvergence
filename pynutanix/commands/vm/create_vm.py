import click
from pynutanix.lib.vm import VM
from pynutanix.lib.storage import Storage
import json
from pynutanix.lib.network import Network
from pynutanix.lib.utils import object_to_dict_converter


@click.command()
@click.option("-r", "--requirements", default="auto", help="Name", type=str)
@click.option("-n", "--name", required=True, help="Name", type=str, prompt=True)
@click.option(
    "-m", "--memory-mb", required=True, help="Memory MB", type=int, prompt=True
)
@click.option(
    "-v", "--num-vcpus", required=True, help="Number of VCPUs", type=int, prompt=True
)
@click.option(
    "-c",
    "--num-cores-per-vcpu",
    required=True,
    help="Number of cores per VCPU",
    type=int,
    prompt=True,
)
@click.option("-d", "--vm-disk-uid", help="VM Disk UID", type=str)
@click.option(
    "-i",
    "--image-disk-uid",
    required=True,
    help="Image Disk UID",
    type=str,
    prompt=True,
)
@click.option("-net", "--network-uid", help="Network UID", type=str)
@click.option(
    "-ip", "--ip-address", required=True, help="IP Address", type=str, prompt=True
)
@click.option("-u", "--userdata", help="Userdata", type=str)
def create(
    requirements,
    name,
    memory_mb,
    num_vcpus,
    num_cores_per_vcpu,
    vm_disk_uid,
    image_disk_uid,
    network_uid,
    ip_address,
    userdata,
):
    if requirements == "auto":
        prefix = "SRC2-GROUP6"
        storage = Storage(name=f"{prefix}-Storage", capacity=500000000000)
        response_storage = storage.create()

        params = {"search_string": storage.name}
        storages = storage.list(params=params)
        network = Network(
            name=f"{prefix}-Network",
            vlan_id=1,
            ip_config='{"network_address": "10.0.6.0", "prefix_length": "24"}',
        )
        response_network = network.create()
        print(response_network, storages)
        vm = VM(
            name=name,
            memory_mb=memory_mb,
            num_vcpus=num_vcpus,
            num_cores_per_vcpu=num_cores_per_vcpu,
            vm_disk_uid=storages.get("entities")[0]["container_uuid"],
            image_disk_uid=image_disk_uid,
            network_uid=response_network["network_uuid"],
            ip_address=ip_address,
            userdata=userdata,
        )
        response = vm.create()

    click.echo(f"response = {response}")
    click.echo(f"Vm is created: {object_to_dict_converter(vm)}")

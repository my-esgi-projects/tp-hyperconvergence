import click
from pynutanix.commands.storage import create_storage, list_storages
from pynutanix.commands.network import create_network, list_networks
from pynutanix.commands.vm import create_vm, list_vms


@click.group()
def cli():
    pass


@cli.group()
def storage():
    pass


storage.add_command(create_storage.create)
storage.add_command(list_storages.list)


@cli.group()
def network():
    pass


network.add_command(create_network.create)
network.add_command(list_networks.list)


@cli.group()
def vm():
    pass

vm.add_command(create_vm.create)
vm.add_command(list_vms.list)


if __name__ == "__main__":
    cli()

import click
from pynutanix.lib.storage import Storage
from pynutanix.lib.vm import VM
from pynutanix.lib.network import Network


@click.command()
def launch():
    prefix = "tp-esgi-SRC2-GRP6"
    storage_params = f"{prefix}-Storage"
    storage = Storage(name=f"{prefix}-Storage", capacity=500000000000)

    storages = 

    click.echo(f"response = {response}")

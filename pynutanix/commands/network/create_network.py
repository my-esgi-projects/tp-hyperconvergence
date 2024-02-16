import click
import json
from pynutanix.lib.network import Network
from pynutanix.lib.utils import object_to_dict_converter


@click.command()
@click.option("-n", "--name", required=True, help="Network name", prompt=True)
@click.option(
    "-v",
    "--vlan_id",
    required=True,
    help="Vlan ID",
    type=int,
    prompt=True,
)
@click.option(
    "-i",
    "--ip_config",
    required=True,
    help="Network ip config(network_address, prefix_length)",
    prompt=True,
)
def create(name, vlan_id, ip_config):
    network = Network(name=name, vlan_id=vlan_id, ip_config=json.loads(ip_config))
    response = network.create()

    click.echo(f"response = {response}")
    click.echo(f"Network is created: {object_to_dict_converter(network)}")

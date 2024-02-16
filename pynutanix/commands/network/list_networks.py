import click
from pynutanix.lib.network import Network


@click.command()
def list():
    network = Network()
    response = network.list()

    click.echo(f"response = {response}")

import click
from pynutanix.lib.storage import Storage


@click.command()
def list():
    storage_container = Storage()
    response = storage_container.list()

    click.echo(f"response = {response}")

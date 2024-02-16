import click
from pynutanix.lib.storage import Storage


@click.command()
@click.option("-n", "--name", required=True, help="Storage container name", prompt=True)
@click.option(
    "-c",
    "--capacity",
    required=True,
    help="Storage container advertised capacity",
    type=int,
    prompt=True,
)
def create(name, capacity):
    storage_container = Storage(name=name, capacity=capacity)
    response = storage_container.create()

    click.echo(f"response = {response}")
    click.echo(f"storage container name's {name} with capacity {capacity} is created")

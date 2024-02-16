import click
from pynutanix.lib.tp import create_vm,create_protection_domain


@click.command()
@click.option("-p", "--prefix", default="tp-esgi-SRC2-GRP6", help="Name", type=str)
def launch(prefix):
    
    # Create VMs (It will create network and Storage)
    web_vm = create_vm(prefix=prefix, suffix="web", ip="10.0.6.3")
    db_vm = create_vm(prefix=prefix, suffix="db", ip="10.0.6.4")

    # Create protection domain
    protection_domain = create_protection_domain(prefix=prefix)
    click.echo(
        f"protection_domain={protection_domain[2]}"
    )

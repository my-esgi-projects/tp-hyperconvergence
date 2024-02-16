import click
from pynutanix.lib.tp import create_vm, manage_protection_domain


@click.command()
@click.option("-p", "--prefix", default="tp-esgi-SRC2-GRP6", help="Name", type=str)
def launch(prefix):
    
    # Create VMs (It will create network and Storage)
    web_vm = create_vm(prefix=prefix, suffix="web", network="10.0.136.0", ip="10.0.136.3", vlan_id=136)
    db_vm = create_vm(prefix=prefix, suffix="db", network="10.0.136.0", ip="10.0.136.4", vlan_id=136)

    # Create protection domain and add vms on it
    protection_domain = manage_protection_domain(prefix=prefix, vms=[f"{prefix}-web", f"{prefix}-db"])
    click.echo(
        f"web_vm_found = {web_vm}, db_vm={db_vm}, protection_domain={protection_domain}"
    )

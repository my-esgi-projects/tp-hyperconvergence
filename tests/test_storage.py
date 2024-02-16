from click.testing import CliRunner
from pynutanix.commands.storage.create_storage import create


def test_storage_create():
    runner = CliRunner()
    result = runner.invoke(create, ["--name", "toto", "--capacity", "4"])

    assert result.exit_code == 0
    assert (
        "storage container name's toto with capacity 4 is created"
        in result.output.strip()
    )


# def test_storage_update():
#     runner = CliRunner()

# setup.py
from setuptools import setup, find_packages


def requirements():
    with open("requirements.txt") as file:
        try:
            requirements = file.read().splitlines()
        except:
            raise Exception("Requirements file not parseable")
        return requirements


setup(
    name="pynutanix",
    version="1.0.0",
    packages=find_packages(),
    install_requires=requirements(),
    entry_points={
        "console_scripts": [
            "pynutanix = pynutanix.cli:cli",
        ],
    },
)

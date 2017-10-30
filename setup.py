import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    install_requires=required,
    name="sumo_traci",
    version="0.01",
    description="Redistribution of the SUMO TraCI source madules for use in the TrafficSenseMSD project",
    author="",
    packages=find_packages()
)

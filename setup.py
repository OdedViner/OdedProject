# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="oded-task",
    version="1.0",
    description="oded-package",
    author="Oded Viner",
    author_email="odedviner@gmail.com",
    license="MIT",
    install_requires=[
        "paramiko",
    ],
    entry_points={
        "console_scripts": [
            "local-disk=locally_disk:main",
            "ssh-setup=ssh_sessions:main"
        ],
    },
    zip_safe=True,
    include_package_data=True,
    packages=find_packages(exclude=["ez_setup"]),
)

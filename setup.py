#!/usr/bin/env python

from setuptools import setup, find_packages
from pip.req import parse_requirements

setup(
    name="elasticsearch-scripts",
    description="Set of scripts for administering Elasticsearch clusters.",
    version="1.0.0",
    packages=find_packages(),
    url="https://github.com/anchor/elasticsearch-scripts",
    maintainer="Sharif Olorin",
    maintainer_email="sio@tesser.org",
    author="Saj Goonatilleke",
    author_email="sg@redu.cx",
    scripts=[
        "es-allocator-disable",
        "es-allocator-enable",
        "es-am-i-master",
        "es-autoflush-disable",
        "es-autoflush-enable",
        "es-cluster-health",
        "es-cluster-settings",
        "es-cluster-state",
        "es-concurrent-rebalance",
        "es-flush",
        "es-index-delete",
        "es-index-locations",
        "es-index-settings",
        "es-index-size",
        "es-index-status",
        "es-list-indices",
        "es-move-shard",
        "es-node-info",
        "es-node-name-to-id",
        "es-node-settings",
        "es-node-shard-count",
        "es-node-stats",
        "es-nuke-all-indices",
        "es-write-disable",
        "es-write-enable",
    ],
    license="MIT",
    install_requires=[str(req.req) for req in
                          parse_requirements("requirements.txt")],
    include_package_data=True
)

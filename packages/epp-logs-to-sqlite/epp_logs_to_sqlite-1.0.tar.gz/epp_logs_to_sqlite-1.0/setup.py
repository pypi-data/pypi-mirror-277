# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='epp_logs_to_sqlite',
    version='1.0',
    description='Convert egg plant performance test results parser',
    packages=find_packages(),
    install_requires=[
        'epp_event_log_parser',
    ],
)

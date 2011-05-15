import os
import sys

from setuptools import setup, find_packages

setup(
    name='jobs.python.org',
    version='1.0dev',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires = [
        'deform',
        'mailinglogger',
        'mortar_rdb >= 1.1.0',
        'MySQL-python',
        'pyramid',
        'transaction',
        'WebError',
        # test dependencies, here because of Pyramid's scan
        'mock',
        'testfixtures',
        'WebTest',
        ],
    entry_points = """\
      [paste.app_factory]
      main = jobs:main

      [console_scripts]
      admin = jobs.admin:main
      """,
    )

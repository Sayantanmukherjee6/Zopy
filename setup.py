#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

version = '0.1.9'

setup(name='Zopy',
      version=version,
      description="Zoho API integration for Python",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='Zoho API Developers CRM',
      author='Dharwin Perez',
      author_email='dhararon@hotmail.com',
      url='https://github.com/dhararon/zopy',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['zopy'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'requests',
          'marshmallow'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

# -*- coding: utf-8 -*-
#!/usr/bin/env python

__author__ = 'ahnseonghyun'

from setuptools import setup, find_packages

version = '0.0.1'

setup(name='logliner',
      version=version,
      description="A module of downloading image from URL and resizing.",
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.6',
          'Topic :: Utilities',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='log timeline',
      author='AhnSeongHyun',
      author_email='sh84.ahn@gmail.com',
      url='https://github.com/AhnSeongHyun/logliner',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'attrdict',
          'pyyaml',
          'jinja2'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,

      )
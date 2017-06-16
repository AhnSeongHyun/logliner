# -*- coding: utf-8 -*-
#!/usr/bin/env python

__author__ = 'ahnseonghyun'


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from logliner import __version__


with open('README.md') as readme_file:
    readme = readme_file.read()


setup(name='logliner',
      version=__version__,
      description="find a keyword in multiple log files and merge according datetime",
      long_description=readme,
      author='AhnSeongHyun',
      author_email='sh84.ahn@gmail.com',
      url='https://github.com/AhnSeongHyun/logliner',
      packages=[
          'logliner',
      ],
      include_package_data=True,
      zip_safe=False,
      keywords='log timeline',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.6',
          'Topic :: Utilities',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      license='MIT',
      install_requires=[
          'attrdict',
          'PyYAML',
          'Jinja2'
      ],
      entry_points={
          'console_scripts': [
              'logliner=logliner.logliner:main',
          ],
      },

      )
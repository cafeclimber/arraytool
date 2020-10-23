# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(name='arraytool',
      version='0.0.0',
      description='Fork of arraytool from Zinka',
      long_description=readme,
      author='Bailey Campbell',
      author_email='baileycampbell1990@gmail.com',
      url='https://github.com/cafeclimber/arraytool',
      license=license,
      packages=find_packages(exclude=('tests', 'docs', 'misc')))

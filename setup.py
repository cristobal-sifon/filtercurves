from __future__ import absolute_import, print_function

from setuptools import setup

# download from https://github.com/cristobal-sifon/myhelpers
from myhelpers.setup_helpers import *


setup(
    name='filtercurves',
    version=find_version('filtercurves/__init__.py'),
    description='Tools for using instrument filter curves in python',
    long_description=read('README.md'),
    author='Cristobal Sifon',
    author_email='sifon@astro.princeton.edu',
    url='https://github.com/cristobal-sifon/filtercurves',
    packages=['filtercurves'],
    #package_data={'': 'data/*'},
    include_package_data=True,
    zip_safe=False
    )

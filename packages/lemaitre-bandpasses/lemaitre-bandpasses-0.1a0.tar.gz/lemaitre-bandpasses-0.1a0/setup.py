# setup.py file
#
from setuptools import setup, find_namespace_packages

setup(packages=find_namespace_packages(where='src/',
                                       include=['lemaitre.bandpasses']),
      package_dir={'': 'src'},
      include_package_data=True,
      package_data={'lemaitre.bandpasses': ['data/*.hdf5']}
      )

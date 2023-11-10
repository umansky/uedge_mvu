#!/usr/bin/env python
import setuptools


setuptools.setup(
    name='uedge_mvu',
    packages=setuptools.find_packages(),
    install_requires=['h5py', 'mppl', 'forthon', 'uedge', 'matplotlib', 
                      'numpy', 'scipy', 'pandas', 'shapely'],
    author='Maxim Umansky',
    author_email='umansky1@llnl.gov',
    url='https://github.com/umansky/uedge_mvu',
    description='UEDGE tools',
    long_description=open('README.md').read(),
)

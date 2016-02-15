#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Education :: Testing'
    ],
    name='catsim',
    version='0.8.1',
    description='Computerized Adaptive Testing Simulator',
    author='Douglas De Rizzo Meneghetti',
    author_email='douglasrizzom@gmail.com',
    url='https://douglasrizzo.github.io/catsim',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[
        'numpy', 'scipy', 'matplotlib', 'scikit-learn'
    ],
    license='GPLv2'
)

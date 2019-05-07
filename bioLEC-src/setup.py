from setuptools import setup, find_packages
from numpy.distutils.core import setup, Extension

import glob
import subprocess

if __name__ == "__main__":
    setup(name = 'bioLEC',
          author            = "Tristan Salles",
          author_email      = "tristan.salles@sydney.edu.au",
          url               = "https://github.com/Geodels/bioLEC",
          version           = "0.0.1",
          description       = "A Python interface to compute biodiversity metric based on landscape elevational connectivity.",
          long_description = open('README.md').read(),
          long_description_content_type = "text/markdown",
          packages          = ['bioLEC'],
          install_requires  = [
                        'numpy',
                        'scipy>=0.15.0',
                        'pandas',
                        'mpi4py',
                        'scikit-image'],
          python_requires   = '>=2.7, >=3.5',
          package_data      = {'bioLEC': ['Notebooks/*ipynb',
                                          'Notebooks/dataset/*',
                                          'Notebooks/images/*'] },
          include_package_data = True,
          classifiers       = ['Programming Language :: Python :: 2',
                               'Programming Language :: Python :: 2.6',
                               'Programming Language :: Python :: 2.7',
                               'Programming Language :: Python :: 3',
                               'Programming Language :: Python :: 3.3',
                               'Programming Language :: Python :: 3.4',
                               'Programming Language :: Python :: 3.5',
                               'Programming Language :: Python :: 3.6']
          )

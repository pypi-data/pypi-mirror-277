# setup.py file
#

from setuptools import setup, Extension

extensions = [
    Extension('bbf._libbbf',
              ['bbf/utils.c'],
              extra_compile_args=['-std=c11', '-O3', '-fopenmp'])]

setup(ext_modules=extensions)

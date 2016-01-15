from setuptools import setup
import re
import os
import io

def read(fname):
    return io.open(os.path.join(os.path.dirname(__file__), fname), encoding="UTF-8").read()

version = re.search('^__version__\s*=\s*"(.*)"',
                    open('breaking_point/__init__.py').read(), re.M).group(1)

setup(
    name='breaking-point',
    version=version,
    author='Yuri Shikanov',
    author_email='dizballanze@gmail.com',
    packages=['breaking_point'],
    # scripts=[],
    url='https://github.com/dizballanze/breaking-point',
    license='MIT',
    description='breaking-point.py helps to find a size of input data where one function starts outperform another function. It is a convenient way to compare different algorithms for a single task.',
    long_description=read('README.rst'),
    install_requires=[],
    data_files=[('', ['LICENSE', 'README.rst'])]
)

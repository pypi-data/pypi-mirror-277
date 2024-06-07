from setuptools import setup, find_packages
from setuptools.extension import Extension

setup(
    name='fftwb',
    version='0.1.1',
    author='Formula Finance',
    author_email='',
    description='The bindings for the C++ backtesting engine.',
    long_description=open('README.md').read(),
    packages=find_packages(),
    package_data={
        'fftwb': ['twb.cpython-311-x86_64-linux-gnu.so'],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)

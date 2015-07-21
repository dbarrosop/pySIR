import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='pySIR',
    version='0.3',
    packages=['pySIR'],
    include_package_data=True,
    license='Apache version 2.0',  # example license
    description='Python API to interact with the SIR agent',
    long_description=README,
    url='https://github.com/dbarrosop/pySIR',
    author='David Barroso',
    author_email='dbarrosop@dravetech.com',
    classifiers=[
        'Topic :: System :: Networking',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
)

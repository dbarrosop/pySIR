import uuid
from setuptools import setup
from pip.req import parse_requirements

version = '0.41'

install_reqs = parse_requirements('requirements.txt', session=uuid.uuid1())
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='pySIR',
    version=version,
    packages=['pySIR'],
    include_package_data=True,
    license='Apache version 2.0',  # example license
    description='Python API to interact with the SIR agent',
    long_description=open('README.md').read(),
    url='https://github.com/dbarrosop/pySIR',
    author='David Barroso',
    author_email='dbarrosop@dravetech.com',
    install_requires=reqs,
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

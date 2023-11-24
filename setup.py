from setuptools import setup

setup(
    name='apiarmor',
    version='0.1.0',
    packages=['secureapi'],
    install_requires=[
        'Flask',
        'cryptography',
    ],
)

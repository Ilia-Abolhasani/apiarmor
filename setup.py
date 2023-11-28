from setuptools import setup

setup(
    name="apiarmor",
    version="0.1.0",
    packages=["apiarmor", "apiarmor.server", "apiarmor.client"],
    install_requires=[
        "cryptography",
    ],
    extras_require={
        "server": ["Flask"],
    },
)

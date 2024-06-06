from setuptools import setup, find_packages

setup(
    name="rixolky",
    version="0.1",
    description="A package",
    author="Rixolky",
    author_email="rixolky@gmail.com",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "start=command.main:start"
        ]
    },
)
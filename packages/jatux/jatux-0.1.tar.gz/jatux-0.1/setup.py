from setuptools import setup, find_packages

setup(
    name="jatux",
    version="0.1",
    description="A simple Python package",
    author="Jatux",
    author_email="jatux@proton.me",
    packages=find_packages(),
    install_requires=[],
    entry_points={"console_scripts": ["hello=command.main:hi"]},
)
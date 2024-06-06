from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="jsonmorph",
    version="0.0.6",
    author="Bidut Karki",
    author_email="bidutjava3@gmail.com",
    description="Tool for transforming a JSON to another JSON by defining a configuration JSON setting file.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['wheel'],
    setup_requires=['wheel'],
)

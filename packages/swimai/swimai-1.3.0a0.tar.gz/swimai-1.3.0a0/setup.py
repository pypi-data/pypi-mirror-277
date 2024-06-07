from setuptools import setup
import os

VERSION = "1.3.0-alpha"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="swimai",
    description="swimai is now swimos",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    version=VERSION,
    install_requires=["swimos"],
    classifiers=["Development Status :: 7 - Inactive"],
)

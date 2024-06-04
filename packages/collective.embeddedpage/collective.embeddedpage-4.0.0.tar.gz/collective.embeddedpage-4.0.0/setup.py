"""Installer for the collective.embeddedpage package."""

from setuptools import find_packages
from setuptools import setup

import sys


assert sys.version_info >= (
    3,
    7,
    0,
), "collective.embeddedpage 3.x.x requires Python 3.7.0+. Please downgrade to collective.embeddedpage 2.x.x for Python 2 and Plone 4.3/5.1."

long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CONTRIBUTORS.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="collective.embeddedpage",
    version="4.0.0",
    description="Add-on to embed remote HTML pages into the Plone CMS",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone",
    author="kitconcept GmbH",
    author_email="info@kitconcept.com",
    url="https://pypi.python.org/pypi/collective.embeddedpage",
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["collective"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.7",
    install_requires=[
        "chardet",
        "lxml",
        "plone.api",
        "plone.app.contenttypes",
        "plone.app.dexterity",
        "plone.app.lockingbehavior",
        "plone.app.relationfield",
        "plone.app.versioningbehavior",
        "plone.restapi",
        "Products.GenericSetup>=1.8.2",
        "requests",
        "setuptools",
        "z3c.jbot",
    ],
    extras_require={
        "test": [
            "cssselect",
            "httmock",
            "robotframework",
            "plone.app.testing",
            "plone.testing",
            "plone.app.contenttypes",
            "plone.app.robotframework[debug]",
            "zest.releaser[recommended]",
            "towncrier",
            "zestreleaser.towncrier",
            "wheel",
            "black",
            "isort",
            "flake8",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)

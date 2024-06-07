#! -*- coding: utf8 -*-

from setuptools import find_packages
from setuptools import setup


version = "1.3.1"

long_description = (
    open("README.rst").read() + "\n" + "Contributors\n"
    "============\n" + "\n" + open("CONTRIBUTORS.rst").read() + "\n" + open("CHANGES.rst").read() + "\n"
)

setup(
    name="collective.dms.batchimport",
    version=version,
    description="Batch import of files into the Documents Management System",
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Zope Plone",
    author="Cedric Messiant",
    author_email="dev@imio.be",
    project_urls={
        "PyPI": "https://pypi.python.org/project/collective.dms.batchimport",
        "Source": "https://github.com/collective/collective.dms.batchimport",
    },
    license="gpl",
    packages=find_packages("src"),
    package_dir={"": "src"},
    namespace_packages=["collective", "collective.dms"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        "collective.dms.basecontent",
        "collective.dms.mailcontent",
        "collective.z3cform.datagridfield",
        "imio.helpers",
        "imio.pyutils",
        "natsort",
        "five.grok",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            "ecreall.helpers.testing",
        ],
    },
    entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      [console_scripts]
      batchimport_add_metadata = collective.dms.batchimport.script:add_metadata
      """,
)

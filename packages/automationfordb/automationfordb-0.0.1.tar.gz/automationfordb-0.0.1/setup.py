from setuptools import setup, find_packages
from typing import List


with open("README.md", "r", encoding="utf-8") as f:
    long_desc = f.read()

__version__ = "0.0.1"
REPO_NAME = "mongodbconnectorpkg"
PKG_NAME = "automationfordb"
AUTHOR_USER_NAME = "mortalbeingg"
AUTHOR_EMAIL = "newmortalbeing333@gmail.com"


setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with a database",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)

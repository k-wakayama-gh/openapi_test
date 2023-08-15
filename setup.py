"""Python setup.py for openapi_test package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("openapi_test", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="openapi_test",
    version=read("openapi_test", "VERSION"),
    description="Awesome openapi_test created by k-wakayama-gh",
    url="https://github.com/k-wakayama-gh/openapi_test/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="k-wakayama-gh",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["openapi_test = openapi_test.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)

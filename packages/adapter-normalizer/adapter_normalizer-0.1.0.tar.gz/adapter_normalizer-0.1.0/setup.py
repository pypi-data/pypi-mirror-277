from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="adapter_normalizer",  # package name
    version="0.1.0",  # version
    author="Lev Belous",
    author_email="leva22.08.01@inbox.ru",
    description="adapter for db",  # short description
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url='https://github.com/lev4ek0/',  # package URL
    install_requires=[
        "sqlalchemy",
        "asyncpg",
        "greenlet",
    ],  # list of packages this package depends
    # on.
    packages=find_packages(),  # List of module names that installing
    # this package will provide.
    python_requires=">=3.9",
)

"""The setup script."""

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["Click>=7.0"]

setup_requirements = []

test_requirements = []

setup(
    author="FreightTrust and Clearing Corporation",
    author_email="admin@freighttrust.com",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Global Container Freight Index Pricing based on Drewry.co.uk Pricing Information",
    entry_points={
        "console_scripts": ["drewry_container_index=drewry_container_index.cli:main"]
    },
    install_requires=requirements,
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="drewry_container_index",
    name="drewry_container_index",
    packages=find_packages(
        include=["drewry_container_index", "drewry_container_index.*"]
    ),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/@freight-trust/drewry_container_index",
    version="0.1.0",
    zip_safe=False,
)

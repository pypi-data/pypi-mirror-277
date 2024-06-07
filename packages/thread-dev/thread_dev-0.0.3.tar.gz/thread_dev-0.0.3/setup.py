from setuptools import setup, find_packages

with open("../README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="thread-dev",
    version="0.0.3",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "jupyter-server>=2.0",
        "jupyter",
    ],
    entry_points={
        "console_scripts": [
            "jupyter-thread = thread:launch_instance",
            "thread = thread:launch_instance",
        ]
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
)

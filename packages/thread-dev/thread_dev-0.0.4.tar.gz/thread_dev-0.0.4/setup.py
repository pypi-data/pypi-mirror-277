from setuptools import setup, find_packages

# Read the content of README.md
with open("../README.md", "r") as fh:
    long_description = fh.read()

# Replace all mentions of 'public/' with 'thread/static/'
long_description = long_description.replace('public/', 'thread/static/')

setup(
    name="thread-dev",
    version="0.0.4",
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

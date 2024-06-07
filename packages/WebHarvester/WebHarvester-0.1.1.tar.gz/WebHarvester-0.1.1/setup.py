
from setuptools import setup, find_packages

import WebHarvester

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="WebHarvester",
    version=WebHarvester.__version__,
    author="ulala",
    author_email="2713389652@qq.com",
    description="A simple super fast asynchronous crawler framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/uraurara/web-harvester",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    install_requires=requirements,
)

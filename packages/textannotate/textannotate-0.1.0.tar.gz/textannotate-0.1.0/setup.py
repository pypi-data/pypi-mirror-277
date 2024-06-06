import re

import setuptools
from setuptools import find_packages

with open("./textannotate/__init__.py", "r") as f:
    content = f.read()
    # from https://www.py4u.net/discuss/139845
    version = re.search(r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]', content).group(1)

with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="textannotate",
    version=version,
    author="capjamesg",
    author_email="readers@jamesg.blog",
    description="A text classification annotation and review tool developed in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/capjamesg/textannotate",
    install_requires=[
        "flask",
        "click"
    ],
    include_package_data=True,
    package_data={"": ["templates/*"]},
    packages=find_packages(exclude=("tests",)),
    entry_points={
        "console_scripts": [
            "textannotate = textannotate.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
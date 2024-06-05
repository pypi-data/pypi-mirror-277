from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Sets up a basic CLI App to take inputs to move a file from one location to another.'
LONG_DESCRIPTION = 'A package that sets up a basic CLI App to take user inputs to move files between directories.'

# Setting up
setup(
    name="RelocateFile",
    version=VERSION,
    author="kunaalg",
    author_email="<kunaal@runcode.in>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    include_package_data=False,
    data_files=[
        ('src/FileMover.py', ['src/FileMover.py']),
        ],
    packages=find_packages(),
    scripts=[],
    install_requires=['datetime', 'pandas', 'requests', 'numpy', 'flask', 'virtualenv'],
    keywords=['python', 'Flask', 'App', 'Javascript', 'Function', 'math'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
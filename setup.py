import os
import codecs
from setuptools import setup, find_packages
from pkg_resources import parse_requirements

# Get the absolute path of the current directory
here = os.path.abspath(os.path.dirname(__file__))

# Parse requirements.txt, ignoring comments and empty lines
with open('requirements.txt', 'r') as req_file:
    requirements = [str(req) for req in parse_requirements(req_file) if req and not req.url]

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


# Setting up
setup(
    name='bangla_dictionary',
    version='0.0.1',
    author="Biplab Kumar Sarkar, Afrar Jahin, Asif Shusmit",
    author_email="bip.sec22@gmail.com, afarjahin@gmail.com",
    description="A Complete Bangla Dictionary PyPI Module.",
    long_description_content_type="text/markdown",
    long_description=long_description,
    package_dir={"": "bangla_dictionary"},
    packages=find_packages(where="bangla_dictionary"),
    url="https://github.com/bipsec/bangla-dictionary",
    license="MIT",
    install_requires=requirements,
    keywords=['python', 'online dictionary', 'bangla dictionary', 'bengali dictionary', 'bangla_dict', 'corpus dictionary', 'bangla corpus'],
    classifiers=[
        "Development Status :: Corpus Building",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.3'
DESCRIPTION = 'A vinted api wrapper in python.'
LONG_DESCRIPTION = 'A package that allows you to interact with the vinted api.'

# Setting up
setup(
    name="pythed",
    version=VERSION,
    author="Archithebald",
    author_email="<archithebald@proton.me>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests', 'selenium'],
    keywords=['python', 'vinted', 'pypi', 'api', 'wrapper'],
)

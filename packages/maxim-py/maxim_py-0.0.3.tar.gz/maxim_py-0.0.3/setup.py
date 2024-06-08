from setuptools import setup, find_packages
import codecs
import os
import codecs
import os

from setuptools import find_packages, setup
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()
print(os.path.join(here, "README.md"))
VERSION = '0.0.3'
DESCRIPTION = 'Maxim Python Library'
LONG_DESCRIPTION = 'A package that allows you to use the Maxim Python Library to interact with the Maxim Platform'

packages = find_packages()
packages.remove('maxim-sdk.tests')
print(packages)
# Setting up
setup(
    name="maxim_py",
    version=VERSION,
    author="Maxim",
    author_email="<aniruddha@getmaxim.ai>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=packages,
    install_requires=[],
    keywords=['python', 'prompts','logs','workflow','testing'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
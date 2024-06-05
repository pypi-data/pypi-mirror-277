from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.7'
DESCRIPTION = 'Sets up a basic Flask App with Javascipt Functionality'
LONG_DESCRIPTION = 'A package that sets up a basic Flask App Boilerplate with Javascript Functionality.'

# Setting up
setup(
    name="Flask_App_Multi",
    version=VERSION,
    author="kunaalg",
    author_email="<kunaalgadhalay93@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    include_package_data=True,
    data_files=[
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
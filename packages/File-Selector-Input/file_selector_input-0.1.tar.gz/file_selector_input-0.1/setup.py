from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1'
DESCRIPTION = 'Sets up a basic application to move file locations'
LONG_DESCRIPTION = 'A package that sets up a basic App to move file locations.'

# Setting up
setup(
    name="File_Selector_Input",
    version=VERSION,
    author="kunaalg",
    author_email="<kunaal@runcode.in>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    include_package_data=False,
    packages=find_packages(),
    scripts=[],
    install_requires=['datetime', 'pandas', 'requests', 'numpy', 'flask', 'virtualenv'],
    keywords=['python', 'FileSelector', 'App', 'Move', 'Function', 'math'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
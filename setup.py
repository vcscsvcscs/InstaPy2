# This Python file uses the following encoding: utf-8

from setuptools import setup
from os import path

# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import and use built-in open()
from io import open as io_open
import re


summary = "Automation script for Instagram that farms comments, follows and likes."
project_homepage = "https://github.com/official-antique/InstaPy2"
here = path.abspath(path.dirname(__file__))


def readall(*args):
    with io_open(path.join(here, *args), encoding="utf-8") as fp:
        return fp.read()


with open("requirements.txt") as f:
    dependencies = f.read().splitlines()

documentation = readall("README.md")
metadata = dict(
    re.findall(r"""__([a-z]+)__ = "([^"]+)""", readall("instapy2", "__init__.py"))
)

setup(
    name="instapy2",
    version=metadata["version"],
    description=summary,
    long_description=documentation,
    long_description_content_type="text/markdown",
    author="Antique",
    author_email="official.antique@gmail.com",
    maintainer="Antique",
    license="GPLv3",
    url=project_homepage,
    download_url=(project_homepage + "/archive/main.zip"),
    project_urls={
        "Bug Reports": (project_homepage + "/issues")
    },
    packages=["instapy2"],
    # include_package_data=True,  # <- packs every data file in the package
    package_data={  # we need only the files below:
        "instapy2": [
            "icons/Windows/*.ico",
            "icons/Linux/*.png",
            "icons/Mac/*.icns",
            "firefox_extension/*",
            "plugins/*",
        ]
    },
    keywords=(
        "instapy2 python instagram automation \
         marketing promotion bot selenium"
    ),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Win32 (MS Windows)",
        "Environment :: MacOS X",
        "Environment :: Web Environment",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: JavaScript",
        "Programming Language :: SQL",
        "Topic :: Utilities",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3.10",
        "Natural Language :: English",
    ],
    install_requires=dependencies,
    extras_require={"test": ["tox", "virtualenv", "tox-venv"]},
    python_requires=">=3.10",
    platforms=["win32", "linux", "linux2", "darwin"],
    zip_safe=False,
    entry_points={"console_scripts": []},
)

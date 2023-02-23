from setuptools import setup
import pypkg
import sys

DESCRIPTION = "pypkg: Python pyproject.toml Genelator"
NAME = 'pypkg'
AUTHOR = 'sonyakun'
AUTHOR_EMAIL = 'sonyakun217@gmail.com'
URL = 'https://github.com/sonyakun/pyinit'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/sonyakun/pyinit/releases'
VERSION = "1.0.0"
PYTHON_REQUIRES = ">=3.9"

INSTALL_REQUIRES = [
    'toml',
    'cleo',
]

CLASSIFIERS = [
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3 :: Only',
]

with open('README.md', 'r') as fp:
    readme = fp.read()
long_description = readme

setup(
    name=NAME,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=AUTHOR,
      maintainer_email=AUTHOR_EMAIL,
      description=DESCRIPTION,
      long_description=long_description,
      license=LICENSE,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      python_requires=PYTHON_REQUIRES,
      install_requires=INSTALL_REQUIRES,
      classifiers=CLASSIFIERS,
    entry_points={
        "console_scripts": [
            "pypkg=pypkg.cli.main:main".format(sys.version_info[0]),
        ]
    },
)
"""
URL filter and manipulation tools
http://github.com/adbar/courlan
"""

import re

from pathlib import Path
from setuptools import setup



def get_version(package):
    "Return package version as listed in `__version__` in `init.py`"
    # version = Path(package, '__init__.py').read_text() # Python >= 3.5
    with open(str(Path(package, '__init__.py')), 'r', encoding='utf-8') as filehandle:
        initfile = filehandle.read()
    return re.search('__version__ = [\'"]([^\'"]+)[\'"]', initfile).group(1)


def get_long_description():
    "Return the README"
    with open('README.rst', 'r', encoding='utf-8') as filehandle:
        long_description = filehandle.read()
    #long_description += "\n\n"
    #with open("CHANGELOG.md", encoding="utf8") as f:
    #    long_description += f.read()
    return long_description


setup(
    name='courlan',
    version=get_version('courlan'),
    description='Clean, filter, normalize, and sample URLs',
    long_description=get_long_description(),
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        #'Development Status :: 4 - Beta',
        #'Development Status :: 5 - Production/Stable',
        #'Development Status :: 6 - Mature',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing :: Filters',
    ],
    keywords=['urls', 'url-parsing', 'url-manipulation', 'preprocessing', 'validation', 'webcrawling'],
    url='http://github.com/adbar/courlan',
    author='Adrien Barbaresi',
    author_email='barbaresi@bbaw.de',
    license='GPLv3+',
    packages=['courlan'],
    project_urls={
        "Source": "https://github.com/adbar/courlan",
        "Coverage": "https://codecov.io/github/adbar/courlan",
        "Tracker": "https://github.com/adbar/courlan/issues",
    },
    #package_data={},
    include_package_data=True,
    python_requires='>=3.4',
    install_requires=[
        'requests',
        'tldextract',
    ],
    #extras_require=extras,
    entry_points = {
        'console_scripts': ['courlan=courlan.cli:main'],
    },
    # platforms='any',
    tests_require=['pytest', 'tox'],
    zip_safe=False,
)

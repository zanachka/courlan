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
    description='Clean, filter and sample URLs to optimize data collection. Includes spam, content type and language filters.',
    long_description=get_long_description(),
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
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
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
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
        "Tracker": "https://github.com/adbar/courlan/issues",
        "Blog": "https://adrien.barbaresi.eu/blog/",  # /tag/courlan.html
    },
    #package_data={},
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=[
        'langcodes>=3.2.1',
        'tld>=0.12',
        'urllib3>=1.26,<2',
    ],
    #extras_require=extras,
    entry_points = {
        'console_scripts': ['courlan=courlan.cli:main'],
    },
    # platforms='any',
    tests_require=['pytest'],
    zip_safe=False,
)

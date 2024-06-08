#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'PySide6',
    'tscat==0.4.*',
]

test_requirements = ['pytest>=3', ]

setup(
    author="Patrick Boettcher",
    author_email='p@yai.se',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    description="Time-series catalogue - graphical user interface library",
    entry_points={
        'console_scripts': [
            'tscat_gui=tscat_gui.app:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='tscat_gui',
    name='tscat_gui',
    packages=find_packages(include=['tscat_gui', 'tscat_gui.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/SciQLop/tscat_gui',
    version='0.4.0',
    zip_safe=False
)

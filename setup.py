#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='mastering_python',
    version='0.0.1',
    description="Exercises and examples based mainly on Pack Publishing books and videos + other interesting sources about python development.",
    long_description=readme + '\n\n' + history,
    author="Baeza Olvera Daniel Jesus",
    author_email='daniil_iisus@icloud.com',
    url='https://github.com/dbaeza0/mastering_python',
    packages=[
        'mastering_python',
    ],
    package_dir={'mastering_python':
                 'mastering_python'},
    entry_points={
        'console_scripts': [
            'mastering_python=mastering_python.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='mastering_python',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)

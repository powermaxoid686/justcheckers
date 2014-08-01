#!/usr/bin/env python
# coding=utf-8
import re

from setuptools import setup, find_packages


def gather_requirements(filename='requirements.txt'):
    """
    Gather the requirements from a requirements file.

    :param filename: The name of the file.
    """
    with open(filename) as req_file:
        raw_requirements = req_file.readlines()

    return [requirement.strip()
            for requirement in raw_requirements
            if requirement.strip() and not re.match('#|-(?!e)', requirement)]


setup(
    name='justcheckers',
    version='0.5.0',
    url='http://justcheckers.org/',
    license='GPL v3',
    author='Dorian Pula',
    author_email='dorian.pula@gmail.com',
    description='An advanced cross-platform checkers game.',

    install_requires=gather_requirements(),
    extras_requires={
        'web': gather_requirements('requirements/web.txt'),
    },

    packages=find_packages(exclude=['test']),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'justcheckers = justcheckers.app:main',
        ]
    },

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment:: MacOS',
        'Environment :: Web Environment',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience:: End Users / Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Games/Entertainment',
        'Topic :: Games/Entertainment :: Board Games',
    ],
)


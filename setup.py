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
    packages=['justcheckers'],
    url='http://justcheckers.org/',
    license='Affero GPL v3',
    author='Dorian Pula',
    author_email='dorian.pula@gmail.com',
    description='An advanced cross-platform checkers game.',

    install_requires=gather_requirements(),
    extras_requires={
        'web': gather_requirements('requirements/web.txt'),
    },

    packages=find_packages('justcheckers'),
    include_package_data=True,
)

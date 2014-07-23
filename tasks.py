import os
from os import path

from invoke import task, run


@task
def docs():
    """Build Sphinx documentation."""
    build_dir = '_build'
    if not path.exists(build_dir):
        os.mkdir(build_dir)
    run('sphinx-build -b slides . _build')


@task
def clean():
    """Clean generated files."""
    run('rm *.pyc')
    run('rm _build -rv')


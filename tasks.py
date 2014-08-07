import os
from os import path
import shutil

from invoke import task, run


@task
def clean():
    """Clean generated files."""
    run('rm *.pyc')


@task
def docs():
    """Creates the HTML documentation through Sphinx."""
    build_dirs = ['docs/_api', 'docs/_build']
    for build_dir in build_dirs:
        if not path.exists(build_dir):
            os.mkdir(build_dir)
    run('sphinx-apidoc -o docs/_api rookeries')
    run('sphinx-build -b html docs docs/_build')


@task
def clean_docs():
    """Clean up the generated Sphinx documentation."""
    sphinx_api_docs_dir = os.path.join(os.curdir, 'docs', '_api')
    if os.path.exists(sphinx_api_docs_dir):
        shutil.rmtree(sphinx_api_docs_dir)

    sphinx_build_docs_dir = os.path.join(os.curdir, 'docs', '_build')
    if os.path.exists(sphinx_build_docs_dir):
        shutil.rmtree(sphinx_build_docs_dir)


@task
def test_style():
    """Test the coding style using Flake8."""
    run('flake8')


@task
def test():
    """Test the webapp using both unit and integration nose tests."""
    run('nosetests  --with-coverage --cover-html --cover-package=justcheckers --cover-inclusive --cover-branches')


@task
def clean_tests():
    """Cleans test reports and artifacts."""
    coverage_report_dir = os.path.join(os.curdir, 'cover')
    if os.path.exists(coverage_report_dir):
        shutil.rmtree(coverage_report_dir)


@task
def build_package():
    """Prepares the project for packaging."""
    run('python setup.py sdist')


@task
def clean_package():
    """Cleans up generated files after packaging the project."""
    packaging_dirs = [os.path.join(os.curdir, packaging) for packaging in ['justcheckers.egg-info', 'dist']]
    for packaging in packaging_dirs:
        if os.path.exists(packaging):
            print("Removing '{}'".format(packaging))
            shutil.rmtree(packaging)

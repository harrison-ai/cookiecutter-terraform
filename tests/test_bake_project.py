"""
A modified version of https://github.com/audreyfeldroy/cookiecutter-pypackage/blob/master/tests/test_bake_project.py
"""

import datetime
import importlib
import os
import shlex
import subprocess
import sys
from contextlib import contextmanager

import yaml
from click.testing import CliRunner
from cookiecutter.utils import rmtree


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def check_output_inside_dir(command, dirpath):
    "Run a command from inside a given directory, returning the command output"
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))


def project_info(result):
    """Get toplevel dir, project_slug, and project dir from baked cookies"""
    project_path = str(result.project)
    project_slug = os.path.split(project_path)[-1]
    project_dir = os.path.join(project_path, project_slug)
    return project_path, project_slug, project_dir


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert 'docker-compose.yml' in found_toplevel_files
        assert 'envvars.yml' in found_toplevel_files
        assert 'Makefile' in found_toplevel_files
        assert 'LICENSE' not in found_toplevel_files

        # Check the contents of dirs
        common_files = [f for f in os.listdir(result.project.listdir('tf')[0])]
        assert 'provider.tf' in common_files
        assert 'data.tf' in common_files
        assert 'main.tf' in common_files
        assert 'dev' in common_files
        assert 'prod' in common_files


def test_locals_tf_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        tf_dir = os.path.join(result.project.dirpath(),
                              'terraform-cookiecutter', 'tf')

        with open(os.path.join(tf_dir, 'dev', 'locals.tf'), 'r') as _f:
            tf_locals_dev = _f.read()

        with open('./tests/locals_dev.tf', 'r') as _f:
            tf_locals_expected = _f.read()

        assert tf_locals_dev == tf_locals_expected

        with open(os.path.join(tf_dir, 'prod', 'locals.tf'), 'r') as _f:
            tf_locals_prod = _f.read()

        with open('./tests/locals_prod.tf', 'r') as _f:
            tf_locals_expected = _f.read()

        assert tf_locals_prod == tf_locals_expected

        # Check for symlinks
        for env, name in zip(['dev', 'prod'],
                             ['main.tf', 'data.tf', 'provider.tf']):
            filepath = os.path.join(tf_dir, env, name)
            assert os.path.islink(filepath)

            # Open the link file
            with open(filepath, 'r') as _f:
                link = _f.read()

            # Open the src file
            with open(os.path.join(tf_dir, name), 'r') as _f:
                src = _f.read()

            assert link == src


def test_backend_tf_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        tf_dir = os.path.join(result.project.dirpath(),
                              'terraform-cookiecutter', 'tf')

        with open(os.path.join(tf_dir, 'dev', 'backend.tf'), 'r') as _f:
            tf_backend_dev = _f.read()

        with open('./tests/backend_dev.tf', 'r') as _f:
            tf_backend_expected = _f.read()

        assert tf_backend_dev == tf_backend_expected

        with open(os.path.join(tf_dir, 'prod', 'backend.tf'), 'r') as _f:
            tf_backend_prod = _f.read()

        with open('./tests/backend_prod.tf', 'r') as _f:
            tf_backend_expected = _f.read()

        assert tf_backend_prod == tf_backend_expected


def test_bake_without_author_file(cookies):
    with bake_in_temp_dir(cookies, extra_context={'create_author_file':
                                                  'n'}) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert 'AUTHORS.md' not in found_toplevel_files


def test_bake_selecting_license(cookies):
    license_strings = {
        'MIT license': 'MIT ',
        'BSD license': 'Redistributions of source code must retain the ' +
        'above copyright notice, this',
        'ISC license': 'ISC License',
        'Apache Software License 2.0':
        'Licensed under the Apache License, Version 2.0',
        'GNU General Public License v3': 'GNU GENERAL PUBLIC LICENSE',
    }
    for license, target_string in license_strings.items():
        with bake_in_temp_dir(cookies,
                              extra_context={'open_source_license':
                                             license}) as result:
            assert target_string in result.project.join('LICENSE').read()


def test_bake_not_open_source(cookies):
    with bake_in_temp_dir(
            cookies, extra_context={'open_source_license':
                                    'Not open source'}) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        # assert 'setup.py' in found_toplevel_files
        assert 'LICENSE' not in found_toplevel_files
        assert 'License' not in result.project.join('README.md').read()


# def test_project_with_hyphen_in_module_name(cookies):
#     result = cookies.bake(
#         extra_context={'project_name': 'something-with-a-dash'}
#     )
#     assert result.project is not None
#     project_path = str(result.project)
#
#     # when:
#     travis_setup_cmd = ('python travis_pypi_setup.py'
#                         ' --repo audreyr/cookiecutter-pypackage'
#                         ' --password invalidpass')
#     run_inside_dir(travis_setup_cmd, project_path)
#
#     # then:
#     result_travis_config = yaml.load(
#         open(os.path.join(project_path, ".travis.yml"))
#     )
#     assert "secure" in result_travis_config["deploy"]["password"],\
#         "missing password config in .travis.yml"

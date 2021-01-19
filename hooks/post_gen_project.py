#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def create_symlink(basename):
    target = 'tf'
    dev = os.path.join('tf', 'dev')
    prod = os.path.join('tf', 'prod')
    os.symlink(os.path.join(os.path.relpath(target, dev), basename),
               os.path.join(dev, basename))
    os.symlink(os.path.join(os.path.relpath(target, prod), basename),
               os.path.join(prod, basename))


if __name__ == '__main__':

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')
        remove_file('AUTHORS.md')
        remove_file('CONTRIBUTING.md')

    for name in ['data.tf', 'main.tf', 'provider.tf']:
        create_symlink(name)

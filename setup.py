#!/usr/bin/env python
"""The setup script."""

from setuptools import find_packages, setup

import versioneer

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.md') as history_file:
    history = history_file.read()

requirements = []

setup_requirements = [
    'pytest-runner',
]

test_requirements = [
    'pytest>=3',
]

setup(
    author="Ben Johnston",
    author_email='ben.johnston@harrison.ai',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Harrison.ai Terraform Cookiecutter Template",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='cookiecutter_terraform',
    name='cookiecutter_terraform',
    packages=find_packages(
        include=['cookiecutter_terraform', 'cookiecutter_terraform.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/harrison-ai/cookiecutter-terraform',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    zip_safe=False,
)

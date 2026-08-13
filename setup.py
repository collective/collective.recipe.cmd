"""
This module contains the tool of collective.recipe.cmd
"""
from pathlib import Path

from setuptools import setup


version = '1.0.1.dev0'

long_description = '\n\n'.join(
    Path(filename).read_text(encoding='utf-8')
    for filename in ('README.rst', 'CONTRIBUTORS.rst', 'CHANGES.rst')
)

entry_point = 'collective.recipe.cmd'
entry_points = {
    'zc.buildout': [
        f'default = {entry_point}:Cmd',
        f'sh = {entry_point}:Cmd',
        f'py = {entry_point}:Python',
    ],
    'zc.buildout.uninstall': [
        f'default = {entry_point}:uninstallCmd',
        f'sh = {entry_point}:uninstallCmd',
    ],
}

setup(
    name='collective.recipe.cmd',
    version=version,
    description='Buildout recipe to execute shell commands.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    # Get more from https://pypi.org/classifiers
    classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.10',
    keywords='buildout recipe',
    author='Gael Pasgrimaud',
    author_email='gael@gawel.org',
    url='https://github.com/collective/collective.recipe.cmd',
    license='BSD',
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'zc.buildout',
    ],
    extras_require={
        'test': [
            'zope.testing',
            'zope.testrunner',
            'zc.buildout',
            'manuel'
        ]
    },
    entry_points=entry_points,
)

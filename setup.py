"""
This module contains the tool of collective.recipe.cmd
"""
from pathlib import Path

from setuptools import setup


version = '1.0.0.dev0'
description = 'Buildout recipe to execute shell commands.'
long_description = '\n'.join(
    Path(f).read_text(encoding='utf-8')
    for f in ('README.rst', 'CONTRIBUTORS.rst', 'CHANGES.rst')
)

entry_point = 'collective.recipe.cmd'
entry_points = {"zc.buildout": [
    "default = %s:Cmd" % entry_point,
    "sh = %s:Cmd" % entry_point,
    "py = %s:Python" % entry_point,
],
    "zc.buildout.uninstall": [
    "default = %s:uninstallCmd" % entry_point,
    "sh = %s:uninstallCmd" % entry_point,
],
}

tests_require = ['zope.testing', 'zope.testrunner', 'zc.buildout', 'manuel']

setup(
    name='collective.recipe.cmd',
    version=version,
    description=description,
    long_description=long_description,
    # Get more strings from
    # http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    keywords='buildout recipe',
    author='Gael Pasgrimaud',
    author_email='gael@gawel.org',
    url='http://plone.org/products/collective-recipes',
    license='BSD',
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        'setuptools',
        'zc.buildout'
        # -*- Extra requirements: -*-
    ],
    tests_require=tests_require,
    extras_require=dict(test=tests_require),
    test_suite='collective.recipe.cmd.tests.test_docs.test_suite',
    entry_points=entry_points,
)

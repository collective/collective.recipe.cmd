# -*- coding: utf-8 -*-
"""
This module contains the tool of collective.recipe.cmd
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.7'

long_description = (
    '.. contents::\n\n'
    'Change history\n'
    '**************\n'
    + '\n' +
    read('CHANGES.rst')
    + '\n' +
    'Detailed Documentation\n'
    '**********************\n'
    + '\n' +
    read('README.rst')
    + '\n' +
    'Contributors\n'
    '************\n'
    + '\n' +
    read('CONTRIBUTORS.rst')
    + '\n' +
    'Download\n'
    '********\n'
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

tests_require = ['zope.testing', 'zc.buildout', 'manuel']

setup(name='collective.recipe.cmd',
      version=version,
      description="ZC Buildout recipe to execute a commande line",
      long_description=long_description,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: BSD License',
        ],
      keywords='buildout recipe',
      author='Gael Pasgrimaud',
      author_email='gael@gawel.org',
      url='http://plone.org/products/collective-recipes',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.recipe'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'zc.buildout'
                        # -*- Extra requirements: -*-
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite='collective.recipe.cmd.tests.test_docs.test_suite',
      entry_points=entry_points,
      )

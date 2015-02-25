# -*- coding: utf-8 -*-
"""
This module contains the tool of collective.recipe.cmd
"""
from setuptools import find_packages
from setuptools import setup

version = '0.10'
description = 'A Buildout recipe to execute commands in the console user interface'
long_description = (
    open('README.rst').read() + '\n' +
    open('CONTRIBUTORS.rst').read() + '\n' +
    open('CHANGES.rst').read()
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

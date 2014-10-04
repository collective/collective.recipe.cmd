*********************
collective.recipe.cmd
*********************

.. contents::

Introduction
************

.. image:: https://secure.travis-ci.org/collective/collective.recipe.cmd.png?branch=master
    :target: http://travis-ci.org/collective/collective.recipe.cmd

``collective.recipe.cmd`` is a `Buildout`_ recipe to execute commands in the
console user interface.

.. _`Buildout`: http://buildout.org/

Usage
*****

Supported options
=================

The recipe supports the following options:

``on_install``
    true if the commands must run on install

``on_update``
    true if the commands must run on update

``cmds``
    a set of command lines

``uninstall_cmds``
    a set of command lines executed in the buildout uninstall phase

``shell``
    a valid interpreter (POSIX only)

Example usage
=============

We need a config file::

  >>> cfg = """
  ... [buildout]
  ... parts = cmds
  ...
  ... [cmds]
  ... recipe = collective.recipe.cmd
  ... on_install=true
  ... cmds= %s
  ... """

  >>> test_file = join(sample_buildout, 'test.txt')
  >>> cmds = 'echo "bouh" > %s' % test_file
  >>> write(sample_buildout, 'buildout.cfg', cfg % cmds)

Ok, so now we can touch a file for testing::

  >>> print(system(buildout))
  Installing cmds...

  >>> 'test.txt' in os.listdir(sample_buildout)
  True

And remove it::

  >>> test_file = join(sample_buildout, 'test.txt')
  >>> if sys.platform == 'win32':
  ...    cmds = 'del %s' % test_file
  ... else:
  ...    cmds = 'rm -f %s' % test_file
  >>> write(sample_buildout, 'buildout.cfg', cfg % cmds)

  >>> print(system(buildout))
  Uninstalling cmds.
  Running uninstall recipe.
  Installing cmds...

  >>> 'test.txt' in os.listdir(sample_buildout)
  False

We can run more than one commands::

  >>> if sys.platform == 'win32':
  ...     cmds = '''
  ... echo "bouh" > %s
  ... del %s
  ... ''' % (test_file, test_file)
  ... else:
  ...     cmds = '''
  ... echo "bouh" > %s
  ... rm -f %s
  ... ''' % (test_file, test_file)

  >>> test_file = join(sample_buildout, 'test.txt')
  >>> if sys.platform == 'win32':
  ...     cmds = 'del %s' % test_file
  ... else:
  ...     cmds = 'rm -f %s' % test_file
  >>> write(sample_buildout, 'buildout.cfg', cfg % cmds)

  >>> print(system(buildout))
  Updating cmds...

  >>> 'test.txt' in os.listdir(sample_buildout)
  False

We can also run some python code::

  >>> cfg = """
  ... [buildout]
  ... parts = py py2
  ...
  ... [py]
  ... recipe = collective.recipe.cmd:py
  ... on_install=true
  ... cmds= 
  ...   >>> sample_buildout = buildout.get('directory', '.')
  ...   >>> print(sorted(os.listdir(sample_buildout)))
  ...   >>> os.remove(os.path.join(sample_buildout, ".installed.cfg"))
  ...   >>> print(sorted(os.listdir(sample_buildout)))
  ... [py2]
  ... recipe = collective.recipe.cmd:py
  ... on_install=true
  ... cmds=
  ...   >>> def myfunc(value):
  ...   ...     return value and True or False
  ...   >>> v = 20
  ...   >>> print(myfunc(v))
  ... """

  >>> write(sample_buildout, 'buildout.cfg', cfg)

Ok, so now we run it::

  >>> print(system(buildout))
  Uninstalling cmds.
  Running uninstall recipe.
  Installing py.
  ['.installed.cfg', 'bin', 'buildout.cfg', 'develop-eggs', 'eggs', 'parts']
  ['bin', 'buildout.cfg', 'develop-eggs', 'eggs', 'parts']
  Installing py2.
  True...

If the shell script generated from the commands returns a non-zero
exit/status code then an exception is raised and buildout fails::

  >>> cfg = """
  ... [buildout]
  ... parts = cmds
  ...
  ... [cmds]
  ... recipe = collective.recipe.cmd
  ... on_install=true
  ... cmds= exit 23
  ... """

  >>> write(sample_buildout, 'buildout.cfg', cfg)

  >>> print(system(buildout))
  Uninstalling py2.
  Uninstalling py.
  Installing cmds...
  ...CalledProcessError: Command 'sh .../run' returned non-zero exit status 23

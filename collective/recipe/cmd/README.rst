Supported options
=================

The recipe supports the following options:

.. Note to recipe author!
   ----------------------
   For each option the recipe uses you should include a description
   about the purpose of the option, the format and semantics of the
   values it accepts, whether it is mandatory or optional and what the
   default value is if it is omitted.

on_install

    true if the commands must run on install

on_update

    true if the commands must run on update

cmds

    a set of command lines

uninstall_cmds

    a set of command lines executed in the buildout uninstall phase

shell

    a valid interpreter (POSIX only)

Example usage
=============

.. Note to recipe author!
   ----------------------
   zc.buildout provides a nice testing environment which makes it
   relatively easy to write doctests that both demonstrate the use of
   the recipe and test it.
   You can find examples of recipe doctests from the PyPI, e.g.
   
     http://pypi.python.org/pypi/zc.recipe.egg

   The PyPI page for zc.buildout contains documentation about the test
   environment.

     http://pypi.python.org/pypi/zc.buildout#testing-support

   Below is a skeleton doctest that you can start with when building
   your own tests.

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

  >>> print system(buildout)
  Installing cmds.

  >>> 'test.txt' in os.listdir(sample_buildout)
  True

And remove it::

  >>> test_file = join(sample_buildout, 'test.txt')
  >>> if sys.platform == 'win32':
  ...    cmds = 'del %s' % test_file
  ... else:
  ...    cmds = 'rm -f %s' % test_file
  >>> write(sample_buildout, 'buildout.cfg', cfg % cmds)

  >>> print system(buildout)
  Uninstalling cmds.
  Running uninstall recipe.
  Installing cmds.

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

  >>> print system(buildout)
  Updating cmds.

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
  ...   >>> print sorted(os.listdir(sample_buildout))
  ...   >>> os.remove(os.path.join(sample_buildout, ".installed.cfg"))
  ...   >>> print sorted(os.listdir(sample_buildout))
  ... [py2]
  ... recipe = collective.recipe.cmd:py
  ... on_install=true
  ... cmds=
  ...   >>> def myfunc(value):
  ...   ...     return value and True or False
  ...   >>> v = 20
  ...   >>> print myfunc(v)
  ... """

  >>> write(sample_buildout, 'buildout.cfg', cfg)

Ok, so now we run it::

  >>> print system(buildout)
  Uninstalling cmds.
  Running uninstall recipe.
  Installing py.
  ['.installed.cfg', 'bin', 'buildout.cfg', 'develop-eggs', 'eggs', 'parts']
  ['bin', 'buildout.cfg', 'develop-eggs', 'eggs', 'parts']
  Installing py2.
  True




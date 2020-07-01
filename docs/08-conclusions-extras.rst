Conclusions and Extras
======================

Conclusions
-----------

Congratulations! You have successfully created a python package that is reproducible on other systems!

Your package is better prepared to survive the test of time than most of the software repositories that exist on GitHub because it contains

* helpful documentation
* specific requirements
* tests for each method
* standard installation procedure

Remember that if you decide to continue development on this or any other package, you can increment the version in ``setup.py`` and pip will be able to upgrade the package and any dependencies too.


Extras
------

Additional challenges to explore in your free time

Add the version flag
++++++++++++++++++++

Using the `'version' action <https://docs.python.org/3/library/argparse.html#action>`_ and the following code in setup.py

.. code-block:: python

   # Create version
   VERSION = "0.0.1"
   with open(os.path.join(pkg_dir,'version.py'), 'w') as VF:
       cnt = """
   # THIS FILE IS GENERATED FROM SETUP.PY
   version = '%s'
   """
       VF.write(cnt%(VERSION))

Add additional functions and create tests for them
++++++++++++++++++++++++++++++++++++++++++++++++++

* Create a new function called ``my_median()`` to compute median
* Add a new ``--median`` flag to use this new function instead of ``summarize()``
* Create a new pytest for ``my_median()``

Create a GitHub action that tests your project on push
++++++++++++++++++++++++++++++++++++++++++++++++++++++

https://help.github.com/en/actions/language-and-framework-guides/using-python-with-github-actions

Allow the installation on python2 and use tox to test both python 2 and 3 environments

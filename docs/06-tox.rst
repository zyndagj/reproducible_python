Sandboxing tests with tox
=========================

If you thought it was odd that we ran our pytests in our active python environment, you were correct.
Ideally, the package should be installed in a clean environment that only contains the dependencies of the package being tested.
After it is confirmed that the package can be installed, any tests should then be run.

`Tox <https://tox.readthedocs.io/en/latest/index.html>`_ aims to not only support this usecase, but also run builds and tests on an array of platforms and python versions.

To test summarize with tox, you'll need to

* Install tox via pip
* Create the ``pyproject.toml`` file
* Create the ``tox.ini`` file

Installing tox
--------------

::

   $ pip install --user tox

Creating ``pyproject.toml``
--------------------------

Similar to ``setup.py``, this is a standardized file name that tox looks for, and cannot change.

.. literalinclude:: assets/pyproject.toml
   :linenos:

While a ``pyproject.toml`` can be fairly complex, our just tells tox that a modern version of setuptools is required to build our package.

Creating ``tox.ini``
--------------------

Once again, this is a standardized file name and cannot change.

.. literalinclude:: assets/tox.ini
   :linenos:

The first section describes the python test environments.
In our case, we want to test summarize using python 3.6, 3.7, and 3.8.
If any of these python versions are not available on your system, those tests will be skipped and not throw an error.
Each of these test environments will also be isolated from your system, and fresh dependencies will be installed from scratch.
This will help ensure that your package will work for others as dependencies are updated over time.

The second section describes the test environment.
The "deps" section lists out any dependencies required to build and test (not run) the package.
In the case of summarize, pytest is the only external test dependency, and since tox creates a clean environment, pytest will not be available if not specified here.
Lastly, you specify how the tests are run with the "commands" field.

Running tox
-----------

Running tox is extremely simple

::

   $ tox

It will create a clean virtual environment for every python version you want to test again, install your package and all dependencies, and then run your test commands.
This is meant to make continuous integration and delivery easy and simple.

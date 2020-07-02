Creating tests with pytest
==========================

::

   $ mkdir tests

In your favorite editor, create the file ``tests/test_summarize.py`` and add the follow 4 lines to load the summarize package and numpy.

.. literalinclude:: assets/tests/test_summarize.py
   :language: python
   :linenos:
   :lines: 1-4

Make sure everything is in order by running

::

   $ pip install --user pytest
   $ python -m pytest tests/

to install pytest and make sure it works on our simple test.

If summarize is installed, you can also just run

::

   $ pytest

Your first test
---------------

.. literalinclude:: assets/tests/test_summarize.py
   :pyobject: test_true
   :linenos:

While not very useful for your package, this is a simple test to ensure ``True`` is equal to ``True`` with the standard `assert <https://docs.pytest.org/en/latest/assert.html>`_ statement, and *should* always succeed.

If you have any errors running ``pytest`` at this point, something is wrong with your configuration.

Testing the size of the array
-----------------------------

The next test will ensure that when the ``summarize.gen_numbers`` function is given a 5, it returns an array with 5 values.
Running the code manually would look something like

.. code-block:: python

   >>> import summarize
   >>> summarize.gen_numbers(5)
   array([20, 19, 38, 79, 50])

The test should then assert that the returned array has a length of 5.

.. literalinclude:: assets/tests/test_summarize.py
   :pyobject: test_gen_numbers_5
   :linenos:

Try creating a new test called test_gen_numbers_10 that ensures it works with an argument of 10 too.

Running a test across multiple values
-------------------------------------

For times like this where you want to run a test across multiple values, you can import pytest and utilize the `pytest.mark.parametrize <https://docs.pytest.org/en/stable/parametrize.html>`_ to sweep across a list of values.

   *Note: The decorator function is spelled parametrize, not parameterize. Your brain may unconsciously auto-correct that.*

.. literalinclude:: assets/tests/test_summarize.py
   :language: python
   :linenos:
   :lines: 14-18

Much cleaner, and easier to scale. Try modifying fixture this to also test for 20.

Testing the returned type
-------------------------

Each of the values in the array is the type ``np.int64`` and we can test for that.

.. literalinclude:: assets/tests/test_summarize.py
   :pyobject: test_gen_numbers_5_type
   :linenos:

Testing the returned values
---------------------------

If you call ``summarize.gen_numbers(5)`` multiple times, you'll notice that you get different numbers each time.

.. code-block:: python

   >>> import summarize
   >>> summarize.gen_numbers(5)
   array([20, 19, 38, 79, 50])
   >>> summarize.gen_numbers(5)
   array([95, 94, 80, 68,  4])

You can make this random process deterministic for your tests be setting the `random seed <https://en.wikipedia.org/wiki/Random_seed>`_ used to initialize the random number generator.

.. code-block:: python

   >>> import summarize
   >>> import numpy as np
   >>> np.random.seed(5)
   >>> summarize.gen_numbers(5)
   array([99, 78, 61, 16, 73])
   >>> summarize.gen_numbers(5)
   array([ 8, 62, 27, 30, 80])
   >>> np.random.seed(5)
   >>> summarize.gen_numbers(5)
   array([99, 78, 61, 16, 73])
   >>> np.random.seed(5)
   >>> summarize.gen_numbers(5)
   array([99, 78, 61, 16, 73])

You can apply this to testing as well for deterministic output, even with random calls.

.. literalinclude:: assets/tests/test_summarize.py
   :pyobject: test_gen_numbers_5_vals_seed
   :linenos:

You can also test the returned values of the summary function.
First, with a hardcoded input

.. literalinclude:: assets/tests/test_summarize.py
   :pyobject: test_summarize_custom
   :linenos:

Then, with the seeded input

.. literalinclude:: assets/tests/test_summarize.py
   :pyobject: test_summarize_seed
   :linenos:

Conclusions
-----------

After writing all these tests, you should see something like

::

   ===================================================== test session starts =====================================================
   platform darwin -- Python 3.8.3, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
   rootdir: /Users/gzynda/Documents/reproducible_python/docs/assets
   collected 9 items

   tests/test_summarize.py .........                                                                                       [100%]

   ====================================================== 9 passed in 0.14s ======================================================

and just **feel good**.

This may seem like plenty of tests for just a few simple functions, but you want at least one test per function, and this is a minimum.
Ideally, you would want multiple tests per function to handle all kinds of edge cases.
For instance, even after writing all of these tests, ``summary.summary`` still has the opportunity to fail and throw an error when given ``-N`` is less than 1.
An error like this may be confusing to the user, and a human readable error statement should be returned before exiting.
A test can even be written to test for the exit code.

This guide is not meant to teach you mastery over pytest and testing itself.
This is only meant to be a gentle introduction to show you that writing tests is fairly simple and rewarding.
There is still much to learn, like

* `Error codes <https://docs.pytest.org/en/stable/assert.html#assertions-about-expected-exceptions>`_
* Consistent `setup/teardown <https://docs.pytest.org/en/latest/xunit_setup.html>`_

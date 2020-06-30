Writing the python code
=======================

The "summarize" package will not flex your knowledge of python, it is just a means to learn how to package code.
The source code itself will consist of the single ``__init__.py`` file, which will contain the following 3 functions:

main()
  * The default function that is run when the package is invoked from the command line
  * Uses argparse to accept the ``-N`` parameter, which specifies the number of values that are generated, and defaults to 5.

gen_numbers(n_numbers)
  * A function that uses `numpy.random.randint <https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html>`_ to generate ``n_numbers`` random numbers ranging from 0 to 99

summarize(numbers)
  * Returns the mean of the ``numpy.ndarray``, ``numbers``.

Create the package directory
----------------------------

The current directory is the repository, create another ``summarize`` directory to serve as the package.

.. code-block::

   $ mkdir summarize
   $ cd summarize

When the package is installed on a system, you can imagine this directory and its contents being copied into the ``site-packages`` path.

Creating the ``__init__.py`` file
---------------------------------

While the `__init__.py <https://docs.python.org/3/tutorial/modules.html#packages>`_ file was designed to allow for a directory to be imported as a module with sub-modules, it is a good convention to always follow when creating packages.

In your preferred text editor, create a file called ``__init__.py`` that contains the following sections:

Header
++++++

.. literalinclude:: assets/summarize/__init__.py
   :language: python
   :linenos:
   :lines: 1-4

Line 1 tells your shell how to run this file when executed, and lines 3 and 4 import the packages necessary to run this python program.
While `argparse <https://docs.python.org/3/library/argparse.html>`_ is build in to all python distributions, `Numpy <https://numpy.org/>`_ is an external dependency that must be installed to run.

The ``main()`` function
+++++++++++++++++++

.. literalinclude:: assets/summarize/__init__.py
   :pyobject: main
   :linenos:

Transforming your python script into a tool usable on the CLI can be done in as few as 3 lines.
The first instruction (line 3) constructs the parser object and also describes the the tool itself.
Line 4 adds the first and only argument, which restricts values to integers and includes a description which states the default of 5 numbers.
Line 5 parses the input and generates the ``args`` object. The value passed in through the ``-N`` parameter can be accessed through ``args.N``.

After setting up the CLI arguments, the random numbers are generated in line 7 and the mean is calculated in line 9. Finally, the mean is printed before exiting.

The ``gen_numbers()`` function
++++++++++++++++++++++++++++++

.. literalinclude:: assets/summarize/__init__.py
   :pyobject: gen_numbers
   :linenos:

The ``summarize()`` function
++++++++++++++++++++++++++++

.. literalinclude:: assets/summarize/__init__.py
   :pyobject: summarize
   :linenos:

Epilogue
++++++++

.. literalinclude:: assets/summarize/__init__.py
   :language: python
   :linenos:
   :lines: 31-32

These two lines tell python what to run when the script is invoked. In our case, the ``main()`` function is run.
This section should always exist at the end of a file so all functions and global-scoped variables have already been initialized before running anything.

Current structure
-----------------

At this point, you should have a directory called ``summarize`` containing the file ``__init__.py``.

.. code-block::

   $ cd ..
   $ tree summarize
   summarize/
   └── __init__.py

   0 directories, 1 file

Assuming you have numpy already installed, running ``__init__.py`` with the ``-h`` argument should present you with its help text.

.. code-block::

   $ python summarize/__init__.py -h
   usage: __init__.py [-h] [-N INT]

   A simple tool for computing the mean of a random list

   optional arguments:
     -h, --help  show this help message and exit
     -N INT      Number of random integers [5]

Running it without an argument should also return a number.

.. code-block::

   $ python summarize/__init__.py
   52.2

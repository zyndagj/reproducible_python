Documentation
=============

All good projects have documentation - even if your program has help text.
At a minimum, you should detail any requirements and write instructions for installing, testing, and using a python package.
GitHub will always render the ``README.md`` file on the landing page for your repository.
We suggest creating subsections for each of these topics in the file.

Requirements
------------

.. literalinclude:: assets/README.md
   :linenos:
   :lines: 5-7

Installing
----------

Pip can install from `more places <https://pip.pypa.io/en/stable/reference/pip_install/#examples>`_ than just pypi and a local directory.
If you ``git add``, ``git commit``, and ``git push`` all the files we created, you'll be able to install summarize without a separate checkout command.

These directions show how users can install your package directly from your GitHub URL.

.. literalinclude:: assets/README.md
   :linenos:
   :lines: 9-21

Testing
-------

It's always a good idea to demonstrate how to both setup the test environment and run tests

.. literalinclude:: assets/README.md
   :linenos:
   :lines: 23-38

Usage
-----

Lastly, include an explanation on usage along with expected output.

.. literalinclude:: assets/README.md
   :linenos:
   :lines: 40-55

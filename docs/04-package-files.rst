Creating the package files
==========================

At this point the package directory is completed, but all the metadata that describes the package is still missing.
Meaning you can

.. code-block::

   $ python
   >>> import summarize
   >>> summarize.main()
   35.0

but ``pip install .`` will not work yet.
To enable this, the `setup.py <https://packaging.python.org/tutorials/packaging-projects/#creating-setup-py>`_` file needs to be created to describe the package metadata.

The ``setup.py`` file
---------------------

Open your favorite text editor and create your ``setup.py`` containing the following fields:

.. literalinclude:: assets/setup.py
   :language: python
   :linenos:
   :emphasize-lines: 9

Be sure to fill in the URL to your GitHub repository for the package on line 9.

Current structure
-----------------

Additional Information
----------------------

* https://packaging.python.org/guides/distributing-packages-using-setuptools/
* https://github.com/pypa/sampleproject

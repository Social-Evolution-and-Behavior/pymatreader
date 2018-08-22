.. pymatreader documentation master file, created by
   sphinx-quickstart on Mon Mar 26 16:49:50 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pymatreader
======================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Introduction
------------

pymatreader is a small python package that provides a consistent way of loading
all versions of Matlab .mat files.

pymatreader returns a python :code:`dict` with all the variables found in the
.mat file. Matlab data types are converted to python datatypes as follows:

+-----------------------------------------------+-----------------------------------------------------+
| Matlab                                        | Python                                              |
+===============================================+=====================================================+
| Primitive types (double, single, int, string) | Primitive numpy types (double, single, int, string) |
+-----------------------------------------------+-----------------------------------------------------+
| Structure                                     | dict                                                |
+-----------------------------------------------+-----------------------------------------------------+
| Matrix/Vector                                 | numpy ndarray                                       |
+-----------------------------------------------+-----------------------------------------------------+
| Cell array                                    | list                                                |
+-----------------------------------------------+-----------------------------------------------------+
| Struct array                                  | dict containing lists                               |
+-----------------------------------------------+-----------------------------------------------------+


Install
-------
pymatreader is available via `pypi <https://pypi.org/project/pymatreader/>`_:

.. code-block:: bash

   pip install pymatreader

You can also install it via `conda <https://anaconda.org/obob/pymatreader>`_:

.. code-block:: bash

   conda install -c obob pymatreader


Reference
---------
pymatreader only has one function:

.. automodule:: pymatreader
    :members: read_mat


In case of problems
-------------------
Please raise an issue here: https://gitlab.com/obob/pymatreader/issues


If you want to contribute
-------------------------
Your contribution is always welcome!

pymatreader is developed on gitlab: https://gitlab.com/obob/pymatreader

Please make sure to include proper tests and adhere to the `PEP 8 Style Guide
<https://www.python.org/dev/peps/pep-0008/>`_.

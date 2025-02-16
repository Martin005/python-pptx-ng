.. _install:

Installing
==========

|pp| is hosted on PyPI, so installing with `pip` is simple::

    pip install python-pptx-ng

|pp| depends on the ``lxml`` package and ``Pillow``, the modern version of
the Python Imaging Library (``PIL``). The charting features depend on
``XlsxWriter``. Both ``pip`` and ``easy_install`` will take care of
satisfying these dependencies for you, but if you use the ``setup.py``
installation method you will need to install the dependencies yourself.

Currently |pp| requires Python 2.7 or 3.3 or later. The tests are run against 2.7 and
3.8 on Travis CI.

Dependencies
------------

* Python 2.6, 2.7, 3.3 or later
* lxml
* Pillow
* XlsxWriter (to use charting features)

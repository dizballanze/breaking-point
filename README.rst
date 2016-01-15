breaking-point.py
==========

breaking-point.py helps to find a size of input data where one function starts outperform another function. It is a convenient way to compare different algorithms for a single task.

INSTALLATION
------------

::
    
    pip install breaking-point


USAGE
-----

.. code:: python

    from breaking_point import find_breaking_point

    find_breaking_point(f1, f2, input_generator, start=1, step=1, limit=1000000, trial_count=1000, repeat_count=3)

there 

-  ``f1``, ``f2`` - functions to compare.
-  ``inpurt_generator`` - function that takes ``n`` argument (size of input on current iteration) and returns input data for ``f1`` and ``f2``. Return value should be a tuple with first element - list of non-keyworded arguments and second element - dict of keyword arguments.
-  ``start`` - initial input data size.
-  ``step`` - step of iteration.
-  ``limit`` - maximum amount of input data. If breaking point was not found until limit was reached - iteration stops.
-  ``trial_count`` - number of executions with each input data size.
-  ``repeat_count`` - repeat trial several times and use average performance result.

Function returns ``n0`` - size of input data for which ``f2(n0)`` executed faster than  ``f1(n0)`` or ``None`` if reaches limit.


EXAMPLE
-------

See ``example.py``.


LICENSE
-------

MIT

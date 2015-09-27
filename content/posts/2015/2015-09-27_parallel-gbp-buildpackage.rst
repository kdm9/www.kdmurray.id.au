Parallel building of Debian packages
####################################

:date: 2015-09-27 20:53
:tags: debian, gotchas
:category: notes-to-self
:author: Kevin Murray
:slug: parallel-debian-build
:summary: Use DEB_BUILD_OPTIONS="parallel=4"

To build Debian packages using more than 1 CPU, you can use the
``DEB_BUILD_OPTIONS`` environment variable. Note that the ``debian/rules``
target must have the ``--parallel`` option to ``dh``. This works with pbuilder,
and with ``gbp buildpackage``.

.. code::

    export DEB_BUILD_OPTIONS="parallel=4"  # use 4 cpus
    gbp buildpackage


See `this askubuntu thread
<http://askubuntu.com/questions/337093/how-to-run-parallel-make-with-debuild>`_
for more detail.

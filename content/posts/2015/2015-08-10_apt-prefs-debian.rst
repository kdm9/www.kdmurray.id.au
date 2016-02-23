Apt Preferences and Pinning in Debian
=====================================

:date: 2015-08-10 14:55
:tags: debian, configs
:category: config
:slug: debian-apt-preferences
:author: Kevin Murray
:summary: How to pin to a Debian release using apt_preferences(5)


Put the following in ``/etc/apt/preferences``:

.. code::

    Package: *
    Pin: release unstable
    Pin-Priority: 400

    Package: *
    Pin: release testing
    Pin-Priority: 900

    Package: *
    Pin: release stable
    Pin-Priority: 300


This will pin such that packages from both stable and unstable are available,
but packages from testing are preferred. Which is how I reccommend running
Debian.

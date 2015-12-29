Quick Reference
===============

This page is a short, handy guide to the data available through |project|'s
interface.

Aggregate Data
--------------

Each of the "primary" objects provides direct access to the current data for
that object, such as overall wordcount or the number of participants on the
site or in a region.

``pynano.User``
^^^^^^^^^^^^^^^

.. currentmodule:: pynano.User

.. autosummary::

   wordcount
   name
   id
   winner
   history

``pynano.Region``
^^^^^^^^^^^^^^^^^

.. currentmodule:: pynano.Region

.. autosummary::

   wordcount
   name
   id
   writers
   min
   max
   average
   stddev
   donations
   donors
   history

``pynano.Site``
^^^^^^^^^^^^^^^

.. currentmodule:: pynano.Site

.. autosummary::

   wordcount
   writers
   min
   max
   average
   stddev
   history

Historical Data
---------------

The API also provides day-to-day data for each of these objects. This data is
available as read-only sequence of "day" objects via the ``history`` property
on each one; the sequence is 0-indexed, so to e.g. access day 15's data you
would use the index ``14``.

Users
^^^^^

.. currentmodule:: pynano.day.NanoDay

.. autosummary::

   date
   wordcount

Regions
^^^^^^^

.. currentmodule:: pynano.region.RegionDay

.. autosummary::

   date
   writers
   min
   max
   average
   stddev
   donations
   donors

.. warning::

   There is no ``wordcount`` available in the daily data for Regions. This is a
   limitation of (bug in?) the backend API itself.

Site
^^^^

.. currentmodule:: pynano.site.SiteDay

.. autosummary::

   date
   wordcount
   min
   max
   average
   stddev

Example Usage
^^^^^^^^^^^^^

Individual days from an object's history can be directly accessed::

   >>> from pynano import User
   >>> kromey = User('kromey')
   >>> kromey.history[14].date # The sequence is 0-indexed, so index 14 is day 15
   '2015-11-15'
   >>> kromey.history[14].wordcount
   10499

You can also iterate through an object's history::

   >>> for day in kromey.history:
   ...     print(day.date, day.wordcount)
   ...
   2015-11-01 4137
   2015-11-02 902
   2015-11-03 609
   # ...snip...


Reference Guide
===============

This page is a handy reference to the data available through |project|'s
interface, and how best to make use of it.

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

Performance Considerations
--------------------------

|project| relies on lazy fetching ([#lazy]_) to make object creation as
lightweight as possible: Objects only query the underlying API when data is
actually requested. |project| objects also rely first on the aggregate API, and
only query the history API when the ``history`` property is accessed; they will,
however, use the aggregate data returned from the history API before querying
the aggregate API.

This means that the following sequence results in two queries of the API::

   >>> kromey = User('kromey')
   >>> kromey.wordcount # Queries the aggregate API
   64133
   >>> kromey.history[14].wordcount # Queries the history API
   10499

However, because the User history API returns the aggregate wordcount as well,
the following sequence provides the same data but only queries the API once::

   >>> kromey = User('kromey')
   >>> kromey.history[14].wordcount # Queries the history API
   10499
   >>> kromey.wordcount # Already fetched from the history API; no query!
   64133

Ideally, because it is much "heavier", you should avoid querying the history API
whenever possible and instead rely on the aggregate API as much as you can. On
the other hand, if you know you will need both, it is best to get your history
data first so as to limit the number of overall queries you make; this can be as
simple as "nakedly" accessing the ``history`` property, i.e. touching it is all
that is necessary, you don't have to do anything with it immediately::

   >>> kromey = User('kromey')
   >>> kromey.history # Query is made immediately, even though we aren't using it yet

-----

.. rubric:: Footnotes

.. [#lazy] You can override the "lazy fetching" behavior by providing ``prefetch=True``
           when creating your object; it will then query the API immediately.
           Note, however, that this will only pull from the aggregate API, and
           does not prefetch historical data.


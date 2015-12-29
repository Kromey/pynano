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


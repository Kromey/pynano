Quickstart
==========

Everything you need to get up and running with |project| in 90 seconds or
less! ([#disclaimer]_)

Installation
------------

The easiest way to install |project| is to simply run :command:`pip install
pynano`. It will conveniently take care of the requirements for you.

.. warning::

   As of |today|, |project| has not yet been uploaded to PyPi, and thus this
   command will currently fail.

.. todo::

   Provide manual install instructions. Maybe.

Usage
-----

.. currentmodule:: pynano

Users
^^^^^

::

   >>> from pynano import User
   >>> kromey = User('kromey')
   >>> kromey.wordcount
   64133
   >>> kromey.name
   'Kromey'

The only required parameter when creating a ``User`` object is the user name,
which is case sensitive but should otherwise match what appears on the website::

   >>> bob = User('bob vila')
   >>> bob.name
   'Bob Vila'

Alternatively you can use the API-style name instead (e.g. `bob-vila` for the
user `Bob Vila`).

:attr:`~.User.wordcount` and :attr:`~.User.name` will probably be the most
common properties you'll want; for others, refer to the :ref:`Reference Guide
<ref-pynano-user>`.

Regions
^^^^^^^

::

   >>> from pynano import Region
   >>> fairbanks = Region('usa-alaska-fairbanks')
   >>> fairbanks.wordcount
   1675173
   >>> fairbanks.name
   'USA :: Alaska :: Fairbanks'

Like Users, Region objects require the region name when you create them. Also
like Users, the names are case-insensitive; you can either use the API-style
name as in the example above (i.e. separate each part with a single hyphen, such
as `usa-alaska-fairbanks` for the region `USA :: Alaska :: Fairbanks`), the
two-colon separated style that appears in the region names (e.g. `USA :: Alaska
:: Fairbanks`), or simply use spaces (e.g. `USA Alaska Fairbanks`).

Again, the most common properties you will want to access are :attr:`~.Region.wordcount`
and :py:attr:`~.Region.name`, although :attr:`~.Region.writers` may be common
as well. Refer to the :ref:`Reference Guide <ref-pynano-region>` for more.

Site
^^^^

::

   >>> from pynano import Site
   >>> site = Site()
   >>> site.wordcount
   3396901959
   >>> site.writers
   181344

The Site object provides access to site-wide statistics, and thus does not
require -- nor even accept -- a name parameter; here, you will likely find
yourself most interested in :attr:`~.Site.wordcount` and :attr:`~.Site.writers`.
Refer to the :ref:`Reference Guide <ref-pynano-site` for more.

-----

.. rubric:: Footnotes

.. [#disclaimer] 90-second start up time not guaranteed. Your results may vary.
                 Terms subject to change without notice, but don't matter anyway.

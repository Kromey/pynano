Quickstart
==========

Everything you need to get up and running with |project| in 90 seconds or
less! [#disclaimer]_

Installation
------------

The easiest way to install |project| is to simply run :command:`pip install pynano`.

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

The only required parameter when creating a ``User`` object is the user name.
While the argument is case-insensitive, the name must otherwise match what the
API expects, such as spaces being replaced with hyphens::

   >>> bob = User('bob-vila')
   >>> bob.name
   'Bob Vila'

Likely the most common properties you will want to access are :attr:`~.User.wordcount`
and :py:attr:`~.User.name`.

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
like Users, the names are case-insensitive; the parts of the Region's name are
separated by a single hyphen, as the example above shows: The Region `USA ::
Alaska :: Fairbanks` is referenced as `usa-alaska-fairbanks` in your code.

Again, the most common properties you will want to access are :attr:`~.Region.wordcount`
and :py:attr:`~.Region.name`, although :attr:`~.Region.writers` may be common
as well.

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

.. rubric:: Footnotes

.. [#disclaimer] 90-second start up time not guaranteed.

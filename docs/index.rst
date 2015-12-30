.. title:: Welcome

Welcome to |project|
====================

`National Novel Writing Month <http://nanowrimo.org>`_ is an annual event in
which the goal is generally to write 50,000 words of the first draft of a novel
in the 30 days of November.

Naturally, the hosts have graciously supplied a website with various means of
updating and tracking one's progress through this adventure, including an `API
<http://nanowrimo.org/wordcount_api>`_ to allow users to create their own
progress trackers.

This is where |project| comes into play.

The API is a simple XML-based one supplied over HTTP. While this means it is
fairly simple in most languages to build tools to utilize this data, there are
not many -- or, perhaps, any -- existing ones out there. The API also suffers
from a few drawbacks in its design: inconsistencies between the endpoints
(e.g. you might find ``wcdate`` as the date one place, but ``date`` in another);
some strange naming choices; the fact that each endpoint uses a different,
unique top-level element; and multiple elements for identical data in different
contexts (e.g. ``user_wordcount``, ``region_wordcount``, ``site_wordcount``).

This lack of tools, combined with the inconsistencies and peculiar structure,
lead me, when faced with needing to integrate two systems with this API, to
create a module that smoothed out the wrinkles while providing simple, Pythonic
access to this data.


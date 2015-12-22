import requests
import xmltodict


class NanoBase(object):
    """Base object for pynano API objects.

    This object implements the common functionality for fetching and processing
    API data from the NaNoWriMo API.
    """

    # API name for this object
    _name = None

    # Endpoint URLs for this object; must include a '{name}' placeholder
    _primary_url = None
    _history_url = None

    # Caches for retrieved data
    _data = None
    _history = None

    def __init__(self, name, prefetch=False):
        """Initialize a new pynano API object.

        The only required parameter is name, which is the name of the current
        object as recognized by the backend API.

        If prefetch is set to True, the API will be queried immediately; if not,
        it will be lazily fetched on first use.
        """

        self._name = name

        if prefetch:
            self._fetch()

    def _fetch_element(self, index, is_history=False):
        """Get a particular data element, fetching from the API if necessary.

        If is_history is True, then the subsequent fetch (if necessary) will use
        the history API instead of the primary API.
        """
        try:
            # Attempt to return the requested data element
            return self._data[index]
        except (KeyError, TypeError):
            # Didn't find it, or nothing fetched yet
            # Fetch data from the API
            self._fetch(is_history)

            # If we still don't find it, allow the exception to be raised
            return self._data[index]

    def _fetch(self, history=False):
        """Fetch data from the API.

        If the history parameter is True, then the history URL will be queried
        for data; if it is False, then the primary URL will be queried.
        """
        if history:
            # Fetching history data
            url = self._history_url
        else:
            # Fetching primary data
            url = self._primary_url

        # Now fetch from the server
        r = requests.get(url.format(name=self._name))
        # Parse the returned data (removing root element)
        data = next(iter(xmltodict.parse(r.text).values()))

        # Now stash the data
        if history:
            # Stash the history data
            self._history = data['wordcounts']

            if self._data is None:
                # Haven't fetched primary data, stash what we got
                del data['wordcounts']
                self._data = data
        else:
            # Stash the primary data
            self._data = data


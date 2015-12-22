import requests
import xmltodict


class NanoBase(object):
    """Base object for pynano API objects.

    This object implements the common functionality for fetching and processing
    API data from the NaNoWriMo API.
    """

    # Force the object to fetch from the history endpoint
    fetch_history = False

    # API name for this object
    _name = None

    # Endpoint URLs for this object; must include a '{name}' placeholder
    _primary_url = None
    _history_url = None

    # Cache for retrieved data
    _data = None

    def __init__(self, name, prefetch=False, fetch_history=False):
        """Initialize a new pynano API object.

        The only required parameter is name, which is the name of the current
        object as recognized by the backend API.

        If prefetch is set to True, the API will be queried immediately; if not,
        it will be lazily fetched on first use.
        If fetch_history is set to True, the API will always use the history URL
        rather than using the primary URL when it can.
        """
        self.fetch_history = fetch_history

        self._name = name

        if prefetch:
            self._fetch()

    def _fetch(self, history=None):
        """Fetch data from the API.

        If the history parameter is present and True, then the history URL will
        be queried for data; if it is present and False, then the primary URL
        will be queried.
        If the history parameter is omitted, then the object's fetch_history
        value will be used instead.
        """
        if history is None:
            # Default to our fetch_history setting
            history = self.fetch_history

        if history:
            # Fetching history data
            url = self._history_url
        else:
            # Fetching primary data
            url = self._primary_url

        # Now fetch from the server
        r = requests.get(url.format(name=self._name))
        # Parse and stash the returned data
        self._data = xmltodict.parse(r.text)


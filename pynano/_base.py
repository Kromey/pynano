import requests


class NanoBase(Object):
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
        self.fetch_history = fetch_history

        self._name = name

        if prefetch:
            self._fetch()

    def _fetch(history=self._fetch_history):
        if history:
            url = self._history_url
        else:
            url = self._primary_url

        r = requests.get(url.format(name=self._name))
        self._data = r.text


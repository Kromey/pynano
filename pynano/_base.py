
class NanoBase(Object):
    """Base object for pynano API objects.

    This object implements the common functionality for fetching and processing
    API data from the NaNoWriMo API.
    """

    # Force the object to fetch from the history endpoint
    fetch_history = False

    # Endpoint URLs for this object
    _primary_url = None
    _history_url = None

    def __init__(self, prefetch=False, fetch_history=False):
        self.fetch_history = fetch_history

        if prefetch:
            self._fetch()

    def _fetch(history=self._fetch_history):
        if history:
            # TODO: Fetch from the history API endpoint
            pass
        else:
            # TODO: Fetch from the primary API endpoint
            pass


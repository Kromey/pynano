class NanoDay(object):
    """A pynano historical Day object.

    These objects provide access to historical data for a particular day from
    the history API.
    """
    # Data for this object
    _data = None

    def __init__(self, data):
        self._data = data

    @property
    def date(self):
        return self._data['wcdate']

    @property
    def wordcount(self):
        return self._data['wc']


class NanoDay(object):
    """A pynano historical Day object.

    These objects provide access to historical data for a particular day from
    the history API.
    """
    # Data for this object
    _data = None

    def __init__(self, data):
        """
        :param dict data: A dictionary containing the day's properties
        """
        self._data = data

    @property
    def date(self):
        """The date of this object.

        This property corresponds to `wcdate` or `date` in the API.
        """
        return self._data['date']

    @property
    def wordcount(self):
        """The word count on this date.

        This property corresponds to `wc` in the API.
        """
        return self._data['wc']


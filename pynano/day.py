from collections.abc import Sequence


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


class NanoDaySequence(Sequence):
    _history = None

    def __init__(self, history, *args, **kwargs):
        """Initialize the sequence with our day-to-day history.

        :param dict history: Dictionary (indexed by day-1) of daily data
        """
        super().__init__(*args, **kwargs)
        self._history = history

    def __len__(self):
        """Return the length of our history."""
        return len(self._history)

    def __getitem__(self, key):
        """Retrieve the day represented by the given key.

        The sequence is 0-indexed, so to access data for e.g. the 12th, key
        should be 11.

        :param int key: The day (less 1) to retrieve
        :raise TypeError: if `key` is not an integer
        :raise IndexError: if `key` is out of range

        .. todo::
           Need to detect the difference between out-of-range index, and a gap
           in the data; if the latter, need an "empty" response.
        """
        try:
            key = int(key)

            return self._history[key]
        except ValueError:
            # Not an integer
            raise TypeError('Index must be an integer: {key}'.format(key=key))
        except KeyError:
            raise IndexError()


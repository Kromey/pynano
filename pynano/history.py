from collections.abc import Sequence


class NanoHistorySequence(Sequence):
    _history = None

    def __init__(self, history, *args, **kwargs):
        """Initialize the sequence with our day-to-day history."""
        super().__init__(*args, **kwargs)
        self._history = history

    def __len__(self):
        """Return the length of our history."""
        return len(self._history)

    def __getitem__(self, key):
        """Retrieve the day represented by the given key.

        The sequence is 0-indexed, so to access data for e.g. the 12th, key
        should be 11.
        """
        try:
            key = int(key)

            return self._history[key]
        except ValueError:
            # Not an integer
            raise TypeError('Index must be an integer: {key}'.format(key=key))
        except KeyError:
            # TODO: Need to detect the difference between out-of-range index,
            # and a gap in the data; if the latter, need an "empty" response
            # For now just assume we're out-of-range
            raise IndexError()


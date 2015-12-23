from .base import NanoBase
from .day import NanoDay


class RegionDay(NanoDay):
    @property
    def wordcount(self):
        # The API doesn't provide this, and we can't seem to calculate it
        # So for now at least just pretend it doesn't exist
        raise AttributeError("'RegionDay' object has no attribute 'wordcount'")

    @property
    def min(self):
        return self._data['min']

    @property
    def max(self):
        return self._data['max']

    @property
    def average(self):
        return self._data['average']

    @property
    def stddev(self):
        return self._data['stddev']

    @property
    def writers(self):
        return self._data['count']

    @property
    def donations(self):
        return self._data['donations']

    @property
    def donors(self):
        return self._data['numdonors']


class Region(NanoBase):
    # Endpoint URLs for region objects
    _primary_url = 'http://nanowrimo.org/wordcount_api/wcregion/{name}'
    _history_url = 'http://nanowrimo.org/wordcount_api/wcregionhist/{name}'

    # Use our own Day object
    _day_class = RegionDay
    # The day field for the history API
    _date_field = 'date'

    @property
    def id(self):
        return self._fetch_element('rid')

    @property
    def name(self):
        return self._fetch_element('rname')

    @property
    def wordcount(self):
        return self._fetch_element('region_wordcount')

    @property
    def min(self):
        return self._fetch_element('min')

    @property
    def max(self):
        return self._fetch_element('max')

    @property
    def average(self):
        return self._fetch_element('average')

    @property
    def stddev(self):
        return self._fetch_element('stddev')

    @property
    def writers(self):
        return self._fetch_element('count')

    @property
    def donations(self):
        return self._fetch_element('donations')

    @property
    def donors(self):
        return self._fetch_element('numdonors')


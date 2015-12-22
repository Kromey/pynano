from .base import NanoBase


class Region(NanoBase):
    # Endpoint URLs for region objects
    _primary_url = 'http://nanowrimo.org/wordcount_api/wcregion/{name}'
    _history_url = 'http://nanowrimo.org/wordcount_api/wcregionhist/{name}'

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


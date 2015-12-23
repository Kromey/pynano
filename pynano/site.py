from .base import NanoBase
from .day import NanoDay


class SiteDay(NanoDay):
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
    def count(self):
        # TODO: What is this one??
        return self._data['count']


class Site(NanoBase):
    # Endpoint URLs for region objects
    _primary_url = 'http://nanowrimo.org/wordcount_api/wcstatssummary{name}'
    _history_url = 'http://nanowrimo.org/wordcount_api/wcstats{name}'

    # Use our own Day object
    _day_class = SiteDay

    def __init__(self, *args, **kwargs):
        """Site objects don't have a name, but we have to supply one."""
        super().__init__(name='', *args, **kwargs)

    @property
    def wordcount(self):
        return self._fetch_element('site_wordcount')

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


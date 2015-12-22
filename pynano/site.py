from ._base import NanoBase


class Site(NanoBase):
    # Endpoint URLs for region objects
    _primary_url = 'http://nanowrimo.org/wordcount_api/wcstatssummary{name}'
    _history_url = 'http://nanowrimo.org/wordcount_api/wcstats{name}'

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


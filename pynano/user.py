from .base import NanoBase


class User(NanoBase):
    # Endpoint URLs for user objects
    _primary_url = 'http://nanowrimo.org/wordcount_api/wc/{name}'
    _history_url = 'http://nanowrimo.org/wordcount_api/wchistory/{name}'

    @property
    def id(self):
        return self._fetch_element('uid')

    @property
    def name(self):
        return self._fetch_element('uname')

    @property
    def wordcount(self):
        return self._fetch_element('user_wordcount')

    @property
    def winner(self):
        return self._fetch_element('winner') == 'true'


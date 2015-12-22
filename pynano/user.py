from ._base import NanoBase


class User(NanoBase):
    # Endpoint URLs for user objects
    _primary_url = 'http://nanowrimo.org/wordcount_api/wc/{name}'
    _history_url = 'http://nanowrimo.org/wordcount_api/wchistory/{name}'

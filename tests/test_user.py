import pytest
from requests import HTTPError
import responses


from pynano import User  # noqa


def test_user_wordcount(kromey_response):
    with responses.RequestsMock() as rsps:
        kromey_response(rsps)
        kromey = User('kromey')
        assert kromey.wordcount == 64135

    # We should get no requests going out now that we've fetched
    with responses.RequestsMock() as rsps:
        assert kromey.wordcount == 64135


def test_user_wordcount_prefetch(kromey_response):
    with responses.RequestsMock() as rsps:
        kromey_response(rsps)
        kromey = User('kromey', prefetch=True)

    # We should get no requests going out now that we've prefetched
    with responses.RequestsMock() as rsps:
        assert kromey.wordcount == 64135


def test_user_name(kromey_response):
    with responses.RequestsMock() as rsps:
        kromey_response(rsps)
        kromey = User('kromey')
        assert kromey.name == 'Kromey'


def test_user_id(kromey_response):
    with responses.RequestsMock() as rsps:
        kromey_response(rsps)
        kromey = User('kromey')
        assert kromey.id == '217507'


def test_user_winner(kromey_response):
    with responses.RequestsMock() as rsps:
        kromey_response(rsps)
        kromey = User('kromey')
        assert kromey.winner


def test_user_wordcount_setter(kromey_writeapi):
    with responses.RequestsMock() as rsps:
        kromey_writeapi(rsps)
        kromey = User('kromey')

        # No key
        assert kromey.secret_key is None
        with pytest.raises(ValueError):
            kromey.wordcount = 12345

        # Wrong key
        kromey.secret_key = '123abc'
        assert kromey.secret_key == '******'
        with pytest.raises(HTTPError):
            kromey.wordcount = 12345

        # Correct key
        kromey.secret_key = 'abc123'
        assert kromey.secret_key == '******'
        kromey.wordcount = 12345


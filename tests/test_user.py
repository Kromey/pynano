import responses


from pynano import User  # noqa


def test_user_wordcount(kromey_response):
    with responses.RequestsMock() as rsps:
        kromey_response(rsps)
        kromey = User('kromey')
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


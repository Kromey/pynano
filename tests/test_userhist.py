import responses


from pynano import User  # noqa


def test_userhist_wordcount(kromey_hist_response):
    with responses.RequestsMock() as rsps:
        kromey_hist_response(rsps)
        kromey = User('kromey')
        # Access history first to query the history API
        kromey.history
        assert kromey.wordcount == 64133


def test_userhist_name(kromey_hist_response):
    with responses.RequestsMock() as rsps:
        kromey_hist_response(rsps)
        kromey = User('kromey')
        # Access history first to query the history API
        kromey.history
        assert kromey.name == 'Kromey'


def test_userhist_id(kromey_hist_response):
    with responses.RequestsMock() as rsps:
        kromey_hist_response(rsps)
        kromey = User('kromey')
        # Access history first to query the history API
        kromey.history
        assert kromey.id == '217507'


def test_userhist_winner(kromey_hist_response):
    with responses.RequestsMock() as rsps:
        kromey_hist_response(rsps)
        kromey = User('kromey')
        # Access history first to query the history API
        kromey.history
        assert kromey.winner


def test_userhist_daily_date(kromey_hist_response):
    with responses.RequestsMock() as rsps:
        kromey_hist_response(rsps)
        kromey = User('kromey')
        assert kromey.history[14].date == '2015-11-15'
        assert kromey.history[10].date == '2015-11-11'


def test_userhist_daily_wordcount(kromey_hist_response):
    with responses.RequestsMock() as rsps:
        kromey_hist_response(rsps)
        kromey = User('kromey')
        assert kromey.history[14].wordcount == 10499
        assert kromey.history[10].wordcount == 804


def test_userhist_sequence(kromey_hist_response):
    word_sum = 0

    with responses.RequestsMock() as rsps:
        kromey_hist_response(rsps)
        kromey = User('kromey')
        for day in kromey.history:
            word_sum += day.wordcount

        # Each day's wordcount should add up to the month's wordcount
        assert word_sum == kromey.wordcount


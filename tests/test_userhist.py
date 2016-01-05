
def test_userhist_wordcount(kromey_hist):
    # Note that this value that in the kromey fixture
    # This assures us we're using the different file
    assert kromey_hist.wordcount == 64133


def test_userhist_name(kromey_hist):
    assert kromey_hist.name == 'Kromey'


def test_userhist_id(kromey_hist):
    assert kromey_hist.id == '217507'


def test_userhist_winner(kromey_hist):
    assert kromey_hist.winner


def test_userhist_daily_date(kromey_hist):
    assert kromey_hist.history[14].date == '2015-11-15'
    assert kromey_hist.history[10].date == '2015-11-11'


def test_userhist_daily_wordcount(kromey_hist):
    assert kromey_hist.history[14].wordcount == 10499
    assert kromey_hist.history[10].wordcount == 804


def test_userhist_sequence(kromey_hist):
    word_sum = 0

    for day in kromey_hist.history:
        word_sum += day.wordcount

    # Each day's wordcount should add up to the month's wordcount
    assert word_sum == kromey_hist.wordcount


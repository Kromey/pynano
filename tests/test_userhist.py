from pynano import User


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


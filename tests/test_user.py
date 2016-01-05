
def test_user_wordcount(kromey):
    assert kromey.wordcount == 64135


def test_user_name(kromey):
    assert kromey.name == 'Kromey'


def test_user_id(kromey):
    assert kromey.id == '217507'


def test_user_winner(kromey):
    assert kromey.winner


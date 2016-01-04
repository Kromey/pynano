from decimal import Decimal


from pynano import Site


def test_site_wordcount(site):
    assert site.wordcount == 3397271645


def test_site_writers(site):
    assert site.writers == 181443


def test_site_min(site):
    assert site.min == 0


def test_site_max(site):
    assert site.max == 1000000


def test_site_average(site):
    assert site.average == Decimal('18723.6303')


def test_site_stddev(site):
    assert site.stddev == Decimal('27124.87896618218')


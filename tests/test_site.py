from decimal import Decimal


import responses


# flake8 doesn't think this one is part of our package
from pynano import Site  # noqa


def test_site_wordcount(site_response):
    with responses.RequestsMock() as rsps:
        site_response(rsps)
        site = Site()
        assert site.wordcount == 3397271645


def test_site_writers(site_response):
    with responses.RequestsMock() as rsps:
        site_response(rsps)
        site = Site()
        assert site.writers == 181443


def test_site_min(site_response):
    with responses.RequestsMock() as rsps:
        site_response(rsps)
        site = Site()
        assert site.min == 0


def test_site_max(site_response):
    with responses.RequestsMock() as rsps:
        site_response(rsps)
        site = Site()
        assert site.max == 1000000


def test_site_average(site_response):
    with responses.RequestsMock() as rsps:
        site_response(rsps)
        site = Site()
        assert site.average == Decimal('18723.6303')


def test_site_stddev(site_response):
    with responses.RequestsMock() as rsps:
        site_response(rsps)
        site = Site()
        assert site.stddev == Decimal('27124.87896618218')


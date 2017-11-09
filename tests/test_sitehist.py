from decimal import Decimal


import responses


# flake8 doesn't think this one is part of our package
from pynano import Site  # noqa


def test_site_wordcount(site_hist_response):
    with responses.RequestsMock() as rsps:
        site_hist_response(rsps)
        site = Site()
        # Access history first to query the history API
        site.history
        assert site.wordcount == 3398572178


def test_site_writers(site_hist_response):
    with responses.RequestsMock() as rsps:
        site_hist_response(rsps)
        site = Site()
        # Access history first to query the history API
        site.history
        assert site.writers == 181490


def test_sitehist_daily_date(site_hist_response):
    with responses.RequestsMock() as rsps:
        site_hist_response(rsps)
        site = Site()
        assert site.history[14].date == '2015-11-15'
        assert site.history[10].date == '2015-11-11'


def test_sitehist_daily_wordcount(site_hist_response):
    with responses.RequestsMock() as rsps:
        site_hist_response(rsps)
        site = Site()
        assert site.history[14].wordcount == 4002914868


def test_sitehist_daily_min(site_hist_response):
    with responses.RequestsMock() as rsps:
        site_hist_response(rsps)
        site = Site()
        assert site.history[14].min == -45500


def test_sitehist_daily_max(site_hist_response):
    with responses.RequestsMock() as rsps:
        site_hist_response(rsps)
        site = Site()
        assert site.history[14].max == 458000


def test_sitehist_daily_average(site_hist_response):
    with responses.RequestsMock() as rsps:
        site_hist_response(rsps)
        site = Site()
        assert site.history[14].average == Decimal('2099.1573')


def test_sitehist_daily_stddev(site_hist_response):
    with responses.RequestsMock() as rsps:
        site_hist_response(rsps)
        site = Site()
        assert site.history[14].stddev == Decimal('3727.1484283641685')


def test_sitehist_daily_count(site_hist_response):
    with responses.RequestsMock() as rsps:
        site_hist_response(rsps)
        site = Site()
        assert site.history[14].count == 108587306



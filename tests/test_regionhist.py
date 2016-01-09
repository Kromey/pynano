from decimal import Decimal


import pytest
import responses


# flake8 doesn't think this one is part of our package
from pynano import Region  # noqa


def test_region_wordcount(fbx_hist_response):
    with responses.RequestsMock() as rsps:
        fbx_hist_response(rsps)
        fbx = Region('usa-alaska-fairbanks')
        # Access history first to query the history API
        fbx.history
        assert fbx.wordcount == 1675173


def test_region_name(fbx_hist_response):
    with responses.RequestsMock() as rsps:
        fbx_hist_response(rsps)
        fbx = Region('usa-alaska-fairbanks')
        # Access history first to query the history API
        fbx.history
        assert fbx.name == 'USA :: Alaska :: Fairbanks'


def test_region_id(fbx_hist_response):
    with responses.RequestsMock() as rsps:
        fbx_hist_response(rsps)
        fbx = Region('usa-alaska-fairbanks')
        # Access history first to query the history API
        fbx.history
        assert fbx.id == '4058792'


def test_region_writers(fbx_hist_response):
    with responses.RequestsMock() as rsps:
        fbx_hist_response(rsps)
        fbx = Region('usa-alaska-fairbanks')
        # Access history first to query the history API
        fbx.history
        assert fbx.writers == 78


def test_regionhist_daily_date(fbx_hist_response):
    with responses.RequestsMock() as rsps:
        fbx_hist_response(rsps)
        fbx = Region('usa-alaska-fairbanks')
        assert fbx.history[14].date == '2015-11-15'
        assert fbx.history[10].date == '2015-11-11'


def test_regionhist_daily_wordcount(fbx_hist_response):
    with responses.RequestsMock() as rsps:
        fbx_hist_response(rsps)
        fbx = Region('usa-alaska-fairbanks')
        fbx.history

    # Break out of the Responses context manager because it swallows exceptions
    with pytest.raises(AttributeError) as excinfo:
        fbx.history[14].wordcount
    # We don't actually get a wordcount parameter on RegionDay
    assert "'RegionDay' object has no attribute 'wordcount'" in str(excinfo)


def test_regionhist_writers(fbx_hist_response):
    with responses.RequestsMock() as rsps:
        fbx_hist_response(rsps)
        fbx = Region('usa-alaska-fairbanks')
        assert fbx.history[14].writers == 78


def test_regionhist_min(fbx_hist_response):
    with responses.RequestsMock() as rsps:
        fbx_hist_response(rsps)
        fbx = Region('usa-alaska-fairbanks')
        assert fbx.history[14].min == 0


def test_regionhist_max(fbx_hist_response):
    with responses.RequestsMock() as rsps:
        fbx_hist_response(rsps)
        fbx = Region('usa-alaska-fairbanks')
        assert fbx.history[14].max == 10499


def test_regionhist_average(fbx_hist_response):
    with responses.RequestsMock() as rsps:
        fbx_hist_response(rsps)
        fbx = Region('usa-alaska-fairbanks')
        assert fbx.history[14].average == Decimal('3509.8889')


def test_regionhist_stddev(fbx_hist_response):
    with responses.RequestsMock() as rsps:
        fbx_hist_response(rsps)
        fbx = Region('usa-alaska-fairbanks')
        assert fbx.history[14].stddev == Decimal('3248.054179138224')


def test_regionhist_donations(fbx_hist_response):
    with responses.RequestsMock() as rsps:
        fbx_hist_response(rsps)
        fbx = Region('usa-alaska-fairbanks')
        assert fbx.history[14].donations == Decimal('0.0')
        assert fbx.history[6].donations == Decimal('25.0')


def test_regionhist_donors(fbx_hist_response):
    with responses.RequestsMock() as rsps:
        fbx_hist_response(rsps)
        fbx = Region('usa-alaska-fairbanks')
        assert fbx.history[14].donors == 0
        assert fbx.history[6].donors == 1


from decimal import Decimal


import responses


# flake8 doesn't think this one is part of our package
from pynano import Region  # noqa


def test_region_wordcount(fbx_response):
    with responses.RequestsMock() as rsps:
        fbx_response(rsps)
        fbx = Region('usa-alaska-fairbanks')
        assert fbx.wordcount == 1675173


def test_region_name(fbx_response):
    with responses.RequestsMock() as rsps:
        fbx_response(rsps)
        fbx = Region('usa-alaska-fairbanks')
        assert fbx.name == 'USA :: Alaska :: Fairbanks'


def test_region_id(fbx_response):
    with responses.RequestsMock() as rsps:
        fbx_response(rsps)
        fbx = Region('usa-alaska-fairbanks')
        assert fbx.id == '4058792'


def test_region_writers(fbx_response):
    with responses.RequestsMock() as rsps:
        fbx_response(rsps)
        fbx = Region('usa-alaska-fairbanks')
        assert fbx.writers == 78


def test_region_min(fbx_response):
    with responses.RequestsMock() as rsps:
        fbx_response(rsps)
        fbx = Region('usa-alaska-fairbanks')
        assert fbx.min == 0


def test_region_max(fbx_response):
    with responses.RequestsMock() as rsps:
        fbx_response(rsps)
        fbx = Region('usa-alaska-fairbanks')
        assert fbx.max == 103293


def test_region_average(fbx_response):
    with responses.RequestsMock() as rsps:
        fbx_response(rsps)
        fbx = Region('usa-alaska-fairbanks')
        assert fbx.average == Decimal('21476.5769')


def test_region_stddev(fbx_response):
    with responses.RequestsMock() as rsps:
        fbx_response(rsps)
        fbx = Region('usa-alaska-fairbanks')
        assert fbx.stddev == Decimal('25294.652295124793')


def test_region_donations(fbx_response):
    with responses.RequestsMock() as rsps:
        fbx_response(rsps)
        fbx = Region('usa-alaska-fairbanks')
        assert fbx.donations == Decimal('235.0')


def test_region_donors(fbx_response):
    with responses.RequestsMock() as rsps:
        fbx_response(rsps)
        fbx = Region('usa-alaska-fairbanks')
        assert fbx.donors == 8


def test_region_instantiation(fbx_response):
    with responses.RequestsMock() as rsps:
        fbx_response(rsps)
        fbx = Region('usa-alaska-fairbanks')
        assert fbx.name == 'USA :: Alaska :: Fairbanks'

    with responses.RequestsMock() as rsps:
        fbx_response(rsps)
        fbx = Region('usa alaska fairbanks')
        assert fbx.name == 'USA :: Alaska :: Fairbanks'

    with responses.RequestsMock() as rsps:
        fbx_response(rsps)
        fbx = Region('usa :: alaska :: fairbanks')
        assert fbx.name == 'USA :: Alaska :: Fairbanks'


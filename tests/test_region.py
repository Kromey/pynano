from decimal import Decimal


from pynano import Region


def test_region_wordcount(fbx):
    assert fbx.wordcount == 1675173


def test_region_name(fbx):
    assert fbx.name == 'USA :: Alaska :: Fairbanks'


def test_region_id(fbx):
    assert fbx.id == '4058792'


def test_region_writers(fbx):
    assert fbx.writers == 78


def test_region_min(fbx):
    assert fbx.min == 0


def test_region_max(fbx):
    assert fbx.max == 103293


def test_region_average(fbx):
    assert fbx.average == Decimal('21476.5769')


def test_region_stddev(fbx):
    assert fbx.stddev == Decimal('25294.652295124793')


def test_region_donations(fbx):
    assert fbx.donations == Decimal('235.0')


def test_region_donors(fbx):
    assert fbx.donors == 8


import pytest


from pynano import User


@pytest.fixture(scope='module')
def kromey():
    """A test User object tied to the user Kromey"""
    return User('kromey')


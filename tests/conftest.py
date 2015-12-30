import pytest
import responses


from pynano import User


@pytest.fixture(scope='module')
def kromey():
    """A test User object tied to the user Kromey"""
    with open('tests/data/user_kromey.xml') as f:
        kromey_xml = f.read()

    with responses.RequestsMock() as rsps:
        rsps.add(responses.GET, 'http://nanowrimo.org/wordcount_api/wc/kromey',
                body=kromey_xml, status=200,
                content_type='application/xml; charset=utf-8')
        return User('kromey', prefetch=True)


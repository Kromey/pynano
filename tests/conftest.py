import os


import pytest
import responses


# flake8 doesn't think this one is part of our package
from pynano import Region, Site, User  # noqa


@pytest.fixture()
def kromey_response():
    def response_wrapper(rsps):
        file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'data/user_kromey.xml')
        with open(file_path) as f:
            kromey_xml = f.read()

        rsps.add(responses.GET,
                 'http://nanowrimo.org/wordcount_api/wc/kromey',
                 body=kromey_xml, status=200,
                 content_type='application/xml; charset=utf-8')

    return response_wrapper


@pytest.fixture()
def kromey_hist_response():
    def response_wrapper(rsps):
        file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'data/userhist_kromey.xml')
        with open(file_path) as f:
            kromeyhist_xml = f.read()

        rsps.add(responses.GET,
                 'http://nanowrimo.org/wordcount_api/wchistory/kromey',
                 body=kromeyhist_xml, status=200,
                 content_type='application/xml; charset=utf-8')

    return response_wrapper


@pytest.fixture()
def fbx_response():
    def response_wrapper(rsps):
        file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'data/region_fbx.xml')
        with open(file_path) as f:
            region_xml = f.read()

        url = 'http://nanowrimo.org/wordcount_api/wcregion/usa-alaska-fairbanks'

        rsps.add(responses.GET,
                 url,
                 body=region_xml, status=200,
                 content_type='application/xml; charset=utf-8')

    return response_wrapper


@pytest.fixture()
def site_response():
    def response_wrapper(rsps):
        file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'data/site.xml')
        with open(file_path) as f:
            site_xml = f.read()

        url = 'http://nanowrimo.org/wordcount_api/wcstatssummary'

        rsps.add(responses.GET,
                 url,
                 body=site_xml, status=200,
                 content_type='application/xml; charset=utf-8')

    return response_wrapper


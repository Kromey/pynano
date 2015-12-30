import sys
import subprocess


def test_pep8():
    result = subprocess.call(['pep8', '--statistics', '--show-source'])
    assert result == 0


def test_pypi():
    result = subprocess.call(['python',
                              'setup.py',
                              'check',
                              '--restructuredtext',
                              '--strict',
                              '--metadata',
                              ])
    assert result == 0


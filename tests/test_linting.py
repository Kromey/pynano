import sys
import subprocess


# We really only care about code "cleanness" on modern versions
LINT = sys.version_info >= (3, 4, 0)


def test_pep8():
    if LINT:
        result = subprocess.call(['pep8', '--statistics', '--show-source'])
        assert result == 0


def test_pypi():
    if LINT:
        result = subprocess.call(['python',
                                  'setup.py',
                                  'check',
                                  '--restructuredtext',
                                  '--strict',
                                  '--metadata',
                                  ])
        assert result == 0


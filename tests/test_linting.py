import subprocess
import sys


# We really only care about code "cleanness" on modern versions
LINT = sys.version_info >= (3, 4, 0)


def test_pep8():
    if LINT:
        result = subprocess.call(['flake8',
                                  # Activate Radon with the default complexity
                                  '--radon-max-cc', '10',
                                  ])
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


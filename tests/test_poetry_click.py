from poetry_click import __version__
import click.testing
import pytest
from poetry_click.cli import search_beers


def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def runner():
    return click.testing.CliRunner()

def test_search_beers(runner):
    result = runner.invoke(search_beers, ['--name', 'IPA'])
    assert result.exit_code == 0

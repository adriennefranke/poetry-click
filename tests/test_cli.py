from poetry_click import __version__
import click.testing
import pytest
# from poetry_click.cli import search_beers
from poetry_click import cli


def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def runner():
    return click.testing.CliRunner()

def test_search_beers(runner, mock_requests_get):
    result = runner.invoke(cli.search_beers)
    # result = runner.invoke(search_beers, ['--name', 'IPA'])
    assert result.exit_code == 0

@pytest.fixture
def mock_requests_get(mocker):
    return mocker.patch("requests.get")
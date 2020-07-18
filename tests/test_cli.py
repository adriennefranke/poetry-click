from poetry_click import __version__
import click.testing
import pytest
# from poetry_click.cli import search_beers
from poetry_click import cli
import requests_mock


def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def runner():
    return click.testing.CliRunner()

def test_search_beers(runner, mock_requests_get):
    result = runner.invoke(cli.search_beers)
    assert result.exit_code == 0

@pytest.fixture
def mock_requests_get(mocker):
    mock = mocker.patch("requests.get")
    mock.return_value.json.return_value = {
    "id": 1,
    "name": "Stephen King",
    "username": "kingofhorror"
    }
    return mock
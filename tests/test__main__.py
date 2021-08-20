import shlex
from unittest.mock import MagicMock, call

import click.testing
import pytest

import his-geo-backend
from his-geo-backend import __main__


@pytest.fixture
def patch_path():
    return "his-geo-backend.__main__"


@pytest.fixture(scope="session")
def cli_runner():
    return click.testing.CliRunner()


@pytest.fixture(scope="session")
def cli_invoke(cli_runner):
    def invoke(cmd: str) -> click.testing.Result:
        split_cmd = shlex.split(cmd)
        assert split_cmd[0] == "his-geo-backend"
        return cli_runner.invoke(__main__.entry_point, split_cmd[1:])

    return invoke


@pytest.fixture
def mock_click_module(mocker, patch_path) -> MagicMock:
    return mocker.patch(f"{patch_path}.click")


def test_entry_point_works(mock_click_module):
    __main__.entry_point.callback()
    assert mock_click_module.mock_calls == [call.echo(his-geo-backend.__version__)]


@pytest.mark.behavioral
def test_his-geo-backend_bare(cli_invoke):
    result = cli_invoke("his-geo-backend")
    assert result.exit_code == 0
    assert result.output == his-geo-backend.__version__ + "\n"

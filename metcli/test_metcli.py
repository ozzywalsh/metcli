from unittest.mock import MagicMock
import pytest
import requests
import requests_mock
from . import metcli


def test_met_request_should_return_dict():
    session = requests.Session()
    adapter = requests_mock.Adapter()
    session.mount('mock', adapter)

    json_data = '{"name": "Bob"}'

    with requests_mock.mock() as m:
        m.get('https://www.met.ie/api/weather/national', text=json_data)
        result = metcli.met_request('weather/national')

        assert isinstance(result, dict)


def test_met_request_should_handle_connection_problem(capsys):
    with requests_mock.Mocker() as m:
        m.get('https://www.met.ie/api/weather/national',
              exc=requests.exceptions.ConnectionError)

        with pytest.raises(SystemExit) as excinfo:
            metcli.met_request('weather/national')

        assert str(excinfo.value.code) == 'There was a problem connecting to Met Éireann.'


def test_get_national():
    metcli.met_request = MagicMock()
    metcli.get_national()

    url = metcli.met_request.call_args
    assert 'weather/national' in str(url)

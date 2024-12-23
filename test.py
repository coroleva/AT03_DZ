import pytest
import requests
from main import get_random_cat_image  # Импортируем функцию из основного файла



@pytest.mark.parametrize("expected_status_code", [
    (200),
])
def test_successful_request(expected_status_code, mocker):
    # Подмена ответа от сервера
    mock_response = mocker.MagicMock(spec=requests.Response)
    mock_response.status_code = expected_status_code
    mock_response.json.return_value = [{"url": "https://example.com/cat.jpg"}]

    # Патчинг функции requests.get
    mocker.patch('main.requests.get', return_value=mock_response)

    result = get_random_cat_image()

    assert result == "https://example.com/cat.jpg"


import pytest
from main import get_random_cat_image  # Импортируем функцию из основного файла


@pytest.mark.parametrize("expected_status_code", [
    (404),
])
def test_unsuccessful_request(expected_status_code, mocker):
    # Подмена ответа от сервера
    mock_response = mocker.MagicMock(spec=requests.Response)
    mock_response.status_code = expected_status_code

    # Патчинг функции requests.get
    mocker.patch('main.requests.get', return_value=mock_response)

    result = get_random_cat_image()

    assert result is None
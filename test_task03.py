# Задание 3 - Integration Testing (Mocking)
# Создайте аналогичный тест из п.3 предыдущего задания, но вместо отправки GET-запроса,
# создайте Mock, возвращающий список из 10 пользователей.


from unittest.mock import patch


with patch('test_task02.response') as mock:
    mock_response = mock.return_value
    mock_response.status_code.return_value = 200
    mock_response.headers.return_value = 'application/json; charset=utf-8'
    with open('1.txt', 'r+') as file:
        mock_response.json.return_value = file.read()


class TestMock:
    def test_status_code(self):
        assert mock_response.status_code() == 200

    def test_header(self):
        assert mock_response.headers() == 'application/json; charset=utf-8'

    def test_body(self):
        assert mock_response.json().count("'id'") == 10

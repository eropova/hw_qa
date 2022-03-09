# Задание 3 - Integration Testing (Mocking)
# Создайте аналогичный тест из п.3 предыдущего задания, но вместо отправки GET-запроса,
# создайте Mock, возвращающий список из 10 пользователей.

from unittest.mock import Mock

with open('1.txt', 'r+') as file:
    response = Mock(return_value=file)

response.status_code.return_value = 200
response.headers.return_value = 'application/json; charset=utf-8'
response.json.return_value = 10

class TestMock:
    def test_status_code(self):
        assert response.status_code() == 200


    def test_header(self):
        assert response.headers() == 'application/json; charset=utf-8'


    def test_body(self):
        assert response.json() == 10

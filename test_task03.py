# Задание 3 - Integration Testing (Mocking)
# Создайте аналогичный тест из п.3 предыдущего задания, но вместо отправки GET-запроса,
# создайте Mock, возвращающий список из 10 пользователей.

from unittest.mock import Mock


response = Mock(return_value=[{'user1': 1}, {'user2': 2}, {'user3': 3}, {'user4': 4}, {'user5': 5},
                              {'user6': 6}, {'user7': 7}, {'user8': 8}, {'user9': 9}, {'user10': 10}])
response.status_code.return_value = 200
response.json.return_value = 10
response.headers.return_value = 'application/json; charset=utf-8'


def test_status_code():
    assert response.status_code() == 200


def test_header():
    assert response.headers() == 'application/json; charset=utf-8'


def test_body():
    assert len(response()) == 10

# Задание 2 - API Testing
# Для HTTP запросов с методом GET на URL - https://jsonplaceholder.typicode.com/users
# Создайте следующие тесты:
# 1) Проверка кода ответа: status code is 200 OK
# 2) Проверка заголовка ответа (response header):
# - the content-type header exists in the obtained response
# - the value of the content-type header is application/json; charset=utf-8
# 3) Проверка тела ответа (response body):
# - the content of the response body is the array of 10 users (JSON)
# - Tests should be done using the provided REST web-service.

from requests import get

response = get('https://jsonplaceholder.typicode.com/users')
json_response = response.json()

# 1) Проверка кода ответа: status code is 200 OK


def test_status_code():
    assert response.status_code == 200


# 2) Проверка заголовка ответа (response header):
# - the content-type header exists in the obtained response
# - the value of the content-type header is application/json; charset=utf-8

def test_header():
    assert 'content-type' in response.headers
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'


# 3) Проверка тела ответа (response body):
# - the content of the response body is the array of 10 users (JSON)

def test_body():
    assert len(json_response) == 10

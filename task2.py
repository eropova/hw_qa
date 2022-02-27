from requests import get

response = get('https://jsonplaceholder.typicode.com/users')
json_response = response.json()

print(response)
print(response.status_code)
print(response.headers['Content-Type'])
print(len(json_response))
print((json_response))

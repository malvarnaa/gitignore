import requests

r = requests.get('https://jsonplaceholder.typicode.com/todos/1')
data = r.json()
print(data)

post = {
    'body': 'Loream ipsum',
    'title': 'title',
    'userId': 5
}
req = requests.post('https://jsonplaceholder.typicode.com/post', json=post)
print(req.json())
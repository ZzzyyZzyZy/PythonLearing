import requests

user_info = {'name': ['letian', 'letian2'], 'password': '123'}
a = requests.post("http://127.0.0.1:5000/register", data=user_info)

json_data = {'a': 1, 'b': 2}
b = requests.post("http://127.0.0.1:5000/add", json=json_data)

c = requests.post("http://127.0.0.1:5000/sum", json=json_data)

file_data = {'image': open('Lenna.jpg', 'rb')}

user_info = {'info': 'Lenna'}

d = requests.post("http://127.0.0.1:5000/upload", data=user_info, files=file_data)

print(d.text)

print(a.text)

print(b.text)
print(c.headers)
print(c.text)

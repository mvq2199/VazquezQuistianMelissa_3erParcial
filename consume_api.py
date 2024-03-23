import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print('Solicitud Exitosa')
    print("Datos: ", data["id"])
else:
    print("Error en la solicitud:", response.text)
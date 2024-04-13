import requests

url = "http://127.0.0.1:5000/sistema"
respuesta = requests.get(url)
    
if respuesta.status_code == 200:
        datos = respuesta.json()
        print ("La información de tu ordenador es:")
        print ("Hostname", datos[0]["Hostname"])
        print ("IP", datos[1]["IP"])
else:
        print("No se pudo obtener la información deseada")
   
  
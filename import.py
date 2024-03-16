import json

file_name = "data.json"

# Abrimos el archivo JSON
with open(file_name) as data: 
    datos = json.load(data)

# Ahora 'datos' tiene el contenido del archivo JSON y procedemos a imprimirlo llamando solo las variables 'ip', 'so' y 'hostname'
    print("IP:" + datos["ip"] + "\n" + "SO:" + datos["so"] + "\n" + "Hostname:" + datos["hostname"])

# Ahora debemos imprimir unicamente el numero '10' del arreglo version, para ello primero debemos acceder a la lista
# Y para imprimirlo iniciamos llamando por la posicion de lo datos, en este caso se inica en '0', y este es el dato a llamar 
    print("Versión:" + datos["version"][0])

    



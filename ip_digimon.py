# Importar la bibioteca request
import requests

def obtener_informacion_ip():
    # URL de la API IP
    url = "http://ip-api.com/json"
    respuesta = requests.get(url)
    
    # Verificar si la solicitud fue exitosa (código de estado 200)
    if respuesta.status_code == 200:
    # Devolver los datos de los posts en formato JSON
        datos = respuesta.json()
        return datos
    
def obtener_digimon(nombre):
    # URL de la API Digimon
    url = f"https://digimon-api.vercel.app/api/digimon/name/{nombre}"
    respuesta = requests.get(url)
    
    # Verificar si la solicitud fue exitosa (código de estado 200)
    if respuesta.status_code == 200:
    # Devolver los datos de los posts en formato JSON
        datos = respuesta.json()
        return datos
    else:
    # Si la solicitud no fue exitosa, imprimir el código de estado
        print(f"ERROR, no se pudo obtener información del Digimon: {nombre}.")
        print("Por favor verifica que se haya ingresado correctamente")
        return None
    
resultado = obtener_informacion_ip()

print("Iniciemos verificando la conexion a Internet para la consulta Digimon")
print("Conexión a Internet exitosa, a continuación los detalles:")
# Confirmar la conexión a Internet con el uso de la API IP

if resultado:
    print(f"IP: {resultado['query']}")
    print(f"País: {resultado['country']}")
    print(f"Región: {resultado['regionName']}")
    print(f"ISP: {resultado['isp']}")
    # Imprimir los datos de conexión a Internet

print("Ahora hagamos la consulta Digimon")
nombre_digimon = input("Ingrese el nombre del Digimon que desea buscar(Por ejemplo: Agumon, Omnimon, Patamon, Gomamon, Halsemon, etc): ")

resultado = obtener_digimon(nombre_digimon)
# Consultar el digimon y almacenarlo en la variable "resultado"

if resultado:
    print("Información del Digimon")
    print(f"Nombre: {resultado[0]['name']}")
    print(f"Nivel: {resultado[0]['level']}")
    print(f"Imagen: {resultado[0]['img']}")
    # Imprimir información de Digimon



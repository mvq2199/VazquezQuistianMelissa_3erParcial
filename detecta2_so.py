#En este codigo los print generados en la anterior practica se agregaran sobre un archivo Json

import platform
import sys
import subprocess
import json
file_name = "data.jason"
sistemaop = sys.platform
sistema = platform.system()
version = platform.win32_ver()

if sistema == 'Windows':
    local = subprocess.getoutput("""for /f "tokens=2 delims=[]" %a in ('ping -n 1 -4 "%computername%"') do @echo %a""")
else:
    local = subprocess.getoutput("ifconfig | grep 'inet ' | grep -Fv 127.0.0.1 | awk '{print $2}'")
hostname = platform.node()
cpu = platform.processor()

#Hacemos un diccionario en donde se determinen los print y se coloca sobre un solo archivo Json
diccionario = {'ip':local, 'so':sistema, 'version':version, 'hostname':hostname, 'cpu':cpu}
#dictionaryToJson = json.dumps(diccionario)
#print(dictionaryToJson)
file = open(file_name, "w")
json.dump(diccionario, file, indent=4)
file.close()


#Los archivos Json se 
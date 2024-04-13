import platform
import sys
import subprocess
import json
from flask import Flask, jsonify

sistema = platform.system()

if sistema == 'Windows':
    local = subprocess.getoutput("""for /f "tokens=2 delims=[]" %a in ('ping -n 1 -4 "%computername%"') do @echo %a""")
else:
    local = subprocess.getoutput("ifconfig | grep 'inet ' | grep -Fv 127.0.0.1 | awk '{print $2}'")
hostname = platform.node()

app = Flask(__name__)
tasks = [
    {"id":1, "Hostname": hostname, "active":True},
    {"id":2, "IP": local, "active":True},
   ]

@app.route('/sistema', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True)


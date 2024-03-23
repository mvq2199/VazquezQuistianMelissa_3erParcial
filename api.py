#En caso de no tener instalado el flaks, se procede a instalar con "pip install flask" y "pip install -- upgrade pip"

from flask import Flask, jsonify

app = Flask(__name__)
tasks = [
    {"id":1, "user":"Hector", "active":True},
    {"id":2, "user":"Noe", "active":False},
    {"id":3, "user":"Bladimir", "active":True},
    {"id":4, "user":"Miriam", "active":True},
    {"id":4, "user":"Marciano", "active":False},
    {"id":4, "user":"Melissa", "active":False},
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, jsonify
from users import users

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
    return jsonify(users)  # Cambiado de user a users

@app.route('/users')
def usersHandler():
    # Importar API de usuarios
    return jsonify(users)

if __name__ == '__main__':
    # Puerto y host
    app.run(host="0.0.0.0", port=4000, debug=True)


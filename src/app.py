from flask import Flask, jsonify
from oneUser import users
from users import users

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
    return jsonify(user)

@app.route('/users')
def usersHandler():
    #importar API de usuarios
    return jsonify(users)


if __name__ == '__main__':

    #port and host
    app.run(host="0.0.0.0", port=4000, debug=True)

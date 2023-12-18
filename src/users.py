import requests
import json
import random

def get_users():
    response = requests.get('https://dummyjson.com/users')
    json_data = response.json()
    return json_data

def get_random_user():
    users = get_users()
    random_user = random.choice(users)
    return random_user

# Almacenar todos los usuarios al importar el módulo
users = get_users()

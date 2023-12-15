import requests
import json
import random

response = requests.get('https://dummyjson.com/users')
randomUser = random.choice(response)

oneUser = randomUser.json()
users = response.json()
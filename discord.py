import requests
import random
from random import randint
from time import sleep

# Aquí puedes añadir todos los mensajes que desees.
# Se enviará uno de estos mensajes de manera aleatoria
messages = [
    "Hi!",
    "Hello",
    "gm",
    "Gm",
    "gn",
    "Gn",
    "Hello everybody!",
    "Hello everybody :)",
    "Hey!",
    "Good day"
]

auth = { 
    'authorization': 'TOKEN_DE_AUTORIZACION' # Introduce aquí tu auth token
}

url = [
    "https://discord.com/api/v9/channels/ID_DEL_CANAL/messages", # Sustitye el ID_DEL_CANAL
    "https://discord.com/api/v9/channels/ID_DEL_CANAL/messages",
    "https://discord.com/api/v9/channels/ID_DEL_CANAL/messages", 
]

i = 0

min_time = 60 # Pon aquí el tiempo mínimo (en segundos) entre mensaje y mensaje
max_time = 120 # Aquí el tiempo máximo

while(True):
    if i == len(url):
        i=0
    msg = {
    'content': random.choice(messages)
    }    
    requests.post(url[i], headers = auth, data = msg)
    i=i+1
    sleep(randint(min_time,max_time)) # Esperamos entre 1 y 2 minutos (60s-120s) para enviar el siguiente mensaje
    # Te recomiendo subir el tiempo de espera para evitar el SPAM

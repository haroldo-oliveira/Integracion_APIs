# https://core.telegram.org
# https://core.telegram.org/bots/api

import requests
import random

list_msg = ['Working!', 'Funciona!', 'Ready to use!', 'Very Good!', 'Great Thank You!']

def confirmationBot(list_msg):
    url = 'https://core.telegram.org'
    token_api = '5475967725:AAGJ8H4QUEJDOJM9z_-NnBHMowihOXkfG8I'  # Cambiar por tu token de BotFather.


                    # https://api.telegram.org/bot<token>/METHOD_NAME
    r = requests.post("https://api.telegram.org/bot5475967725:AAGJ8H4QUEJDOJM9z_-NnBHMowihOXkfG8I/sendMessage",
    data = {
            'chat_id': '@haroPrueba',  # Cambiar por en nombre de tu canal.
            'text': random.choice(list_msg)
            })

    return random.choice(list_msg)
confirmationBot(random.choice(list_msg))

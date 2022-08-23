# https://core.telegram.org
# https://core.telegram.org/bots/api

import requests
import random
import os

list_msg = ['Working!', 'Funciona!', 'Ready to use!', 'Very Good!', 'Great Thank You!']

def confirmationBot(list_msg):
    token_api = os.environ['API_TELEGRAM']  # Cambiar por tu token de BotFather.
    url = 'https://core.telegram.org'

                    # https://api.telegram.org/bot<token>/METHOD_NAME
    r = requests.post("https://api.telegram.org/bot&key="+token_api+"/sendMessage",
    data = {
            'chat_id': '@haroPrueba',  # Cambiar por en nombre de tu canal.
            'text': random.choice(list_msg)
            })

    return random.choice(list_msg)
confirmationBot(random.choice(list_msg))

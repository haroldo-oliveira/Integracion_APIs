# https://core.telegram.org
# https://core.telegram.org/bots/api
# https://www.el-tiempo.net/api/json/v2/home


from time import time_ns
import requests
import json

def climaCiudades(ciudad):

    url = 'https://www.el-tiempo.net/api/json/v2/home'

    api = requests.get(url)
    if api.status_code == 200:
        json_data = json.loads(api.content)

    ciudades = json_data['ciudades']
    temperatura = ''
    estado_cielo = ''

    for ciudadInfo in ciudades:
        if ciudadInfo["nameProvince"] == ciudad:

            estado_cielo = ciudadInfo["stateSky"]["description"]
            temperatura = ciudadInfo["temperatures"]

    textoFinal = f'''
            El clima hoy en {ciudad}...\n
            Estado del Cielo  ==> {estado_cielo} \n
            Temperatura ==> {temperatura}
            '''

    return textoFinal

# ciudad = ''
# ciudad = ciudad.capitalize()
# def  meteoBot():
#     tiempo = climaCiudades(ciudad)

#                     # https://api.telegram.org/bot<token>/METHOD_NAME
#     requests.post("https://api.telegram.org/bot5475967725:AAGJ8H4QUEJDOJM9z_-NnBHMowihOXkfG8I/sendMessage",
#     data = {
#             'chat_id': '@haroPrueba',
#             'text': tiempo
#             })

#     return tiempo

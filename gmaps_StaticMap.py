import requests
import os

location = ''
location.capitalize()
def maps(location):
    api_key = os.environ['API_MAPS']
    url = 'https://maps.googleapis.com/maps/api/staticmap?'

    center = location
    zoom = 10

    r = requests.get(url + 'center='+ center + '&zoom=' +str(zoom) + '&size=1024x768&key='+api_key)

    return url + 'center='+ center + '&zoom=' +str(zoom) +'&size=1024x768&key='+api_key

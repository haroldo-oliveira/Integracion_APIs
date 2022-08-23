import requests
import os

location = ''
location.capitalize()
def maps(location):

    api_key = os.environ['API_MAPS']
    # url = 'https://www.google.com/maps/embed/v1/directions? &origin=Oslo+Norway  &destination=Telemark+Norway  &avoid=tolls|highways'
    url = 'https://www.google.com/maps/embed/v1/directions?'

    center = location
    zoom = 10

    # r = requests.get(url + 'center='+ center + '&zoom=' +str(zoom) + '&size=1024x768 + 'origins=' + home + '&destination=' + target + '&key=' + api_key)')
    r = requests.get(url + 'center='+ center + '&zoom=' +str(zoom) + '&size=1024x768&key='+api_key)

    return url + 'center='+ center + '&zoom=' +str(zoom) +'&size=1024x768&key='+api_key

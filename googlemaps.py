import requests
# import raw_input

# url = 'https://maps.googleapis.com/maps/api/place/details/output?parameters'
api_key = 'AIzaSyD02SoQsG7ClLP_O9iyPmlkjbq3jmgOe6Y'

url = 'https://maps.googleapis.com/maps/api/staticmap?'

location = input("Introduzca el nombre de una ciudad Espanola: ")

center = location

zoom = 10

r = requests.get(url + 'center='+ center + '&zoom=' +str(zoom) + '&size=1024x768&key='+api_key)

print(url + 'center='+ center + '&zoom=' +str(zoom) + '&size=1024x768&key='+api_key)

from tabnanny import check
from urllib import response
import requests
import os
import smtplib  # Enviar Email

# API Key
api_key = os.environ['API_MAPS']

# home address input
home = input("Type where you are!\n")

# target address input
target = input("Enter a target address!\n")

# base_url
# url = 'https://maps.googleapis.com/maps/api/distancematrix/json? origins=home &destinations=target &key= + api_key'
url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

# get response
r = requests.get(url + 'origins=' + home + '&destination=' + target + '&key=' + api_key)

# return km as text
km = r.json()['rows'][0]['elements'][0]['distance']['text']
# return time as text
time = r.json()['rows'][0]['elements'][0]['duration']['text']

# print total travel time
print('\nEl tiempo total del trayecto es de ', time)
print('\nLa distancia total es de ', km, 'km')

# # check if travel time is more than 3 hs
# if(seconds > 10800):
#     # email contraints
#     sender = 'malocaswear@gmail.com'
#     recipient = 'malocaswear@gmail.com'
#     subject = 'Demasiado lejos!'
#     message = 'Este viaje es mas largo de 3 horas, recomendamos elegir otro destino'

#     # format email
#     email = 'Subject: {}\n\n{}'.format(subject, message)

#     # get sender password
#     password_file = open("password.txt", "r")
#     password = password_file.readline()
#     password_file.close()

#     # creates SMTP session
#     s = smtplib.SMTP("smtp.gmail.com", 587)

#     # start TLS for security
#     s.starttls()

#     # authentication
#     s.login(sender, password)

#     # sending the mail
#     s.sendmail(sender, recipient, email)

#     # terminating the session
#     s.quit()

#     # success message
#     print("\nSuccessfully sent a sick-day email to", recipient, "since the travel time was too long")

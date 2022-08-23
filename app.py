import streamlit as st
from PIL import Image
from gmaps_StaticMap import maps, location
from tlgram_MeteoBot import climaCiudades
from tlgram_ConfirBot import confirmationBot, list_msg

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title='Eniax App', page_icon=':speech_balloon:', layout='wide')

# --- LOGO ---
st.image("images/eniax-logo-rojo.png", width=200)

# --- HEADER SECTION ---
with st.container():
    st.title('Eniax App Info Ciudades')
    st.subheader('EVALUACIÓN TÉCNICA DE INTEGRACIÓN')
    st.write("Hola, Bienvenidos a nuestra APP 💡📉🌡")

    st.markdown('<a href="https://github.com/haroldo-oliveira/Integracion_APIs" target="_self">GitHub - Integracion_APIs</a>', unsafe_allow_html=True)

# --- GOOGLE STATIC MAP SECTION ---
with st.container():
    st.write("---")
    st.subheader('GOOGLE STATIC MAP SECTION')
    left_column, right_column = st.columns(2)

    with left_column:
        location = st.text_input("Introduzca el nombre de una ciudad Espanola: ")
        location
    with right_column:
        st.image(maps(location))

# --- TELEGRAM METEO BOT ---
with st.container():
    st.write("---")
    st.subheader('TELEGRAM METEO BOT SECTION')
    left_column, right_column = st.columns(2)

    with left_column:
        ciudad = st.text_input("Introduzca el nombre de una ciudad Espanola, que te apetezca consultar el clima actual: ")
        ciudad
    with right_column:
        st.write(climaCiudades(ciudad))

        if st.button('Reenviar a tu Telegram!'):
            st.write(confirmationBot(list_msg))
        else:
            st.write('Reciba la Meteo via mensaje de texto en tuTelegram, haciendo clik en el boton arriba...')

# --- TELEGRAM CONFIRMATION BOT ---
with st.container():
    st.subheader('TELEGRAM CONFIRMATION BOT SECTION')

    if st.button('Confirmacion Telegram'):
        st.write(confirmationBot(list_msg))

    else:
        st.write('Confirme el proceso haciendo clik, en el boton arriba...')

# --- GOOGLE EMBED MAP SECTION ---
with st.container():
    st.write("---")
    st.subheader('GOOGLE EMBED MAP SECTION')
    left_column, right_column = st.columns(2)

    # with left_column:
    #     location = st.text_input("Introduzca el nombre de una ciudad de Espana: ")
    #     location
    # with right_column:
    #     st.image('#')

# --- GOOGLE DISTANCE MATRIX SECTION ---
with st.container():
    st.write("---")
    st.subheader('GOOGLE DISTANCE MATRIX SECTION')
    left_column, right_column = st.columns(2)

    # with left_column:
    #     location = st.text_input("Introduzca el nombre de una ciudad de Espana: ")
    #     location
    # with right_column:
    #     st.image('#')

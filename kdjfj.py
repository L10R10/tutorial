import streamlit as st
import os
from PyPDF2 import PdfReader
import docx2txt
from PIL import Image
import plotly.express as px
import pandas as pd
from info import cargar_partidos
from Comentarios import come
from posiciones import pos
from foto import bio
from video import vid
from archivos import carga



img = Image.open("data/logo.jpg")

st.set_page_config(page_title="BEISBOL INVERNAL", page_icon= img, layout="wide")

def main():
    st.title("BEISBOL INVERNAL")
    menu = ["Pagina principal", "Calendario", "Pocisiones" , "Fotos", "Videos", "Cargar Archivos", "Comentarios"]
    barra = st.sidebar.selectbox("Menu", menu)
    img = Image.open("data/logo.jpg")
    st.image(img, use_container_width=True)

    if barra == "Pagina principal":
        st.subheader("noticias y mas")
    elif barra == "Calendario":
        cargar_partidos()
    elif barra == "Pocisiones":
        pos()
    elif barra == "Fotos":
        bio()
    elif barra == "Videos":
        vid()
    elif barra == "Cargar Archivos":
        carga()
    elif barra == "Comentarios":
        st.subheader("Dejanos tus Comentarios")
        come()





if __name__ == "__main__":
        main()









import streamlit as st

# Título de la aplicación
st.title("Encuesta sobre Béisbol Invernal")


preguntas = [
    "¿Cuál es tu equipo favorito en la liga invernal?",
    "¿Qué jugador crees que ha tenido el mejor rendimiento esta temporada?",
    "¿Qué aspectos del béisbol invernal te parecen más emocionantes: la estrategia del juego o la habilidad individual de los jugadores?",
    "¿Cuál ha sido el partido más memorable que has visto en la liga invernal?",
    "¿Qué opinas sobre las nuevas reglas implementadas en la liga esta temporada?",
    "¿Cómo crees que afecta la agencia libre a la competitividad de los equipos?",
    "¿Qué jugador dominicano crees que ha dejado una huella más profunda en la historia del béisbol invernal?",
    "¿Cuál es tu recuerdo favorito relacionado con el béisbol invernal?",
    "¿Qué importancia tiene el béisbol invernal en la cultura dominicana?",
    "¿Cómo te sientes acerca de la cobertura mediática del béisbol invernal?",
    "¿Qué cambios te gustaría ver en la liga para mejorar la experiencia de los fanáticos?",
    "¿Cuál es tu pronóstico para la próxima temporada en términos de equipos y jugadores destacados?",
    "¿Qué impacto crees que tiene el béisbol invernal en el desarrollo de jóvenes talentos en la República Dominicana?"
]


with st.form(key='encuesta'):
    respuestas = []
    for pregunta in preguntas:
        respuesta = st.text_input(pregunta)
        respuestas.append(respuesta)

    
    submit_button = st.form_submit_button(label='Enviar Respuestas')

if submit_button:
    st.success("¡Gracias por participar en la encuesta!")
    # Aquí podrías guardar las respuestas en un archivo o base de datos
    for i, respuesta in enumerate(respuestas):
        st.write(f"Pregunta {i + 1}: {respuesta}")

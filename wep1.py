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




#aqui comienzo

import streamlit as st
import pandas as pd
import os

# pregunta 1
st.title("Encuesta: ¿Cuál es el equipo más apoyado de béisbol en la República Dominicana?")

# Opciones de los equipos
equipos = ["Águilas Cibaeñas", "Leones del Escogido", "Tigres del Licey", "Estrellas Orientales", "Gigantes del Cibao", "Toros del Este"]

# Pregunta 2
st.header("¿Cuál es tu equipo favorito?")
equipo_seleccionado = st.selectbox("Selecciona un equipo:", equipos)

# Botón para envia respuestas
if st.button("Enviar"):
    st.success(f"Has seleccionado: {equipo_seleccionado}")
    
    # Guardar la respuesta en un archivo CSV
    if not os.path.isfile('resultados.csv'):
        with open('resultados.csv', 'w') as f:
            f.write('Equipo\n')  

    with open('resultados.csv', 'a') as f:
        f.write(f'{equipo_seleccionado}\n')  # Escribir la respuesta

# esto es para los resultados
st.header("Resultados de la encuesta")
if os.path.isfile('resultados.csv'):
    df = pd.read_csv('resultados.csv')
    st.write(df)
else:
    st.write("Aún no hay resultados, gracias por su respuestas =').")






















if __name__ == "__main__":
        main()
from datetime import date
import pandas as pd
import streamlit as st

st.title("Instrumento de medición")

form = st.form("formulario")

# Evitar lo más posible las preguntas abiertas
# No preguntar el nombre
nombre = form.text_input(
    label="Nombre",
    placeholder="Escribe aquí...")

edad = form.number_input(
    label="Edad",
    min_value=0,
    max_value=130,
    value=18)

confianza = form.slider(
    label="Nivel de confianza",
    min_value=1,
    max_value=10,
    value=5)

redes = [
    "Tiktok",
    "X (antes Twitter",
    "Instagram",
    "Facebook",
    "Otra"
    ]

red_social = form.radio(
    label="Red social donde vio el deepfake",
    options=redes,
    index=3)

delegaciones_cdmx = [
    "Álvaro Obregón",
    "Azcapotzalco",
    "Benito Juárez",
    "Coyoacán",
    "Cuajimalpa de Morelos",
    "Cuauhtémoc",
    "Gustavo A. Madero",
    "Iztacalco",
    "Iztapalapa",
    "La Magdalena Contreras",
    "Miguel Hidalgo",
    "Milpa Alta",
    "Tláhuac",
    "Tlalpan",
    "Venustiano Carranza",
    "Xochimilco"
]

delegación = form.selectbox(
    label="Delegación",
    options=delegaciones_cdmx,
    index=0)

form.write("Razones por las que estás desempleado")

# Se guarda True o False
vacantes = form.checkbox("No hay vacantes")
escolaridad = form.checkbox("Nivel de estudios")
experiencia = form.checkbox("Falta de experiencia")
discriminación = form.checkbox("Discriminación")

fecha = form.date_input(
    label="Fecha en la que ocurrió el incidente",
    min_value="1990-01-01",
    max_value="2030-12-31",
    value=date.today())

datos = form.toggle("¿Compartir tus datos?")

guardar = form.form_submit_button("Guardar")

if guardar:
    resultados_df = pd.read_csv("datos/resultados.csv")
    # "Nombre columna en archivo": nombre_variable
    nueva_fila = pd.DataFrame([{
        "Nombre": nombre,
        "Edad": edad,
        "Nivel de confianza": confianza,
        "Red social": red_social,
        "Delegación": delegación,
        "Vacantes": vacantes,
        "Escolaridad": escolaridad,
        "Experiencia": experiencia,
        "Discriminación": discriminación,
        "Fecha de incidente": fecha,
        "Compartir datos": datos
        }])
    resultados_df = pd.concat([resultados_df, nueva_fila],
                              ignore_index=True)
    resultados_df.to_csv("datos/resultados.csv",
                         index=False)
    form.success("¡Registro guardado!")






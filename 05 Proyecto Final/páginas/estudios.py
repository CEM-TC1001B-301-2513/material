import pandas as pd
import streamlit as st

@st.cache_data
def cargar_datos_csv(nombre):
    df = pd.read_csv(nombre)
    return df

@st.cache_data
def cargar_datos_excel(nombre):
    df = pd.read_excel(nombre)
    return df

trabajadores_df = cargar_datos_csv("datos/trab_norem_pib.csv")

st.title("Estudios consultados")

st.dataframe(trabajadores_df)
st.caption("Tomada de...")

st.bar_chart(trabajadores_df, x="fecha", y="prct_Total")

st.scatter_chart(trabajadores_df, x="prct_Hombres", y="prct_Mujeres")

st.line_chart(trabajadores_df, x="anio", y="prct_Total")

c1, c2, c3 = st.columns(3)
c1.metric("Aprobados", "30 alumnos", "6%")
c2.metric("Arriba de 90", "10 alumnos", "-3%")
c3.metric("Promedio", 85, 2)






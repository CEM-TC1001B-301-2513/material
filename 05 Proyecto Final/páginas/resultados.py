import pandas as pd
import streamlit as st

resultados_df = pd.read_csv("datos/resultados.csv")

st.title("Resultados del instrumento de medición")

st.dataframe(resultados_df)

st.write("Texto sobre la relevancia de sus datos")
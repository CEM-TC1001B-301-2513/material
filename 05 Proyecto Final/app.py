import streamlit as st

pages = [
    st.Page("páginas/introducción.py",
            title="Introducción a la problemática"),
    st.Page("páginas/adicionales.py",
            title="Recursos adicionales"),
    st.Page("páginas/estudios.py",
            title="Estudios consultados"),
    st.Page("páginas/formulario.py",
            title="Instrumento de medición"),
    st.Page("páginas/resultados.py",
            title="Resultados del instrumento"),
    st.Page("páginas/referencias.py",
            title="Referencias consultadas")
    ]
pg = st.navigation(pages)
pg.run()
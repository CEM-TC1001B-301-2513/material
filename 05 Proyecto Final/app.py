import streamlit as st

pages = [
    st.Page("páginas/introducción.py",
            title="Introducción a la problemática")
    ]
pg = st.navigation(pages)
pg.run()
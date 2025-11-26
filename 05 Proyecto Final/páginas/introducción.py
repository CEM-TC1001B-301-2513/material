import streamlit as st

st.title("Problemática a tratar")

st.write("""
# Encabezado (Introducción)
---
## Subencabezado
### Subsubencabezado

Esto es un párrafo de texto.Lorem ipsum dolor sit
amet, consectetur adipiscing elit. Fusce non
tempor magna. Nam euismod scelerisque massa ut
ultrices. Vivamus tristique suscipit elit, ac
semper nunc tristique sed. In porttitor
venenatis nisi, vel feugiat erat convallis vel.
Morbi faucibus neque tortor, eu dictum risus
bibendum lacinia. Ut molestie dapibus viverra.
Nam dictum eleifend magna ac dignissim.
Vestibulum facilisis elit lorem, vel mattis
felis accumsan sed. Ut eu elementum nisl.

In hac habitasse platea dictumst. Nullam aliquam neque vitae elit gravida, sit amet posuere tortor posuere. Etiam vitae efficitur nisi. Nulla facilisi. Nulla egestas viverra porta. Maecenas a malesuada ipsum. Fusce interdum risus sit amet ipsum suscipit ultrices. Maecenas sit amet pharetra sapien, mollis pretium nisi. Nulla ac enim enim.

### Listas ordenadas
1. Primer elemento
2. Segundo elemento
3. Tercer elemento

### Listas no ordenadas
- Primer elemento.
    - Primer subelemento.
- Segundo elemento.
- Tercer elemento.

### Decoraciones de texto
- Texto en *cursivas*.
- Texto en **negritas**.
- Texto en ***cursivas y negritas***.

### Colores en texto
- Texto en :blue[azul]
- Texto con :red-background[fondo rojo]
- Texto con :red-background[:blue[fondo rojo y texto azul]]

### Enlaces a sitios externos
- Enlace directo: https://experiencia21.tec.mx/courses/592670
- Agregar un enlace a un texto: [Curso TC1001B](https://experiencia21.tec.mx/courses/592670)

### Emojis y icónos
- Emoji :confused:
- Material icons :material/done_outline:

### Tablas

| Matrícula | Nombre |
| --- | --- |
| 8758686 | Juan Pérez |
| 7586986 | María Hernández |
| 9485832 | Pedro López |

### Latex
- En misma línea $\sum_{k=1}^{n}k^{2}-1$
- En su propia línea $$\sum_{k=1}^{n}k^{2}-1$$

""")

st.image("imágenes/pexels-andre-mouton-1207875.jpg")
st.caption("Obtenida de: https://www.pexels.com/photo/closeup-photo-of-primate-1207875/")

c1, c2 = st.columns(2)
c1.write("""In hac habitasse platea dictumst. Nullam aliquam neque vitae elit gravida, sit amet posuere tortor posuere. Etiam vitae efficitur nisi. Nulla facilisi. Nulla egestas viverra porta. Maecenas a malesuada ipsum. Fusce interdum risus sit amet ipsum suscipit ultrices. Maecenas sit amet pharetra sapien, mollis pretium nisi. Nulla ac enim enim.""")
c2.image("imágenes/pexels-andre-mouton-1207875.jpg")
c2.caption("Obtenida de: https://www.pexels.com/photo/closeup-photo-of-primate-1207875/")

c3, c4 = st.columns([0.3, 0.7])
c3.write("""In hac habitasse platea dictumst. Nullam aliquam neque vitae elit gravida, sit amet posuere tortor posuere. Etiam vitae efficitur nisi. Nulla facilisi. Nulla egestas viverra porta. Maecenas a malesuada ipsum. Fusce interdum risus sit amet ipsum suscipit ultrices. Maecenas sit amet pharetra sapien, mollis pretium nisi. Nulla ac enim enim.""")
c4.image("imágenes/pexels-andre-mouton-1207875.jpg")
c4.caption("Obtenida de: https://www.pexels.com/photo/closeup-photo-of-primate-1207875/")
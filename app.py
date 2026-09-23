import streamlit as st

st.title("Mi primera aplicación de Informática Médica")

st.write("¡La aplicación está funcionando correctamente!")

nombre = st.text_input("Escribe tu nombre:")

if nombre:
    st.success(f"Hola, {nombre}. Bienvenido a la aplicación.")

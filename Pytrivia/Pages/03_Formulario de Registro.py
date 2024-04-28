import streamlit as st

st.title("Formulario de Registro")

# Campos del formulario
with st.form("my_form"):
    username = st.text_input("Nombre de Usuario")
    full_name = st.text_input("Nombre Completo")
    email = st.text_input("Mail")
    birth_date = st.date_input("Fecha de Nacimiento")
    gender = st.selectbox("Género", ["Masculino", "Femenino", "Otro"])
    
    # Botón para enviar el formulario
    submitted = st.form_submit_button("Enviar")

    if submitted:
        st.success("Formulario enviado con éxito!")
        
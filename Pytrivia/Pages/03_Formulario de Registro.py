import streamlit as st
from datetime import date

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

    # Chequeo de que el usuario ingrese bien los datos
    if submitted:
        if not username or not full_name or not email:
            st.error ("Complete todos los campos para continuar.")
        elif not '@' in email or not '.com' in email:
            st.error ("Ingrese un email válido.")
        elif birth_date >= date.today():
            st.error ("Ingrese una fecha válida.")
        else:
            st.success("Formulario enviado con éxito!")
        
import streamlit as st
import csv
import pathlib

from datetime import date

def save_form_csv(username, full_name, email, birth_date, gender):
    path = pathlib.Path('Csv/datos_formularios.csv')
    EMAIL = 2

    try:
        with path.open(mode='r+', encoding='UTF-8', newline='') as file:
            reader = csv.reader(file)
            user = [username, full_name, email, birth_date, gender]

            next (reader)
            for row in reader:  # Ignora la primera fila que es la cabecera
                if row[EMAIL] == email:
                    row[:] = user  # Reemplaza todos los elementos de la fila con los nuevos datos
                    break
                else:
                      
                      # Agrega una nueva fila si el correo electrónico no existe

            # Escribe todo el contenido de nuevo al archivo
            file.seek(0)  # Regresa al inicio del archivo
            writer = csv.writer(file)
            writer.writerows(rows)

    except FileNotFoundError:
        st.error("No se encontró el archivo CSV.")

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
            st.error("Complete todos los campos para continuar.")
        elif not '@' in email or not '.com' in email:
            st.error("Ingrese un email válido.")
        elif birth_date >= date.today():
            st.error("Ingrese una fecha válida.")
        else:
            save_form_csv(username, full_name, email, birth_date, gender)
            st.success("Formulario enviado con éxito!")

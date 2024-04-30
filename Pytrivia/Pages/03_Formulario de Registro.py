import streamlit as st
import csv
import pathlib

from datetime import date


def save_form_csv(username, full_name, email, birth_date, gender):
    path = pathlib.Path('Csv/datos_formularios.csv')
    EMAIL = 2
    ok = False
    create_header = False

    # en variable ok se guarda si ya hay un usuario con ese mail
    with path.open(mode='r', encoding='UTF-8') as file:
        reader = csv.reader(file)

        # chequea si csv esta vacio para crear cabecera
        if path.stat().st_size == 0:
            create_header = True

        for line in reader:
            if line[EMAIL] == email:
                ok = True
                break
    
    # si ok es true se guardan todas las lineas en lines y se modifica la del usuario
    if ok:
        lines = []
        with path.open(mode='r', encoding='UTF-8') as file:
            reader = csv.reader(file)

            for line in reader:
                if line[EMAIL] == email:
                    line = [username, full_name, email, birth_date, gender]
                lines.append(line)

        # se escriben todas las lineas
        with path.open(mode='w', encoding='UTF-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(lines)
    else:
        # en caso de no estar se abre en modo A para agregar el usuario al final
        with path.open(mode='a', encoding='UTF-8', newline='') as file:
            writer = csv.writer(file)

            # se crea cabecera si esta vacio el csv
            if create_header:
                header = ['Usuario', 'Nombre completo', 'Email', 'Nacimiento','Genero']
                writer.writerow(header)

            writer.writerow([username, full_name, email, birth_date, gender])


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
            save_form_csv(username, full_name, email, birth_date, gender)
            st.success("Formulario enviado con éxito!")
            
        
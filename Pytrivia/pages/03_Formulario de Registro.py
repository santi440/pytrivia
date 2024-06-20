import streamlit as st
import pandas as pd
from datetime import date

def save_form_csv(username, full_name, email, birth_date, gender):
    path = 'csv/datos_formularios.csv'
    df = pd.read_csv(path)

    if email in df['Email'].values:
        df.loc[df['Email'] == email, ['Usuario', 'Nombre completo', 'Email', 'Nacimiento', 'Genero']] = [username, full_name, email, birth_date, gender]
    else:
        # Agregar una nueva fila al DataFrame
        new_row = {'Usuario': username, 'Nombre completo': full_name, 'Email': email, 'Nacimiento': birth_date, 'Genero': gender}
        df = df._append(new_row, ignore_index=True)

    df.to_csv(path, index=False)

# Configuración de la aplicación Streamlit
st.title("Formulario de Registro")

# Campos del formulario
with st.form("my_form"):
    username = st.text_input("Nombre de Usuario")
    full_name = st.text_input("Nombre Completo")
    email = st.text_input("Mail")
    birth_date = st.date_input("Fecha de Nacimiento", min_value=date(1900, 1, 1))
    gender = st.selectbox("Género", ["Masculino", "Femenino", "Otro"])
    
    # Botón para enviar el formulario
    submitted = st.form_submit_button("Enviar")

    # Validaciones del formulario
    if submitted:
        if not username or not full_name or not email:
            st.error("Complete todos los campos para continuar.")
        elif not '@' in email or not '.com' in email:
            st.error("Ingrese un email válido.")
        elif birth_date >= date.today():
            st.error("Ingrese una fecha válida.")
        else:
            save_form_csv(username, full_name, email, birth_date, gender)
            st.session_state.email= email
            st.session_state.user= username
            st.success("Formulario enviado con éxito!")
            
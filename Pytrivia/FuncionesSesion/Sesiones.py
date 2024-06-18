import streamlit as st
import pandas as pd
from pathlib import Path

df_user = Path('csv/datos_formularios.csv')
df_user = pd.read_csv(df_user)

def login_form():
    st.write("### Inicio de Sesión")
    usuario_seleccionado = st.selectbox("Selecciona tu usuario", options=df_user['Usuario'])
    if st.button("Iniciar Sesión"):
        # Obtener el email asociado al usuario seleccionado
        email = df_user.loc[df_user['Usuario'] == usuario_seleccionado, 'Email'].iloc[0]
        st.session_state.email = email
        st.success(f"¡Inicio de sesión exitoso como {usuario_seleccionado}!")

def get_logged_in_user():
    if 'email' in st.session_state:
        email = st.session_state.email
        user = df_user.loc[df_user['Email'] == email]
        return user
    else:
        return None
    
def is_user_logged_in():
    return 'email' in st.session_state
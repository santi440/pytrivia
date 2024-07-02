import streamlit as st
import pandas as pd
from pathlib import Path

df_user = Path('csv/datos_formularios.csv')
df_user = pd.read_csv(df_user)

def login_form():
    """
    Genera un selectbox para seleccionar el usuario con el cual se quiere inciar sesión y lo carga en el session_state
    """
    st.write("### Inicio de Sesión")
    usuario_seleccionado = st.selectbox("Selecciona tu usuario", options=df_user['Usuario'])
    if st.button("Iniciar Sesión"):
        try:
            # Obtener el email asociado al usuario seleccionado
            email = df_user.loc[df_user['Usuario'] == usuario_seleccionado, 'Email'].iloc[0]
            st.session_state.email = email
            st.session_state.user = usuario_seleccionado
            st.success(f"¡Inicio de sesión exitoso como {usuario_seleccionado}!")
            st.rerun()
        except IndexError:
            st.write("Si no tiene un usuario, debe registrarse.")
        
def get_logged_in_user():
    """
    Retorna el usuario que está cargado en el session_state, si no hay usuario cargado, retorna None
    """
    if 'email' in st.session_state:
        email = st.session_state.email
        user = df_user.loc[df_user['Email'] == email]
        return user
    else:
        return None
    
def is_user_logged_in():
    """
    Retorna true si el email es diferente de None en el session_state
    """
    if st.session_state.email != None:
        return True
    else:
        return False
    
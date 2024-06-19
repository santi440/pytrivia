# PyTrivia - Juego Educativo de Trivia

¡Bienvenido al repositorio del proyecto PyTrivia! Este es un juego educativo de trivia desarrollado como parte del trabajo integrador para el Seminario de Lenguajes-Python año 2024.

## Equipo de Desarrollo
- [Federico Kesselman 23786/4](https://gitlab.catedras.linti.unlp.edu.ar/kesselmanfederico)
- [Ignacio Battaglino 24595/3](https://gitlab.catedras.linti.unlp.edu.ar/battaglinoignacio)
- [Santiago Marcos 23345/0](https://gitlab.catedras.linti.unlp.edu.ar/santiago0105)
- [Bautista Rosli 23539/9](https://gitlab.catedras.linti.unlp.edu.ar/roslibautista05)

## Instrucciones de Ejecución

### Requisitos
Para ejecutar este proyecto, necesitará tener instalado Python en su sistema. Además, asegúrese de tener instalada las bibliotecas detalladas en requirements.txt o instalelas directamente desde su consala con el siguiente comando.

```bash
pip install -r requirements.txt
```
## Pasos para Ejecutar
- Clone este repositorio en su máquina local.
- Navegue hasta la carpeta del proyecto.
- Ejecute el siguiente comando en su terminal:

```bash
cd Pytrivia
streamlit run Inicio.py
```

Esto iniciará la aplicación Streamlit y podrá acceder al juego a través de su navegador web.

Además, para un análisis más exhaustivo podra pasar por los distintos archivos en formato Jupyter Notebook (.ipynb) y ejecutar los bloques de código que considere necesario o ,en la parte superior, el botón "Run All" que ejecutara todos en forma lineal.  

## Estructura de Directorios
- datasets: Contiene los conjuntos de datos originales.
- datasets_custom: Contiene los conjuntos de datos procesados.
- procesamiento: Contiene el Jupyter Notebook utilizados para el procesamiento y las funciones que se requieran para ello en la subcarpeta "funciones".
- consultas: Contiene los Jupyter Notebooks utilizados para el análisis de datos y las funciones que se requieran para ello en la subcarpeta "funciones".

- Pytrivia: Contiene el conjunto de archivos que componen la página web del juego. Organización:
    - Csv: Contiene los datasets con la información de los usuarios(datos_formularios) y de las jugadas(resultado).
    - FuncionesDatos: Archivos con las funciones para generar los gráficos en la página de Datos.
    - FuncionesEstadisticas: Archivos con las funciones para generar los gráficos / lógica de las opciones presentadas en Estadísticas.
    - FuncionesJuego: Archivos con las funciones para generar la lógica detrás del juego.
    - FuncionesSesion: Archivos con las funciones para crear y administrar las sesiones de los usuarios.
    - pages: Las diferentes páginas del sitio web, que utilizan todas las funciones explicadas anteriormente.
    - Inicio: La página principal del sitio. Aquella que da la introducción y que recibe a los usuarios.

- README.md: Este archivo que proporciona información sobre el proyecto y cómo ejecutarlo.
- LICENSE: Archivo que contiene la licencia del código.

## Funcionalidades Implementadas en la Primera Etapa
- Procesamiento de Datasets: Se realizaron operaciones de limpieza y transformación en los conjuntos de datos proporcionados.
- Interfaz Gráfica: Se ha desarrollado una interfaz gráfica utilizando Streamlit.
- Formulario de Registro: Se ha implementado un formulario de registro para que los usuarios puedan registrarse en el sistema.

## Funcionalidades Implementadas en la Segunda Etapa
- Pagina Inicio: Página de bienvenida con información del juego y su funcionamiento.
- Página Conociendo nuestros datos: Visualización de datos con gráficos y mapas basados en los datasets.
- Página de Juego: Juego de trivia con selección de usuario, temática y dificultad. Generación de preguntas aleatorias y cálculo de puntaje.
- Página Ranking: Visualización del ranking de mejores resultados y detalle de la partida jugada.
- Página Estadísticas sobre las jugadas: Visualización de estadísticas del juego y rendimiento de los usuarios.

¡Gracias por visitar nuestro repositorio! Si tiene alguna pregunta o sugerencia, no dude en comunicarse con nosotros. ¡Esperamos que disfruten del juego!
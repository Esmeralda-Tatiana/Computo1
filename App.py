import streamlit as st
from PIL import Image

import streamlit as st
from streamlit_option_menu import option_menu

def main():
  
    st.image(
          "https://upload.wikimedia.org/wikipedia/commons/3/3a/LOGO_UNSA.png",
            width=600, # Manually Adjust the width of the image as per requirement
        )
    st.markdown("# Trabajo de Investigación Formativa ") 
    st.sidebar.markdown("# PRESENTACIÓN")
    st.markdown("## Ingenierio Renzo Bolivar")
    st.markdown("![linea 1](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)")
    st.markdown("## Grupo B - N°4")
    st.markdown("### Autores:")
    st.markdown("* Esmeralda Tatiana Colque Apaza")
    st.markdown("* Maricielo Phoebe Valero Puma")
    st.markdown("* Edson Ciro Chiri Gonzales")
    st.markdown("* Marco Andree Valdivia Aragon")
    st.markdown("* Yeferson Gustavo Espinoza Turpo")
    st.markdown("* Saúl Paolo Valencia Solari")
    st.markdown("![linea 1](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)")
    st.markdown("## OBJETIVOS")
    st.markdown("""
Los Objetivos de la investigación formativa son:

- **Competencia Comunicativa** Presentación de sus resultados con lenguaje de programación Python utilizando los archivos Jupyter Notebook.
- **Competencia Aprendizaje**: con las aptitudes en **Descomposición** (desarticular el problema en pequeñas series de soluciones), **Reconocimiento de Patrones** (encontrar simulitud al momento de resolver problemas), **Abstracción** (omitir información relevante), **Algoritmos** (pasos para resolución de un problema).
- **Competencia de Trabajo en Equipo**: exige habilidades individuales y grupales orientadas a la cooperación, planificación, coordinación, asignación de tareas, cumplimiento de tareas y solución de conflictos en pro de un trabajo colectivo, utilizando los archivos Jupyter Notebook los cuales se sincronizan en el servidor Gitlab con comandos Git.
""")
if __name__ == '__main__':
    main()
  



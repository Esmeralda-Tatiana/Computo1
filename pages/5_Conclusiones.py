# Contents of ~/my_app/streamlit_app.py
import streamlit as st
from PIL import Image
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


    
st.markdown("![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)")
    
st.markdown("## CONCLUSIONES")
    
st.markdown("![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)")  
    
st.markdown("""
### ¿Se valido o no los resultados?
Si se llego a validar los resultados tanto con el programa pandas y con el algoritmo de correlación y se observó que para el coeficiente de correlación ambos procesos se realizan de manera confiable.
""")  

    
st.markdown("""
### ¿Es efectivo el metodo de correlación de pearson?
Sí, es efectivo porque el coeficiente de pearson cumple con lo siguiente.

Para llevar a cabo la correlación de Pearson es necesario cumplir lo siguiente:
- La escala de medida debe ser una escala de intervalo o relación.
- Las variables deben estar distribuida de forma aproximada
- La asociación debe ser lineal.
- No debe haber valores atípicos en los datos.

Ahora con el ejemplo que nuestro presente trabajo veremos si es efectivo 
En nuestra tabla de correlación vemos diferentes datos algunos “ < 0“que significa que las variables se relacionan inversamente si son “>0” quiere decir que las variables se correlacionan directamente y si es “=0” significa que no es posible determinar seria en nuestro caso un NA. Entonces si es efectivo el método de correlación de Pearson.
""")
st.markdown("""
### Correlación de Pearson y regresión lineal ¿Cuál es su relación?
La finalidad de la correlación es examinar la dirección y la fuerza de la asociación entre dos variables cuantitativas. Así conoceremos la intensidad de la relación entre ellas y si, al aumentar el valor de una variable, aumenta o disminuye el valor de la otra variable en cambio   la regresión lineal es una técnica de análisis de datos que predice el valor de datos desconocidos mediante el uso de otro valor de datos relacionado y conocido. Modela matemáticamente la variable desconocida o dependiente y la variable conocida o independiente como una ecuación lineal.
Su relación de ambos seria que los dos se basan en datos que puede ser conocido o no conocido para esto utilizan variables y nos dan a conocer una grafica de dispersión.
""")

    
st.markdown("![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)")
    
st.markdown("![linea 1](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)")
    
st.markdown("## REFERENCIAS")
    
st.markdown("""
- __Profesor de Matematicas__: `John Gabriel Muñoz Cruz`
https://www.linkedin.com/in/jgmc
- __Curso Pandas 04 Matriz Numpy a Dataframe Pandas__: `Moyete`https://www.youtube.com/watch?v=zWla02EaOtk
- __Lista a Numpy Array en Python__: `DelfStack`https://www.delftstack.com/es/howto/numpy/list-to-numpy-array-python/#:~:text=Las%20listas%20y%20los%20Arrays,utilizar%20para%20acceder%20a%20%C3%A9l.
- __Metodo df.fillna()__: `DelfStack`https://www.delftstack.com/es/howto/python-pandas/how-to-replace-all-the-nan-values-with-zeros-in-a-column-of-a-pandas-dataframe/#:~:text=fillna()%20para%20reemplazar%20todos%20los%20valores%20de%20NaN%20por%20ceros,-Reemplacemos%20los%20valores
- __Python - Nivel 24 - Reto 3 - Rellenar matriz__: `Manuel Gonzalez`https://www.youtube.com/watch?v=tq8XsNjkyec&list=WL&index=5&t=243s
- __Mayor y menor de matriz en Pyton__: `Parzybytes blog`https://parzibyte.me/blog/2020/11/27/mayor-menor-matriz-python/
- __Multilistas en Python:Listas de listas__: `Naps Tecnologia y educacion`https://naps.com.mx/blog/multilistas-en-python-listas-de-listas
- __Visualización de Datos con Python__: https://joserzapata.github.io/courses/python-ciencia-datos/visualizacion/
- __Mapa de calor en Python__: https://statologos.com/heatmap-python/#:~:text=Un%20mapa%20de%20calor%20es,heatmap%20
""")

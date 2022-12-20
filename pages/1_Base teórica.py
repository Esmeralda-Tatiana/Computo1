import streamlit as st
import streamlit as st
from PIL import Image
import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
    
# Contents of ~/my_app/streamlit_app.py
import streamlit as st
from PIL import Image
import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
 

st.markdown("# PYTHON - Inteligencia Artificial")
    
st.markdown("## Análisis de Correlación")
    
st.sidebar.markdown("# Base Teórica")
    
st.markdown("El análisis de correlación es el primer paso para construir modelos explicativos y predictivos más complejos.")
    
st.info(
"""
A menudo nos interesa observar y medir la relación entre 2 variables numéricas mediante el análisis de correlación. 
Se trata de una de las *técnicas más habituales en análisis de datos* y el primer paso necesario antes de construir cualquier modelo explicativo o predictivo más complejo.Para poder tener el  Datset hay que recolectar información a travez de encuentas.
"""
)
    
st.markdown("### ¿Qué es la correlación?")
    
st.markdown("""
La correlación es un tipo de asociación entre dos variables numéricas, específicamente evalúa la **tendencia (creciente o decreciente) en los datos**.
Dos variables están asociadas cuando una variable nos da información acerca de la otra. Por el contrario, cuando no existe asociación, el aumento o disminución de una variable no nos dice nada sobre el comportamiento de la otra variable.
Dos variables ***se correlacionan cuando muestran una tendencia creciente o decreciente***.
""")
    
st.markdown("### ¿Cómo se mide la correlación?")  
    
st.markdown("Tenemos el coeficiente de **correlación lineal de Pearson** que se *sirve para cuantificar tendencias lineales*, y el **coeficiente de correlación de Spearman** que se utiliza para *tendencias de aumento o disminución, no necesariamente lineales pero sí monótonas*. ") 
    
st.markdown("## Correlación de Pearson")
    
st.info("El coeficiente de correlación lineal de Pearson mide una tendencia lineal entre dos variables numéricas.")
    
st.markdown("""
Es el método de correlación más utilizado, pero asume que:

 - La tendencia debe ser de tipo lineal.
 - No existen valores atípicos (outliers).
 - Las variables deben ser numéricas.
 - Tenemos suficientes datos (algunos autores recomiendan tener más de 30 puntos u observaciones).

Los dos primeros supuestos se pueden evaluar simplemente con un diagrama de dispersión, mientras que para los últimos basta con mirar los datos y evaluar el diseño que tenemos.
""")
    
st.markdown("### Cómo se interpreta la correlación")
    
st.markdown("""
El signo nos indica la dirección de la relación, como hemos visto en el diagrama de dispersión.
 - un valor positivo indica una relación directa o positiva,
 - un valor negativo indica relación indirecta, inversa o negativa,
 - un valor nulo indica que no existe una tendencia entre ambas variables (puede ocurrir que no exista relación o que la relación sea más compleja que una tendencia, por ejemplo, una relación en forma de U).
""")
    
st.markdown("""
La magnitud nos indica la fuerza de la relación, y toma valores entre $-1$ a $1$. Cuanto más cercano sea el valor a los extremos del intervalo ($1$ o $-1$) más fuerte será la tendencia de las variables, o será menor la dispersión que existe en los puntos alrededor de dicha tendencia. Cuanto más cerca del cero esté el coeficiente de correlación, más débil será la tendencia, es decir, habrá más dispersión en la nube de puntos.
 - si la correlación vale $1$ o $-1$ diremos que la correlación es “perfecta”,
 - si la correlación vale $0$ diremos que las variables no están correlacionadas.
""")

    
st.image(
            "https://user-images.githubusercontent.com/25250496/204172549-2ccf3be3-a2b3-4b49-9cd4-adb66e28621d.png",
            width=750, # Manually Adjust the width of the image as per requirement
        )
    
st.markdown("""
##### Fórmula Coeficiente de Correlación de Pearson
""")
    
st.image(
            "https://media.geeksforgeeks.org/wp-content/uploads/20200311233526/formula6.png",
            width=600, # Manually Adjust the width of the image as per requirement
        )
   
st.markdown("**Regresión Lineal**: La regresión lineal se usa para encontrar una __`relación lineal entre el objetivo y uno o más predictores`__.")
    
    
st.image(
         "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Linear_regression.svg/1200px-Linear_regression.svg.png",
            width=600, # Manually Adjust the width of the image as per requirement
        )
    
st.markdown("### Propiedades")
    
st.markdown("""
**1. ADIMENSIONALIDAD:** Al dividir la suma de cuadrados del producto XY entre las raíces individuales de las sumas de cuadrados de X y Y, se obtiene un índice sin dimensiones que se origina cuando las unidades del numerador se cancelan con las del denominador. Esta propiedad representa una ventaja esencial que hace de este coeficiente una medida versátil y fácilmente interpretable.
""")
    
st.markdown("""
**2. RANGO DEFINIDO ENTRE -1 y 1:** El coeficiente puede entenderse como el coseno del ángulo formado por los vectores asociados a X y Y. Cuando el ángulo es cercano a 0, el coseno tiende a 1, las variables poseen alta proximidad en el espacio. Cuando el ángulo es aproximadamente igual a 180, el coseno será igual a -1 e indicará que las variables siguen exhibiendo una elevada cercanía, pero en direcciones opuestas. En cambio, cuando el ángulo entre los vectores es de 90 grados o similar, el coseno tenderá a 0 y las variables son ortogonales, en consecuencia, no están relacionadas linealmente.
""")
    
st.markdown("""
**3. RELACIÓN LINEAL:** Esta propiedad es una de las más importantes y tal vez sea en la que más errores de interpretación se comenten. Es fundamental distinguir que lo que mide el coeficiente de Pearson es la fuerza y la dirección de la relación lineal entre las variables. 
""")
    
st.markdown("**4. SIMETRÍA:** La simetría en este caso establece que, sin importar si se intercambian las posiciones de X y Y, el resultado del coeficiente será el mismo.")
    
st.markdown("**5. INDEPENDENCIA CON RESPECTO AL ORIGEN:** El valor una vez ha sido calculado, no cambiará a pesar de que se modifique el origen o la escala de los datos; es decir, el coeficiente no se ve afectado por aquellas transformaciones lineales que se apliquen a las variables.")

    
st.markdown("### Suposiciones Vinculadas Al Uso Del Coeficiente De Pearson")
   
st.markdown("El uso adecuado de este coeficiente debe sustentarse en el cumplimiento de las siguientes premisas:")
    
st.markdown("**1. Nivel de medición de las variables:** Las dos variables deben ser de intervalo o de razón, aunque no es necesario que ambas tengan el mismo nivel de medición.")
    
st.markdown("**2. Datos pareados:** Para que el cálculo de esta medida pueda realizarse, se necesitará que los casos en cuestión tengan datos en cada variable. Si hay valores perdidos, estos registros se descartarán por completo del análisis.")
   
    
st.markdown("**4. Ausencia de datos atípicos a nivel bivariado:** Tal y como sucede con el supuesto anterior, la conjetura relacionada con la presencia de datos atípicos a nivel multivariado suele ser malinterpretada y verificada erróneamente.")
    
st.markdown("**5. Linealidad:** Sobre esta propiedad ya se han suministrado suficientes elementos teóricos en esta revisión,de manera que solo se recordará en este punto que lo único que mide el coeficiente de Pearson es la fuerza y la dirección de la relación lineal entre dos variables. Ahora bien, sí se mencionará que la forma más idónea y más empleada de constatar si esta suposición se cumple o no, es a través de los diagramas de dispersión.")




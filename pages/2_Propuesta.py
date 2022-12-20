# Contents of ~/my_app/streamlit_app.py
import streamlit as st
from PIL import Image
import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt   


st.sidebar.markdown("# Propuesta")
    
st.title(" Aplicación en IA Sistema Recomendador")  # add a title
    
st.subheader("El Sistema recomendador deberá encontrar la compatibilidad o similitud entre un grupo de personas encuestadas, en el área de:")
    
st.markdown("#### - Comida  :ramen:")
    
st.markdown("### DATASET")
    
st.info("Para tener un Dataset se recolectó datos mediante una encuesta")
    
df = pd.read_csv("./Data/Comida.csv") 
    
st.write(df)
    
st.markdown("![linea 1](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)")
    
st.markdown("### Correlación de similitud")
    
st.info("El __coeficiente de correlación de Pearson__ es una medida de __`dependencia lineal entre dos variables aleatorias cuantitativas`__. ") 
    
data = pd.read_csv("./Data/Comida.csv")
    
n = data[data.columns[1:]].to_numpy()
    
m = data[data.columns[0]].to_numpy()
    
st.write(n)
    
st.write(m)
    
st.markdown("![linea 1](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)")
    
st.markdown("### Sustitución de Valor NaN")
    
st.info("Para esta parte se usó el método fillna que permite sustituir los valores nulos de una estructura pandas por otro valor según ciertos criterios: pueden sustituirse por un valor concreto o bien puede utilizarse el anterior o posterior valor no nulo (en el caso de los dataframes habrá que especificar el eje sobre el que queremos aplicar la función). De esta manera se logró sacar la correlación de pandas en una tabla sin valores NAN")

    
df=pd.DataFrame(data)
df=df.fillna(-1)
n = df[df.columns[1:]].to_numpy()
m = df[df.columns[0]].to_numpy()
filas = len(n[:,1])
columnas = len(n[1,:])
matriz = []
for i in range(filas):
    matriz.append([])
    valor = max(n[i])
    matriz[i].append(valor)
print(matriz)
l = len(matriz)
for i in range(filas):
    for j in range(columnas):
        if n[i][j] == -1:
            n[i][j] = matriz[i][0]
        else:
            continue
matriz2 = np.asarray(n)
matriz3 = np.array(matriz2)
df = pd.DataFrame(matriz3,m)
df

    
st.write(df)

    
st.markdown("![linea 1](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)")
    
st.markdown("## 3.- Correlación en Pandas")
    
   
 
n = df[df.columns[1:]].to_numpy()
   
n.T
df = pd.DataFrame(matriz3.T, columns = m)
    

m_corr = df.corr()

datitos= m_corr[m_corr.columns[0:]].to_numpy()
    
m_corr_d = np.round(m_corr,decimals = 4)  
st.write(m_corr_d)


    
st.markdown("![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)")
    
st.markdown("## 4.- Matrix de Correlación")
    
st.info(" Aquí se realiza un algoritmo utilizando los valores de la tabla anterior (libre de valores NAN) para esto")
    
df=pd.DataFrame(data)
df=df.fillna(-1)
n = df[df.columns[1:]].to_numpy()
m = df[df.columns[0]].to_numpy()
filas = len(n[:,1])
columnas = len(n[1,:])
matriz = []
for i in range(filas):
    matriz.append([])
    valor = max(n[i])
    matriz[i].append(valor)
print(matriz)
l = len(matriz)
for i in range(filas):
    for j in range(columnas):
        if n[i][j] == -1:
            n[i][j] = matriz[i][0]
        else:
            continue
matriz2 = np.asarray(n)
matriz3 = np.array(matriz2)
df = pd.DataFrame(matriz3,m)
df

    
st.write(df)

f, c = matriz3.shape
def entero(numero):
        try:
            int(numero)
            return True
        except:
            return False
def revision(User1, User2):
        vacios = np.empty((0, 0), int)
        for i in range(0, c):
            if (entero(User1[i])):
                    vacios = vacios
            else:
                vacios = np.append(vacios, i)

        for i in range(0, c):
            if (entero(User2[i])):
                vacios = vacios
            else:
                vacios = np.append(vacios, i)

        return np.unique(np.sort(vacios))
def distancias(Base):
         f, c = matriz3.shape
         mat = np.identity(f)
         for i in range(0, f):
             for j in range(0, f):
                 U1 = Base[i]
                 U2 = Base[j]
                 V = revision(U1, U2)
                 U1 = np.delete(U1, V)
                 U2 = np.delete(U2, V)

                 mat[i, j] = correlacion(U1, U2)
         return mat
    ##  << ---  VALIDACIÓN  --- >>##
def correlacion(X1, X2):

        X1M = np.mean(X1)
        X2M = np.mean(X2)
            
        n1 = X1 - X1M
        n2 = X2 - X2M
        rn = sum(np.multiply(n1, n2))
            
        d1 = sum(np.square(n1))
        d2 = sum(np.square(n2))
        rd = np.sqrt(d1*d2)
        corr = rn/rd

        return corr
Final = pd.DataFrame()
Similitudes = distancias(n)
Final[""] = m
for i in range(0, f):
       Final[m[i]] = Similitudes[i]
Final

st.write(Final)

st.markdown("![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)")
st.markdown("## Gráfica de Calor")
     
plt.figure(figsize = (25,15))
mapa1 = sns.heatmap (m_corr)
figure = mapa1.get_figure()
figure.savefig('mapa1.png', dpi=600 )
st.success("Matriz de correlación en Pandas")
st.write(figure)
        
plt.figure(figsize = (25,15))
mapa2 = sns.heatmap (m_corr)
figure = mapa2.get_figure()
figure.savefig('mapa2.png', dpi=600 )
st.success("Matriz de la correlación realizada")
st.write(figure)

st.markdown("![linea 1](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)")



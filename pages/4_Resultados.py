import streamlit as st
from PIL import Image
import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("./Data/Comida.csv")
    
    
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

 

df = pd.DataFrame(matriz3.T, columns = m)
    

m_corr = df.corr()

datitos= m_corr[m_corr.columns[0:]].to_numpy()
    
m_corr_d = np.round(m_corr,decimals = 4)  



st.markdown("## RESULTADOS")

mayor=0
for fila in datitos:
    for valor in fila:
        if valor == 1:
            continue
        if float(valor) < 1:
            if valor > mayor:
                mayor = valor
                k = fila
for y in range(0,45):
    if k[y]==1:
        t=y
    if k[y]== mayor:
        u=y  
      
mayor2=0
for fila in datitos:
    for valor in fila:
        if valor == 1:
            continue
        if float(valor) < 1:
            if valor > mayor2 and valor < mayor:
                mayor2 = valor
                kk = fila
for y in range(0,45):
    if kk[y]==1:
        tt=y
    if kk[y]== mayor2:
        uu=y
print("1.-",m[t],"y",m[u],"obtienen el PRIMER indice mas alto de similitud con",mayor)

print("2.-",m[tt],"y",m[uu],"obtienen el SEGUNDO indice mas alto de similitud con",mayor2) 

st.write("1.-",m[t],"y",m[u],"obtienen el PRIMER indice mas alto de similitud con",mayor)
st.write("2.-",m[tt],"y",m[uu],"obtienen el SEGUNDO indice mas alto de similitud con",mayor2)

st.markdown("![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)")
st.markdown("## Validación de resultados")
st.markdown("![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)")
st.markdown("### - Validación - Matrix de Correlación Pandas")
st.markdown(" Se debe llenar la tabla de __VALIDACIÓN de la Matriz de Correlación__ con los valores de `Similitud` obtenidos.En `NUMPY` a partir de las matrices `n` y `m` con funciones.")
 
st.code("""
    mayor=0
    for fila in datitos:
        for valor in fila:
            if valor == 1:
                continue
            if float(valor) < 1:
                if valor > mayor:
                    mayor = valor
                    k = fila
    for y in range(0,45):
        if k[y]==1:
            t=y
        if k[y]== mayor:
            u=y        
    mayor2=0
    for fila in datitos:
        for valor in fila:
            if valor == 1:
                continue
            if float(valor) < 1:
                if valor > mayor2 and valor < mayor:
                    mayor2 = valor
                    kk = fila
    for y in range(0,45):
        if kk[y]==1:
            tt=y
        if kk[y]== mayor2:
            uu=y
    print("1.-",m[t],"y",m[u],"obtienen el PRIMER indice mas alto de similitud con",mayor)

    print("2.-",m[tt],"y",m[uu],"obtienen el SEGUNDO indice mas alto de similitud con",mayor2) )""", language='python')
    
st.markdown("""
#### Correo y puntaje de los dos valores más altos en la correlación:
""")
st.markdown("""
1.- oliverajefferson162@gmail.com y jesusparedes199817@gmail.com obtienen el PRIMER indice mas alto de similitud con 0.793061400652281


2.- dfghj@gmail.com y mati_tujuguete@hotmail.com obtienen el SEGUNDO indice mas alto de similitud con 0.7084946245324483
""")
    
 
st.markdown("### - Validación - Matrix de Correlación realizada")

st.code("""
    mayor=0
    for fila in valores2:
        for valor in fila:
            if valor == 1:
                continue
            if float(valor) < 1:
                if valor > mayor:
                    mayor = valor
                    k = fila
    for y in range(0,45):
        if k[y]==1:
            t=y
        if k[y]== mayor:
            u=y        
    mayor2=0
    for fila in valores2:
        for valor in fila:
            if valor == 1:
                continue
            if float(valor) < 1:
                if valor > mayor2 and valor < mayor:
                    mayor2 = valor
                    kk = fila
    for y in range(0,45):
        if kk[y]==1:
            tt=y
        if kk[y]== mayor2:
            uu=y
    print("1.-",m[t],"y",m[u],"obtienen el PRIMER indice mas alto de similitud con",mayor)
    print("2.-",m[tt],"y",m[uu],"obtienen el SEGUNDO indice mas alto de similitud con",mayor2)""",language='python')
    
st.markdown("""
#### Correo y puntaje de los dos valores más altos en la correlación:
""")
st.markdown("""

1.- oliverajefferson162@gmail.com y jesusparedes199817@gmail.com obtienen el PRIMER indice mas alto de similitud con 0.793061400652281


2.- dfghj@gmail.com y mati_tujuguete@hotmail.com obtienen el SEGUNDO indice mas alto de similitud con 0.7084946245324483

""")

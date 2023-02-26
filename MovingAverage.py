'''
Jesús Rosales Santana
17-02-2023
ETL con Pandas de fichero CSV de los valoresde las "Big Fives".
1) Predecir próximo precio en base a la DataBase.
'''
import pandas as pd
import numpy as np 


df = pd.read_csv('bigfivedata.csv')#Con este comando llamo el DataSet.
mediamovilrapida = 0.0
mediamovillenta = 0.0
df['MVR'] = mediamovilrapida #mediamovilrapida
df['MVL'] = mediamovillenta #mediamovillenta
df = df.drop(df.index[df.name == "^IXIC"])#Con este elimino todos los datos que contengan "^IXIC", pues estos no me interesan.
df = df.reset_index(drop= True)#Con esto reseteare el indice, para futuros usos.
print(df)

def mediasMoviles(df):#Con esta fumción se crean las medias moviles.
  mvr = df['close']#Aquí elijo la columna desde donde se sacará el calculo de la Media Movil Rapida.
  mvl = df['close']#Aquí elijo la columna desde donde se sacará el calculo de la Media movil Lenta.
  df['MVR'] = mvr.rolling(12).mean()#Con esto se hace el calculo.
  df['MVL'] = mvl.rolling(25).mean()#Con esto se hace el calculo.
  return df
  
mediasMoviles(df)#Aquí llamo a la función.
df
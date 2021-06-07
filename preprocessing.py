#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 21:16:17 2021

@author: lucas
"""

import  pandas as pd

Data_Set1 = pd.read_csv('Data_Set1.csv')
#seleccionar header
Data_Set2= pd.read_csv('Data_Set1.csv',header=2)
#renombrar columa
Data_Set3 = Data_Set2.rename(columns = {'Temperature':"Temp"})
#remover columna : axis=1 indica eje columna
Data_Set4 = Data_Set3.drop('No. Occupants',axis=1)
#inplace modifica el DataSet original
Data_Set3.drop('No. Occupants',axis=1,inplace= True)
#remover columna : axis=0 indica eje fila
Data_Set4 = Data_Set3.drop(2,axis=0)
#actualizar indice desp de borrar fila
Data_Set5 = Data_Set4.reset_index(drop= True);

Data_Set5.describe()

#buscar minimo de una columna
Min_item = Data_Set5['E_Heat'].min()
#en el dataset, filtrar en la col E_Heat el valor que es igual al min
Data_Set5['E_Heat'][Data_Set5['E_Heat']==Min_item]
#buscamos esa fila mediante el resultado
Data_Set5.iloc[16]
 
#reemplazar el valor - inplace cambiar el DS original
Data_Set5['E_Heat'].replace(-4,21,inplace=True)
#chequeamos el reemplazo
Data_Set5.iloc[16]


#Covariance
Data_Set5.cov()

##mapa de calor
import seaborn as sns
sns.heatmap(Data_Set5.corr())

Data_Set6=Data_Set5
"""
Missing Values
"""

Data_Set6.info()

import numpy as np
#reemplazar valor
Data_Set7= Data_Set6.replace('!',np.NaN)
Data_Set7.info()
#convertir a numeric
Data_Set7=Data_Set7.apply(pd.to_numeric)
Data_Set7.isnull()
#borrar fila - nan
Data_Set7.drop(13,axis=0,inplace=True)
Data_Set7.dropna(axis=0,inplace=True)
Data_Set7 = Data_Set7.reset_index(drop= True);

#Reemplazar nan con otro valor del DataSet (ffill : siguiente valor - bfill: valor previo)
Data_Set8 = Data_Set7.fillna(method='ffill')

"""
Reemplazar valor faltante con el promedio de una fila por ejemplo

"""
#usamos scikit para obtener la media del dataset
from sklearn.impute import SimpleImputer
M_var= SimpleImputer(missing_values=np.nan,strategy='mean')
#asociamos al dataset
M_var.fit(Data_Set7)
Data_Set9= M_var.transform(Data_Set7)


"""
Outlier detection: outlier es un valor inusual fuera del rango normal de los demas valores
Lo podemos observar como un valor alejado del min/max del boxplot
"""
Data_Set8.boxplot()
#necesitamos los cuantiles para calcular los limites del outlier value
Q25=Data_Set8['E_Plug'].quantile(0.25)
Q75=Data_Set8['E_Plug'].quantile(0.75)
#IQR = Q3 - Q1 (diferencia entre Q3 y Q1)  
iqr=Q75-Q25

###  Mild Outlier ###
#lower Bound = Q25 - 1.5 * IQR
mild_lower=Q25-1.5*iqr
#upper Bound = Q75 + 1.5 * IQR
mild_upper=Q75+1.5*iqr


###  Extreme Outlier ###
#lower Bound = Q25 - 3 * IQR
extr_lower=Q25-3*iqr
#upper Bound = Q75 + 3 * IQR
extr_upper=Q75+3*iqr

#reemplazar el outlier value en el data set
Data_Set8['E_Plug'].replace(120,42,inplace=True)


"""
DATA SET CONCATENATION

"""

New_Col = pd.read_csv('Data_New.csv')
Data_Set10 = pd.concat([Data_Set8,New_Col],axis=1)
Data_Set10.info()
#Quitar valores dummies -valores de texto cualitativo no entendible por la pc
Data_Set11= pd.get_dummies(Data_Set10)
Data_Set11.info()
Data_Set11.dropna(axis=0,inplace=True)
Data_Set11 = Data_Set11.reset_index(drop= True);

##q25= 17/2= 8.5
#q75= 47/2 = 23.5
#iqr=23.5 - 8.5
#23.5 - 8.5
##Upper mild =23.5 + 1.5* 15 


"""

Normalization

"""

from sklearn.preprocessing import minmax_scale, normalize
#min max scale normalization: cambiar al rango entre 0,1
Data_Set12 = minmax_scale(Data_Set11,feature_range=(0,1))
#normalizacion euclidean L2 : devuelve una matriz
Data_Set13 = normalize(Data_Set11,norm='l2',axis=0)
Data_Set14 = normalize(Data_Set11,norm='l2',axis=1)
#convertimos el array obtenido a un DataFrame, normalizado
Data_Set13 = pd.DataFrame(Data_Set13, columns=['Time','E_Plug','E_Head','Price','Temp','OffPeak','Peak'])



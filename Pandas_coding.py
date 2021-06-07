#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 23:11:24 2021

@author: lucas
"""

"""
 Series : used to work with series (labeled arrays) and data frames (2D labeled arrays)
""" 

import pandas as pd

"""
Series

"""

Age = pd.Series([10,29,30,40],index=['age1',"age2",'age3',"age4"])

#acceder a un valor
Age.age3
#obtener valores
Age.values
#obtener indices
Age.index

#filtrar de Age los mayores que 20
Filtered_Age=Age[Age>20]

#cambiar indices
Age.index = ['A1',"A2","A3",'A4']

"""
DataFrames : 2D labeled arrays
"""
import numpy as np
Data_Fra = np.array([[20,10,8],[25,8,10],[27,5,3],[30,9,7]])
Data_set = pd.DataFrame(Data_Fra,index=['S1',"S2","S3",'S4'],columns=['Age','Grade1',"Grade2"])
#agregar datos  de una columa 
Data_set['Grade3']=[12,14,17,9]

#locate data (row/column)from label 
S1=Data_set.loc['S1']
S1_grade3a=Data_set.loc['S1']['Grade3']
#ubicar por indices numericos
S1_grade3=Data_set.iloc[0][3]
#obtener filas/columas con iloc
#1er param filas, (usando ':' tengo todas las filas), 2do param colum (usando ':' tengo todas las columnas)
Data_set.iloc[:,0]
Data_set.iloc[1,:]
#filtrar only columns  1 to 2
Filtered_Data_set= Data_set.iloc[:,1:2]

#remover columna/fila por label (axis:1=vertical column - axis:0=horizontal row)
Data_Set_rem=Data_set.drop('Grade1',axis=1)
#replace values
Data_set_replaced=Data_set.replace(10,100)
#replace several numbers - using dictionary
Data_set_replaced1=Data_set.replace({27:270,30:300})
#first rows - check data
Data_set.head(3)
#last rows - check data
Data_set.tail(3)
#sort values
Data_set.sort_values('Age',axis=0,ascending=False)
Data_set.sort_index(axis=0,ascending=False)
#read from csv
Data_CSV=pd.read_csv('Data_Set.csv')











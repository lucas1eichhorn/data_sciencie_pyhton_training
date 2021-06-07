#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 20:43:00 2021


Pracica numpy
"""

import numpy as np

Nump_arr=np.array([[1,2,3],[4,5,7]])

np1=np.array([[1,2],[4,5]])
np2=np.array([[3,4],[5,6]])
#multiplicacion matricial - producto punto - 
np3=np1@np2
np5=np.dot(np1,np2)

#multiplicacion comun
np4=np1*np2
np6=np.multiply(np1,np2)

#suma
Sum1=np1+np2

#Resta
Res1=np1-np2
Res2=np.subtract(np1,np2)

#sumar elementos - obtener un escalar
El_sum=np.sum(np1)

#inrementar elementos + numero
sum_num=np1+3

#sumar matrix y array
np2arr=np.array([[8,9]])
sum_mat_arr=np2+np2arr

#dividir - resultados float
Div=np.divide([12,14,16],5)
#diividir - resultado enteros
Div_ent=np.floor_divide([12,14,16],5)

Sq=np.math.sqrt(10)

#distribuciones normal
ndis=np.random.standard_normal((3,4))

#distribuciones uniforme
udis=np.random.uniform(1,12,(3,4))
#generar distribuciones float
b_float_dis=np.random.rand(1,5)

#generar distribuciones int
b_int_dis=np.random.randint(10,50,(2,5))

#zeros array
za=np.zeros((3,5))

#ones array
ones=np.ones((3,5))

#filtrar array (solo true/false)
Filter_arr=np.logical_and(b_int_dis>30,b_int_dis<50)
#obtenemos lo numeros filtrados - join con el array anterior
Filter_number_array=b_int_dis[Filter_arr]

"Estadistica"
#creamos array
Data_N=np.array([1,3,4,5,7,9]) 
# promedio de valores en el array - mean
Media_N=np.mean(Data_N)
#mediana (par:promedio entre los 2 valores del medio - impar:valor del medio)
Median_N=np.median(Data_N)
#varianza
Varianza_N=np.var(Data_N)
#desviacion standard
des_stand_N=np.std(Data_N)
#varianza en matrices - varianza calculada por columa=0/fila=1
Var_num=np.var(Nump_arr,axis=0)



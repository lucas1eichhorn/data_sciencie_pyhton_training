#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Supervised Learning Classification
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()

iris.feature_names

Data_iris = iris.data
#creamos el data set con las columnas
Data_iris = pd.DataFrame(Data_iris, columns= iris.feature_names)
#agregamos la columna label
Data_iris['label']=iris.target

#dibujar diagrama puntos: ancho y larga de petalos
#Data_iris.iloc[:,2] -> todas las filas y columna 2
plt.scatter(Data_iris.iloc[:,2],Data_iris.iloc[:,3],c=iris.target)
plt.xlabel('Petal length (cm)')
plt.ylabel('Petal width (cm)')
plt.show()

#separamos info -Z x:data y:labels
x = Data_iris.iloc[:,0:4]
y = Data_iris.iloc[:,4]

"""
K-NN Classifier
"""

#definimos el clasificador
from sklearn.neighbors import KNeighborsClassifier
#metric: distance metric-> P: 2 Euclidean, 1: Manhattan
KNN = KNeighborsClassifier(n_neighbors=6,metric='minkowski',p=1)

#lo aplicamos a los datos seleccionados del modelo que entrena al algoritmo KNN
KNN.fit(x,y)
###
#probamos el algoritmo con una muestra para predecir
#determina que tipo de flor es en base a las medidas con que entrenamos al modelo
###
#muestra
x_N= np.array([[5.6,3.4,1.4,0.1]])
#precidmos con el modelo KNN el tipo de la muestra: devuelve label array[0] as setosa
KNN.predict(x_N)
iris.target_names[KNN.predict(x_N)]
#muestra 2: 
x_N2= np.array([[7.5,4,5.5,2]])
#el modelo devuelve label array[2] as virginica
KNN.predict(x_N2)
iris.target_names[KNN.predict(x_N2)]

"""
Testear modelo con sklearn: 80% de los datos para entrenar 20% para testear
"""

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(x,y,test_size= 0.2,train_size=0.8,
                                                    random_state=88,shuffle= True,
                                                    stratify=y)

#definimos el clasificador
from sklearn.neighbors import KNeighborsClassifier
#metric: distance metric-> P: 2 Euclidean, 1: Manhattan
KNN = KNeighborsClassifier(n_neighbors=5,metric='minkowski',p=1)

# aplicamos a los datos de entrenamiento al algoritmo KNN (80% de muestras para entrenar)
KNN.fit(X_train,Y_train)
#testeamos el modelo con el 20% de las muestras restantes. debe predecir Y_test
predicted_type=KNN.predict(X_test)
#medimos las metricas de precision de nuestro modelo

from sklearn.metrics import accuracy_score
#comparamos los resultados reales (Y_test) contra los predecidos por el modelo 
accuracy_score(Y_test,predicted_type)

"""
Decision Tree
"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

Dt = DecisionTreeClassifier()
Dt.fit(X_train,Y_train)
predicted_type_Dt = Dt.predict(X_test)
accuracy_score(Y_test,predicted_type_Dt)
#cross validation, interarcala las muestras test/entrenamiento en distintas iteraciones
#para usar todo el data set
from sklearn.model_selection import cross_val_score
#array de precisiones del algoritmos con distintas muestras de test, 
#la precision final será el promedio de todas las preciones del array
Scores_Dt = cross_val_score(Dt,x,y,cv = 10)









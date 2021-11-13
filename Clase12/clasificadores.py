# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 15:46:58 2021

@author: qagustina
"""
# 12.4: Algoritmos de clasificación supervisada
# 12.12
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier


iris_dataset = load_iris()


for k in range(100):
    
    # Partición del conjunto original en test y train aleatoriamente (sin fijar la semilla).
    X_train, X_test, y_train, y_test = train_test_split(
        iris_dataset['data'], iris_dataset['target']) 
    
    # Entrenamiento de ambos modelos (knn y clf) con el conjunto train resultante.
    # KNeighborsClassifier
    knn = KNeighborsClassifier(n_neighbors = 1)
    knn.fit(X_train, y_train)
    
    # DecisionTreeClassifier
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)
      
    X_new = np.array([[5, 2.9, 1, 0.2]])
    
    prediction = knn.predict(X_new)
    y_pred = knn.predict(X_test)
    
    prediction = clf.predict(X_new)
    y_pred_c = clf.predict(X_test)
    
    # Evaluación de ambos clasifcadores (score) con el conjunto test resultante.
    score_clf = round(clf.score(X_test, y_test), ndigits=2)  
    score_knn = round(knn.score(X_test, y_test), ndigits=2)
    # print(score_knn)
    # print(score_clf)
print("Promedio KNeighborsClassifier: {:.2f}".format(np.mean(y_pred == y_test)))
print("Promedio DecisionTreeClassifier: {:.2f}".format(np.mean(y_pred_c == y_test)))
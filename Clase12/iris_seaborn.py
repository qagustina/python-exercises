# 12.10
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris


iris_dataset = load_iris()

# creamos un dataframe de los datos de flores
# etiquetamos las columnas usando las cadenas de iris_dataset.feature_names
iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names)
# agrego al DataFrame el atributo target
iris_dataframe['target'] = iris_dataset['target']
# reemplazo valores por nombres
iris_dataframe['target'].replace([0], 'Setosa', inplace=True)
iris_dataframe['target'].replace([1], 'Versicolor', inplace=True)
iris_dataframe['target'].replace([2], 'Virginica', inplace=True)

sns.pairplot(iris_dataframe, hue="target")
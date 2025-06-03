from src.Linear_models.Classification.Binary.visual import visual
from src.Linear_models.Classification.Binary.Iris_dataset import data_linear
import matplotlib.pyplot as plt
import pandas as pd


data = data_linear()
df = data.data()
# print(df.head())
print(df['target'].value_counts())
v = visual(df['sepal length (cm)'] , df['sepal width (cm)'] , df['petal length (cm)'] , df['petal width (cm)'] , df['target'])

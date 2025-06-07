from Linear_models.Classification.Binary.visual import visual
from Linear_models.Classification.Binary.Iris_dataset import data_linear
from Linear_models.Classification.Binary.models import models




data = data_linear()
df = data.data()
print(df['target'].value_counts())
v = visual(df['sepal length (cm)'] , df['sepal width (cm)'] , df['petal length (cm)'] , df['petal width (cm)'] , df['target'])
x = df.drop(['target'] , axis = 1)
y = df['target']
op = models(x , y)
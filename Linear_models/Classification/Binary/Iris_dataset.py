from sklearn import datasets
import pandas as pd

class data_linear:
    def __init__(self):
        self.data()
    
    def data(self):
        iris = datasets.load_iris(as_frame= True)
        df = iris.frame
        data = df[df['target'].isin([0,1])]
        print(data.head())
        return data
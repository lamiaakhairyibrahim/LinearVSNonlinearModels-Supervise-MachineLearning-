import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler , StandardScaler
from src.Linear_models.Regression.multiple_linear_regression.visual import visual

class PrepData:
    def __init__(self , path):
        self.path = path 
        self.data()
    
    def data(self):
        df = pd.read_csv(self.path)
        print(df.head())
        print("shape of data : " , df.shape)
        return df
    

    def process(self):
        data = self.data()
        print(data.info())
        print(":the number of missing data : " , data.isnull().sum())
        print("ther are not any missing data")
        print("we can use one hot encoding to convert catagorical dataset to numerecal")
        col = ['mainroad','guestroom','basement','hotwaterheating',\
               'airconditioning','prefarea','furnishingstatus']
        for s in col:
            print(data[s].value_counts())
        data1 = data
        for i in col:
            dum = pd.get_dummies(data[i] , prefix= i ).astype('uint8')
            print(dum.head())
            data1 = data1.drop(i , axis=1)
            data1 = pd.concat([data1 , dum], axis=1)

        print(data1.info())

        print("we can check if found duplicate or not in the dataset")
        print("the number of duplicated value is : " , data1.duplicated().sum())
        f=['bedrooms','bathrooms','stories' ,'parking' ]
        op = MinMaxScaler()
        data1[f] = op.fit_transform(data1[f])
        f1 = ['price','area']
        ops = StandardScaler()
        data1[f1] = ops.fit_transform(data1[f1])
        print(data1.head())
        visual(data1)
        # if you want to remove the outlier
        f = ['price','area','bedrooms','bathrooms','stories','parking']
        #for c in f :
        #    Q1 = data1[c].quantile(0.25)
        #    Q3 = data1[c].quantile(0.75)
        #    IQR = Q3 - Q1
        #    L = Q1 - (IQR*1.5)
        #    U = Q3 + (IQR*1.5) 
        #    data1 = data1[(data1[c] >= L) & (data1[c] <= U)]
        #visual(data1)
        x = data1.drop(['price'] , axis=1)
        y = data1['price']

        return x , y
        
        
        

        








import pandas as pd 

class loadData:
    def __init__(self , path):
        self.path = path 

    def read(self):
        df = pd.read_csv(self.path)
        print(df.info())
        return df 
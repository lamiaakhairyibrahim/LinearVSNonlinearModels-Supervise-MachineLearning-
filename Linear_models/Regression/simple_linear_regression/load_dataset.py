import pandas as pd 


class load_data:
    def __init__(self , path):
        self.path = path 

    def read(self):
        df = pd.read_csv(self.path)
        return df 
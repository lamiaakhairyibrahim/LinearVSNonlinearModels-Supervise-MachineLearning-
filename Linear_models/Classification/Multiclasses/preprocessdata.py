import pandas as pd
from src.Linear_models.Regression.simple_linear_regression.load_dataset import load_data
import logging 

class process:
    def __init__(self , path):
        self.path = path 
       

    def final(self):
        op = load_data(self.path)
        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s' , 
                            )
        data = op.read()
        logging.debug(data.info())
        logging.debug(f"number of missing value :\nf{data.isnull().sum()}")
        logging.debug(f"the dublicated value in the dataset :\n{data.duplicated().sum()}")
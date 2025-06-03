from src.Linear_models.Regression.simple_linear_regression.load_dataset import load_data
from src.Linear_models.Regression.simple_linear_regression.visual import visual
  

class preprocess:
    def __init__(self , path):
        self.path = path 

    def preper(self):
        op = load_data(self.path)
        data = op.read()
        print(data.info())
        print("remove [Unnamed: 0] feature")
        data = data.drop(['Unnamed: 0'] , axis = 1)
        print(data.info())
        print(f"the number of missing value in tha dataset :\n{data.isnull().sum()}")
        print(f"the duplicated data in the dataset :{data.duplicated().sum()}")
        op1 = visual(data['YearsExperience'] , data['Salary'])
        op1.show()
        return data.iloc[: ,:1] ,  data.iloc[: ,1:]

from src.Nonlinear_models.Regression.polynomial.load_dataset import loadData
from src.Linear_models.Regression.simple_linear_regression.visual import visual

class process_data:
    def __init__(self , path):
        self.path = path 

    def preb(self):
        op = loadData(self.path )
        data = op.read()
        print(data.head())
        print(f"the number of missing value in tha dataset :\n{data.isnull().sum()}")
        print(f"the duplicated data in the dataset :{data.duplicated().sum()}")
        op1 = visual(data['Temperature (°C)'] , data['Ice Cream Sales (units)'])
        op1.show()


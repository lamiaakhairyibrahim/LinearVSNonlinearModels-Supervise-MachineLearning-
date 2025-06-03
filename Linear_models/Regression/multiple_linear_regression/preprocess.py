from src.Linear_models.Regression.multiple_linear_regression.preprocessdataset import PrepData
from src.Linear_models.Regression.multiple_linear_regression.models import models

op = PrepData(r"D:\my_projects\inprograss\linear_vs_nonlinear_models_and_losses\mlf\src\Linear_models\Regression\multiple_linear_regression\dataset\Housing.csv")
x,y = op.process()
m = models(x , y)

from src.Linear_models.Classification.Multiclasses.preprocessdata import process
from src.Linear_models.Classification.Multiclasses.models import modelS

path = r"D:\my_projects\inprograss\linear_vs_nonlinear_models_and_losses\mlf\src\Linear_models\Classification\Multiclasses\dataset\covtype.csv"

op = process(path)
x , y = op.final()
op = modelS(x , y)
op.multi()

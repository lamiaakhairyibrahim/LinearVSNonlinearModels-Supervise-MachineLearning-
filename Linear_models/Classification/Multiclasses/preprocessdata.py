import pandas as pd
from src.Linear_models.Regression.simple_linear_regression.load_dataset import load_data
from src.Linear_models.Classification.Multiclasses.visual import visual
from sklearn.preprocessing import StandardScaler 
from sklearn.decomposition import PCA


class process:
    def __init__(self , path):
        self.path = path 
       

    def final(self):
        op = load_data(self.path)
        data = op.read()
        print(data.info())
        print(f"number of missing value :\n{data.isnull().sum()}")
        print(f"the dublicated value in the dataset :\n{data.duplicated().sum()}")
        print(data['Cover_Type'].head())
        print(f"number of columns dublicated :{data.columns.duplicated().sum()}")
        print(data.head())
        #op = visual(data)
        sc = StandardScaler()
        f = ["Elevation" ,"Aspect" , "Slope" , "Horizontal_Distance_To_Hydrology" , "Vertical_Distance_To_Hydrology",
             "Horizontal_Distance_To_Roadways" , "Hillshade_9am" , "Hillshade_Noon" , "Hillshade_3pm",
              "Horizontal_Distance_To_Fire_Points" ,  "Wilderness_Area1" , "Wilderness_Area2" ,"Wilderness_Area3" , 
                "Wilderness_Area4" ]
        data[f] = sc.fit_transform(data[f])
        print("I use StandardScaler because the features are Gaussian distributed and contain some outliers")
        print(f"the dataset after standard scalet :\n{data.head()}")
        print("I use the PCA for dimension reduction")
        x = data.drop("Cover_Type", axis=1)
        y = data["Cover_Type"]
        pca = PCA(n_components= 0.95)
        data_pca = pca.fit_transform(x)
        df = pd.DataFrame(data_pca)
        print(f"data after PCA :\n{df.head()}")
        return df , y
from sklearn.linear_model import LinearRegression , Ridge , Lasso , ElasticNet 
from sklearn.linear_model import HuberRegressor , BayesianRidge ,PassiveAggressiveRegressor , TheilSenRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score , mean_squared_error

class models:
    def __init__(self , x , y):
        self.x = x
        self.y = y
        self.linear_models()
      

    def linear_models(self):
        mode = [LinearRegression , Ridge , Lasso , ElasticNet ,
                HuberRegressor , BayesianRidge ,PassiveAggressiveRegressor , TheilSenRegressor ]
        x_tr , x_test , y_tr ,y_test = train_test_split(self.x, self.y , test_size=0.2 , random_state=42)
        for m in mode:
            if m == "Ridge":
                model = m(alpha=0.001)
            elif m == "Lasso":
                model = m(alpha=0.1)
            elif m == "ElasticNet":
                model = m(alpha=0.5)
            else: 
                model = m()
            
            model.fit(x_tr,y_tr)
            y_pred = model.predict(x_test)
            #recedual = y_test - y_pred
            print("the model is : " , m)
            mse = mean_squared_error(y_test,y_pred)
            r2 = r2_score(y_test,y_pred)
            print(f"Mean Squared Error: {mse:.4f}")
            print(f"R^2 Score: {r2:.4f}")
            print("-----------------------------------------------------")


        #return x_tr , x_test , y_tr ,y_test 
    
    """def linear(self ):
        x_tr , x_test , y_tr ,y_test =  self.split()
        LR = LinearRegression()
        LR.fit(x_tr,y_tr)
        y_pred = LR.predict(x_test)
        recedual = y_test - y_pred
        mse = mean_squared_error(y_test,y_pred)
        r2 = r2_score(y_test,y_pred)
        print(f"Mean Squared Error: {mse:.4f}")
        print(f"R^2 Score: {r2:.4f}")
    
    def linear_R(self ):
        x_tr , x_test , y_tr ,y_test =  self.split()
        LR = Ridge(alpha=1.0)
        LR.fit(x_tr,y_tr)
        y_pred = LR.predict(x_test)
        recedual = y_test - y_pred
        mse = mean_squared_error(y_test,y_pred)
        r2 = r2_score(y_test,y_pred)
        print(f"Mean Squared Error: {mse:.4f}")
        print(f"R^2 Score: {r2:.4f}")
    
    def linear_L(self ):
        x_tr , x_test , y_tr ,y_test =  self.split()
        LR = Lasso(alpha=0.001)
        LR.fit(x_tr,y_tr)
        y_pred = LR.predict(x_test)
        recedual = y_test - y_pred
        mse = mean_squared_error(y_test,y_pred)
        r2 = r2_score(y_test,y_pred)
        print(f"Mean Squared Error: {mse:.4f}")
        print(f"R^2 Score: {r2:.4f}")

    def linear_E(self ):
        x_tr , x_test , y_tr ,y_test =  self.split()
        LR = ElasticNet(alpha=0.1, l1_ratio=0.5)
        LR.fit(x_tr,y_tr)
        y_pred = LR.predict(x_test)
        recedual = y_test - y_pred
        mse = mean_squared_error(y_test,y_pred)
        r2 = r2_score(y_test,y_pred)
        print(f"Mean Squared Error: {mse:.4f}")
        print(f"R^2 Score: {r2:.4f}")
    



"""
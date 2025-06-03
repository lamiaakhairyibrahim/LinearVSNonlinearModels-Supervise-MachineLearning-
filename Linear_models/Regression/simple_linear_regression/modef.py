from sklearn.linear_model import LinearRegression
from src.Linear_models.Regression.simple_linear_regression.preprocess import preprocess
from sklearn.model_selection import train_test_split 
from sklearn.metrics import r2_score , mean_squared_error
import matplotlib.pyplot as plt

class simpl_mode :
    def __init__(self ,path ):
        self.path = path
        self.model_l()
    def model_l(self):
        op  = preprocess(self.path)
        x , y = op.preper()
        x_train , x_test , y_train , y_test = train_test_split(x , y , test_size= 0.2 , random_state= 0)
        m = LinearRegression()
        m.fit(x_train , y_train)
        y_pred_test = m.predict(x_test)
        y_pred_train = m.predict(x_train)
        mse = mean_squared_error(y_test,y_pred_test)
        r2 = r2_score(y_test,y_pred_test)
        print(f"Mean Squared Error: {mse:.4f}")
        print(f"R^2 Score: {r2:.4f}")
        print("-----------------------------------------------------")
        
        # Prediction on training set
        plt.scatter(x_train, y_train, color = 'lightcoral')
        plt.plot(x_train, y_pred_train, color = 'firebrick')
        plt.title('Salary vs Experience (Training Set)')
        plt.xlabel('Years of Experience')
        plt.ylabel('Salary')
        plt.legend(['X_train/Pred(y_test)', 'X_train/y_train'], title = 'Sal/Exp', loc='best', facecolor='white')
        plt.box(False)
        plt.show()

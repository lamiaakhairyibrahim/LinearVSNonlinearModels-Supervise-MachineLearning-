from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import RidgeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

class models:
    def __init__(self , x , y ):
        self.x = x
        self.y = y
        self.split()

    def split(self):
        x_train , x_test , y_train, y_test = train_test_split(self.x , self.y , test_size=0.2, random_state= 42)
        return x_train , x_test , y_train, y_test


    def logisticRegression(self):
        x_train , x_test , y_train, y_test = self.split()


    def svc(self):
        x_train , x_test , y_train, y_test = self.split()


    def RidgeClassifier(self):
        x_train , x_test , y_train, y_test = self.split()



       

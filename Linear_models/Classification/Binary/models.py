from sklearn.linear_model import LogisticRegression , SGDClassifier , RidgeClassifier , PassiveAggressiveClassifier 
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix , classification_report

class models:
    def __init__(self , x , y ):
        self.x = x
        self.y = y
        self.split()
        self.logisticRegression_()
        self.PassiveAggressiveClassifier_()
        self.RidgeClassifier_()
        self.svc_()
        self.scdclassifire_()

    def split(self):
        x_train , x_test , y_train, y_test = train_test_split(self.x , self.y , test_size=0.2, random_state= 42)
        return x_train , x_test , y_train, y_test


    def logisticRegression_(self):
        x_train , x_test , y_train, y_test = self.split()
        log = LogisticRegression()
        self.pre_model(log , x_train,x_test,y_train,y_test)
        self.predict(log , x_test ,y_test)


    def svc_(self):
        x_train , x_test , y_train, y_test = self.split()
        svc = LinearSVC()
        self.pre_model(svc,x_train,x_test,y_train,y_test)
        self.predict(svc, x_test ,y_test)


    def RidgeClassifier_(self):
        x_train , x_test , y_train, y_test = self.split()
        ridg = RidgeClassifier()
        self.pre_model(ridg,x_train,x_test,y_train,y_test)
        self.predict(ridg , x_test ,y_test)

    def scdclassifire_(self):
        x_train , x_test , y_train, y_test = self.split()
        sgd = SGDClassifier()
        self.pre_model(sgd,x_train,x_test,y_train,y_test)
        self.predict(sgd ,x_test ,y_test)
    
    def PassiveAggressiveClassifier_(self):
        x_train , x_test , y_train, y_test = self.split()
        passiv = PassiveAggressiveClassifier()
        self.pre_model(passiv,x_train,x_test,y_train,y_test)
        self.predict(passiv ,x_test ,y_test)

    def pre_model(self ,model_ ,x_train , x_test , y_train , y_test ):
        model_.fit(x_train , y_train)
        self.predict(model_ , x_test , y_test)

    def predict(self , model_ , x_tes , y_tes):
        y_pred = model_.predict(x_tes )
        conv_matrix = confusion_matrix(y_tes , y_pred )
        eval_conv_matrix_ = classification_report(y_tes , y_pred )
        print(f"confusion matrix of {model_} is :\n{conv_matrix}")
        print(f"confusion matrix report of {model_} is :\n{eval_conv_matrix_}")
       

from sklearn.linear_model import LogisticRegression , SGDClassifier , RidgeClassifier , PassiveAggressiveClassifier 
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsRestClassifier , OneVsOneClassifier ,OutputCodeClassifier
from sklearn.model_selection import train_test_split 
from sklearn.metrics import confusion_matrix, classification_report
import joblib


class modelS:
    def __init__(self , x , y):
        self.x = x 
        self.y = y 
    
    def split(self):
        x_train , x_test , y_train , y_test = train_test_split(self.x , self.y ,test_size= 0.2 , random_state= 42)
        return x_train , x_test , y_train , y_test

    def multi(self):
        x_train , x_test , y_train , y_test = self.split()
        m = ['LogisticRegression' ,'LinearSVC' , 'SGDClassifier' , 'RidgeClassifier' , 'PassiveAggressiveClassifier']
        s_m = ['OneVsRestClassifier' , 'OneVsOneClassifier' , 'Multiclass' , "OutputCodeClassifier"]
        for j in s_m:
            if j == 'OneVsRestClassifier' :
                for i in m :
                    if i == 'LogisticRegression' :
                        log_ova = OneVsRestClassifier(LogisticRegression())
                        self.pre_model(log_ova , x_train , x_test , y_train , y_test)
                    elif i == 'LinearSVC':
                        svc_ova = OneVsRestClassifier(LinearSVC())
                        self.pre_model(svc_ova ,x_train , x_test , y_train , y_test )
                    elif i == 'SGDClassifier':
                        SGD_ova = OneVsRestClassifier(SGDClassifier(random_state=42))
                        self.pre_model(SGD_ova ,x_train , x_test , y_train , y_test )
                    elif i == 'RidgeClassifier' :
                        ridg_ova = OneVsRestClassifier(RidgeClassifier())
                        self.pre_model(ridg_ova ,x_train , x_test , y_train , y_test )
                    else :
                        pass_ova = OneVsRestClassifier(PassiveAggressiveClassifier(random_state=42))
                        self.pre_model(pass_ova ,x_train , x_test , y_train , y_test )
            elif j == 'OneVsOneClassifier':
                for i in m :
                    if i == 'LogisticRegression' :
                        log_ovo = OneVsOneClassifier(LogisticRegression())
                        self.pre_model(log_ovo , x_train , x_test , y_train , y_test)
                    elif i == 'LinearSVC':
                        svc_ovo = OneVsOneClassifier(LinearSVC())
                        self.pre_model(svc_ovo ,x_train , x_test , y_train , y_test )
                    elif i == 'SGDClassifier':
                        SGD_ovo = OneVsOneClassifier(SGDClassifier(random_state=42))
                        self.pre_model(SGD_ovo ,x_train , x_test , y_train , y_test )
                    elif i == 'RidgeClassifier' :
                        ridg_ovo = OneVsOneClassifier(RidgeClassifier())
                        self.pre_model(ridg_ovo ,x_train , x_test , y_train , y_test )
                    else :
                        pass_ovo = OneVsOneClassifier(PassiveAggressiveClassifier(random_state=42))
                        self.pre_model(pass_ovo ,x_train , x_test , y_train , y_test )
            elif j ==  'Multiclass' :
                for i in m :
                    if i == 'LogisticRegression' :
                        log_d = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=500)
                        self.pre_model(log_d , x_train , x_test , y_train , y_test)
                    elif i == 'LinearSVC':
                        svc_d = LinearSVC(max_iter=1000)
                        self.pre_model(svc_d ,x_train , x_test , y_train , y_test )
                    elif i == 'SGDClassifier':
                        SGD_d = SGDClassifier(loss='log_loss', max_iter=1000, random_state=42)
                        self.pre_model(SGD_d ,x_train , x_test , y_train , y_test )
                    elif i == 'RidgeClassifier' :
                        ridg_d = RidgeClassifier()
                        self.pre_model(ridg_d ,x_train , x_test , y_train , y_test )
                    else :
                        pass_d = PassiveAggressiveClassifier(max_iter=1000, random_state=42)
                        self.pre_model(pass_d ,x_train , x_test , y_train , y_test )
            elif j == "OutputCodeClassifier":
                for i in m :
                    if i == 'LogisticRegression' :
                        log_oc = OutputCodeClassifier(estimator = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=500), code_size=2.0, random_state=42)
                        self.pre_model(log_oc , x_train , x_test , y_train , y_test)
                    elif i == 'LinearSVC':
                        svc_oc = OutputCodeClassifier(estimator = LinearSVC(max_iter=1000), code_size=2.0, random_state=42)
                        self.pre_model(svc_oc ,x_train , x_test , y_train , y_test )
                    elif i == 'SGDClassifier':
                        
                        SGD_oc = OutputCodeClassifier(estimator = SGDClassifier(loss='log_loss', max_iter=1000, random_state=42), code_size=2.0, random_state=42)
                        self.pre_model(SGD_oc ,x_train , x_test , y_train , y_test )
                    
                    elif i == 'RidgeClassifier' :
                        ridg_OC = OutputCodeClassifier(estimator = RidgeClassifier(), code_size=2.0, random_state=42)
                        self.pre_model(ridg_OC ,x_train , x_test , y_train , y_test )
                    else :
                        pass_OC = OutputCodeClassifier(estimator = PassiveAggressiveClassifier(max_iter=1000, random_state=42), code_size=2.0, random_state=42)
                        self.pre_model(pass_OC ,x_train , x_test , y_train , y_test )
      




    def pre_model(self ,model_ ,x_train , x_test , y_train , y_test ):
        model_.fit(x_train , y_train)
        self.savemodel(model_ , f"{model_}.pkl")
        self.predict(model_ , x_test , y_test)

    def savemodel(self , model , filepath):
        joblib.dump(model , filepath)
        print(f"model saved as {filepath}")
        
    def predict(self , model , x_tes , y_tes):
        y_pred = model.predict(x_tes )
        conv_matrix = confusion_matrix(y_tes , y_pred )
        eval_conv_matrix_ = classification_report(y_tes , y_pred )
        print(f"confusion matrix of {model} is :\n{conv_matrix}")
        print(f"confusion matrix report of {model} is :\n{eval_conv_matrix_}")


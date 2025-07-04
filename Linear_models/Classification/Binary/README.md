# Linear Binary Classification

### topecs

- [Dataset](#dataset)
- [Logistic Regression](#logistic-regression)
- [Linear SVM](#linear-svm)
- [RidgeClassifier](#ridgeclassifier)
- [SGDClassifier](#sgdclassifier)
- [PassiveAggressiveClassifier](#passiveaggressiveclassifier)
## dataset
  - In this project, I used the Iris dataset, a classic dataset in machine learning.
    However, instead of using all three classes, I selected only the first two classes:
    Setosa (label 0)
    Versicolor (label 1)
    This converts the problem into a binary classification task, which is suitable for training a Logistic Regression model ,Linear SVM and RidgeClassifier.

    The decision was made because logistic regression,Linear SVM and RidgeClassifier performs best when the classes are linearly separable or nearly separable.
    In the case of Setosa and Versicolor, some features like petal length and petal width show clear separation, making them ideal for logistic regression,Linear SVM and RidgeClassifier

## Logistic Regression

   - [you can read this artical](https://www.geeksforgeeks.org/understanding-logistic-regression/)

## Linear SVM
 - [you can read this artical](https://medium.com/@akhil0435/linear-svm-classification-40dde297c931)
## RidgeClassifier
 - [you can read this artical](https://www.geeksforgeeks.org/ridge-classifier/)
## SGDClassifier
 - [you can read this artical](https://www.geeksforgeeks.org/stochastic-gradient-descent-classifier/)
## PassiveAggressiveClassifier
 - [you can read this artical](https://www.geeksforgeeks.org/passive-aggressive-classifiers/)
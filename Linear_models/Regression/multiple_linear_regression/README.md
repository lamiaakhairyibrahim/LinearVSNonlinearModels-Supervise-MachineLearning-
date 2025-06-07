# Multiple Linear Regression
## Topics
 - [Dataset](#dataset)
 - [Preprocessing](#preprocessing)
 - [Model](#model)


## Dataset
 - A simple yet challenging project, to predict the housing price based on certain factors like house area, bedrooms, furnished, nearness to mainroad, etc. The dataset is small yet, it's complexity arises due to the fact that it has strong multicollinearity.
 link the dataset [dataset](https://www.kaggle.com/datasets/yasserh/housing-prices-dataset)
## Preprocessing
 - check missing value and fixed it.
 - check if there duplicated, and fix it.
 - Visualize the dataset to see the shape of the dataset
 ### Normalization & Standarization
  - size of the value in the data affects the algorithms, if there is a column (salary), and a column(age) there is bias to salary and maybe ignore the effect column(age)
   - so we make Scaling : 
     - to improve the model accuracy 
     - time down of training model 
     - remove the bias
   - ### Normalization(Min-Max Scaling)
     ```pash
     Xnorm = (X-Xmin)/(Xmax-Xmin)
     ```
     - all values are converted its values to be between (0-1)
     - It's used with algorithms that are sensitive to distance or that compare directly between values and the data not gaussian and no  outliers.
     - Like:
        - KNN
        - SVM
        - K-Mean Clustering
        - Neural Networks 

   - ### Standarization(Z-Score Scaling)
     ```pash
     Xstd = (X-Mean) / sd
     ```
     - all values are converted so be it's mean =0 and standard deviation = 1, all values are nearly zero (some values are positive, some values are negative), the data are gaussian and there  outliers
     - like 
       - PCA
       - Linear models

### outliers
  - After using a boxplot, we found some values  outliers
  - we can remove these values or not, as we want in our problem
  - here the outliers related to the houses (flat, vela, ....), i want to detect all kinds of houses, so I don't remove the outlier

### Model
  - from the visualization, the data set shows that the dataset is linear with the target in one format but others other binary, so I expect that the error will be not satisfied for me  as I want if I use linear regression models
  - I used the Linear Regression model but the evaluation was very bad
  ``` 
   Mean Squared Error: 0.5024
   R^2 Score: 0.6529
  ```
  - So I want to improve it , by :
    - use the improved models like :

        -  Ridge 
            - [you can read this article](https://www.geeksforgeeks.org/what-is-ridge-regression/)
        - Lasso 
            - [you can read this article](https://www.geeksforgeeks.org/what-is-lasso-regression/)
        - ElasticNet 
            - [you can read this article](https://www.geeksforgeeks.org/implementation-of-elastic-net-regression-from-scratch/)
        - HuberRegressor 
            - [you can read this article](https://medium.com/@thommaskevin/tinyml-huber-regression-315f30129ab3)
        - BayesianRidge 
            - [you can read this article](https://medium.com/data-science/how-to-build-a-bayesian-ridge-regression-model-with-full-hyperparameter-integration-f4ac2bdaf329)
        - PassiveAggressiveRegressor 
            - [you can read this article](https://amanxai.com/2021/07/04/passive-aggressive-regression-in-machine-learning/)
        - TheilSenRegressor
            - [you can read this article](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html)
     


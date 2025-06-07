


# multiclasses 
# Forest Cover Type Dataset
- [Dataset](#dataset)
- [Multi-classification strategies](#multi-classification-strategies)
- [models](#models)

## Dataset
  - This dataset contains tree observations from four areas of the Roosevelt National Forest in Colorado. All observations are cartographic variables (no remote sensing) from 30 meter x 30 meter sections of forest. There are over half a million measurements total!
  - Can you build a model that predicts what types of trees grow in an area based on the surrounding characteristics? 
What kinds of trees are most common in the Roosevelt National Forest?
Which tree types can grow in more diverse environments? Are there certain tree types that are sensitive to an environmental factor, such as elevation or soil type?
  - [dataset](https://www.kaggle.com/datasets/uciml/forest-cover-type-dataset/data)
 - ## preprocessing dataset 
     - The dataset does not contain a missing value
     - The dataset does not contain a duplicate value
     - After I saw the features are Gaussian distribution, I decided to use the Standard Scaler
     - I use PCA to dimension reduction The number of components was selected based on preserving **95% of the variance** (or mention your threshold if different).

## Multi-classification strategies
  In this project, we apply and compare different strategies to handle multi-class classification problems using linear models. Here’s a brief explanation of each strategy used:


  - ### 1-One-vs-Rest (OvR) | One-vs-All
      - Each class is trained against all other classes combined.
      - 📌 For N classes, we train N binary classifiers.
      - ✔️ Simple, fast, and works well when classes are linearly separable.
      - ⚠️ Can struggle if classes are highly overlapping or imbalanced.


  - ### 2-One-vs-One (OvO)
    - A separate classifier is trained for each pair of classes.
    - 📌 For N classes, we train N(N-1)/2 classifiers.
    - ✔️ More precise decision boundaries between class pairs.
    - ⚠️ Slower when number of classes is large.


  - ### 3-Direct Multiclass Classification (Softmax Regression)
     - Use a model (like multinomial logistic regression) that can natively handle multiple classes.
     - ✔️ No decomposition into binary problems.
     - ✔️ Optimal when data is linearly separable.
     - ⚠️ Assumes independence between classes in some models (e.g., softmax).


  - ### 4-Error-Correcting Output Codes (ECOC)	
      - Each class is represented as a unique binary code, and binary classifiers are trained for each bit position.
      - ✔️ Can improve robustness to errors.
      - ✔️ Effective in noisy or overlapping data.
      - ⚠️ Requires careful code design; more complex.


  - ### 5-Hierarchical Classification	
      - Classes are organized into a tree structure.
      - ✔️ Efficient for large number of classes.
      - ✔️ Can reflect real-world taxonomy (e.g., animals → mammals → dogs).
      - ⚠️ Misclassification at early levels affects final decision.


### models
- I predict the accuracy of linear classification models is between [50-75]% because the dataset was not linear
- I used all linear classification models like :
  - LogisticRegression
  - LinearSVC
  - SGDClassifier
  - RidgeClassifier
  - PassiveAggressiveClassifier



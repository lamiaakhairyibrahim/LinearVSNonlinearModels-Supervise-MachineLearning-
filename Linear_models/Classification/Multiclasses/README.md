# multiclasses 
- [Multi-classification strategies](#multi-classification-strategies)
- [Dataset](#dataset)
- [Logistic Regression](#logistic-regression)
- [Linear SVM](#linear-svm)
- [RidgeClassifier](#ridgeclassifier)
- [SGDClassifier](#sgdclassifier)
- [PassiveAggressiveClassifier](#passiveaggressiveclassifier)

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




## Logistic Regression
## Linear SVM
## RidgeClassifier
## SGDClassifier
## PassiveAggressiveClassifier
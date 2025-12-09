## **Table of Contents**

* [Regularization](#regularization)
* [Regularization Techniques](#regularization-techniques)

  * [1. Lasso Regression](#1-lasso-regression)
  * [2. Ridge Regression](#2-ridge-regression)
  * [3. Elastic Net Regression](#3-elastic-net-regression)
* [Bias - Variance Tradeoff](#bias---variance-tradeoff)
* [Early Stopping](#early-stopping)
* [Weight Decay](#weight-decay)

---

# Regularization

- Used to prevent overfitting → Adds penalty to the model to reduce the risk of memorizing noise in the training data
- Improves generalization → Models that perform better on new, unseen data
- Regularization trades the marginal decrease in training accuracy for an increase in generalizability
- Large weights make the model extremely sensitive to small changes
- Overfitting always happens when the model tries too hard to reduce the training error
- Regularization forces the weights to be small by adding a penalty

# Regularization Techniques

## 1. Lasso Regression

- Least Absolute Shrinkage and Selection Operator Regression
- Adds the absolute value of magnitude of the co-efficient as a penalty term to the loss function
- This will shrink some weights to zero → helps in selecting only the important features and ignoring the less important ones
    
    $$
    Cost = \frac {1} {n}\sum_{i=1}^n (y_i - \hat y_i)^2 + \lambda \sum_{i=1} ^m|w_i| 
    $$
    
    m → number of features
    
    n → number of samples
    
    lambda → Regularization parameter that controls the strength of regularization
    
- **Usage: When we want feature selection (sparse model)**

## 2. Ridge Regression

- Regression model that uses L2 regularization Technique
- Adds the squared magnitude of the co-efficient as a penalty term to the loss function
- Handles Multicollinearity by shrinking the coefficients of correlated features instead of eliminating them
    
    $$
    Cost = \frac {1} {n}\sum_{i=1}^n (y_i - \hat y_i)^2 + \lambda \sum_{i=1} ^m w_i^2  
    $$
    
- **Usage: When we want stability and all features matter**

## 3. Elastic Net Regression

- Combination of both L1 as well as L2 regularization
- Add the absolute norm of the weights as well as the squared measure of the weights → A hyperparameter is used to control the ratio of L1 and L2 regularization
    
    $$
    Cost = \frac {1} {n}\sum_{i=1}^n (y_i - \hat y_i)^2 + \lambda ((1- \alpha)\sum_{i=1} ^m|w_i|  + \alpha \sum_{i=1} ^m w_i^2) 
    $$
    
    *α →*Mixing parameter where 0 ≤ *α* ≤ 1
    
- **Usage: When features are correlated**

***Note***: *Above formulas are applicable for linear models. Neural networks has more weights than the number of features*

<aside>
💡

Lasso → Shrink some weights to 0

Ridge → Shrink weights around 0

**Why?**

If the weights are larger, both the techniques tries to reduce the weight

If the weights are near zero, then the penalty term become smaller in ridge regression, whereas in lasso the penalty term remains linear to the weight 

So lasso shrinks the weights even when they are smaller → making it to 0

**L2 (squared)** → penalty becomes very small near zero → weight shrinks but not forced to zero

**L1 (absolute)** → penalty is constant even near zero → pushes weights all the way to zero

</aside>

# **Bias - Variance Tradeoff**

- Increased training error for decreased testing error is known as bias-variance tradeoff
- **Bias →** measures the average difference between predicted values and true values
    - As Bias increases → a model predicts less accurately on a training dataset; High error in training
- **Variance →** measures the difference between predictions across various unseen data.
    - As variance increases → a model predicts less accurately on unseen data; High error during testing and validation
- Bias and variance, inversely represent the model accuracy on training and test sets
- Goal: Reduce bias and variance as well
- Regularization → decreased model variance at the cost of increased bias

# Early Stopping

- It limits the number of iterations during model training
- Stopping once, when there is no improvement and perhaps even deterioration in training and validation accuracy
- It is a kind of regularization technique

# Weight Decay

- Form of regularization used for deep neural networks
- Reduces sum of squared network weights → similar to L2 regularization in linear models
- But in neural networks, this reduction has and effect similar to L1 regularization → select neuron weights decrease to zero
- Effectively removes nodes from the network, reducing network complexity through sparsity

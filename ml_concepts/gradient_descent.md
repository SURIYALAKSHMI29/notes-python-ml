# Gradient Descent

## Table of Contents
- [Gradient Descent](#gradient-descent)
- [Learning Rate](#learning-rate)
- [Variants of Gradient Descent](#variants-of-gradient-descent)
- [Gradient Descent Algorithm](#gradient-descent-algorithm)

---

# Gradient Descent

- An iterative optimization algorithm used to minimize a cost function by adjusting model parameters in the direction of the steepest descent of the function’s gradient
- Moving in opposite direction of the gradient allows the algorithm to gradually descend towards lower values of the functions and eventually reaching to the minimum of the function

## Learning Rate

- Controls how big or small the steps should be when going downwards in gradient for updating models parameters
- Denoted as **η** (eta)
- If η is too small
    - Take tiny steps during iteration and converge very slowly
    - Can significantly increases training time and computational cost especially for large datasets
- If η is too big
    - Take huge steps leading overshooting the minimum of cost function without settling
    - Fail to converge, causing the algorithm to oscillate. This is called as exploding gradient problem
- Choosing right learning rate can leads to fast and stable convergence improving the efficiency of the training process
- **To address the problems, some techniques can be used**
    1. **Weight Regularization**
        - Initialization of weights are adjusted within an appropriate range, by using the activation function like ReLU
    2. **Gradient clipping**
        - Restrict the gradients to a predefined range to prevent them from becoming excessively large or small
    3. **Batch Normalization**
        - Normalizing the input of each layer → prevent activation function from saturating
        - Thus reducing vanishing and exploding gradient problems

## Variants of Gradient Descent

1. **Batch gradient descent** → computes gradients using the entire dataset in each iteration  
2. **Stochastic gradient descent** → uses one data point per iteration to compute gradients; faster  
3. **Mini-batch gradient descent** → Uses small batches of data for updates  
4. **Momentum based gradient descent** → Speeds up convergence by adding a fraction of the previous gradient to the current update  
5. **Adagrad** → adjusts the learning rate for each parameter based on the accumulated sum of squared gradients
    
    $$
    lr_t=\frac η {\sqrt {G_t+ϵ}} \\[5mm]
    where,\, lr_t=learning\, rate \, at \,'t'\\
    G_t=Sum\,of\, Squared\, Gradients\, upto\,'t' \\
    ϵ = Small\, value\, added\, to\, avoid\, division\, by\, 0
    $$
    
6. **RMSprop (Root Mean Square Propagation)**  
    - AdaGrad reduces the learning rate too aggressively  
    - RMSprop → keeps a moving average of the squared gradients to normalize the gradient updates  
7. **Adam** → Combines momentum and RMSprop  


## Batch Gradient Descent

- Processing the entire dataset at once
- Suitable for small-medium sized dataset, doesn’t oscillate much
- Disadvantage: if Large dataset → slow

## Stochastic Gradient Descent

- Updating at every step
- Faster; But oscillates more
- Used when the dataset is larger

# Gradient Descent Algorithm

- Finding the most efficient and principled way of navigating the error surface
- Weights and bias are modified, let theta be **[w, b]**
- We need to move the theta in the direction of delta theta, but being conservative and move only by a small amount eta (learning rate)
    
    $$
    \theta_{new} = \theta_{old} + \eta. \triangle \theta
    $$
    
- Neural networks are trained using Gradient Descent in combination with back propagation
- Network learning → minimizing the cost function
- Reaches the local minima

**Step 1:** Initialize the variables with random values  
**Step 2:** Calculate the error between actual and predicted values  
**Step 3:** Compute gradient - how much each parameter contributes to this error  
**Step 4:** Adjust params according to gradient value (to reduce loss)  
**Step 5:** Repeat until loss is very small or maximum epoch reached  


[Code](https://jupyter.org/try-jupyter/notebooks/?path=notebooks/gradient_linear_regression.ipynb)

# Table of Contents
- [Derivative](#derivative)
  - [Loss function](#loss-function)
  - [Gradient](#gradient)
  - [Partial Derivative](#partial-derivative)
  - [Applications of Derivatives in ML](#applications-of-derivatives-in-ml)
    - [Gradient Descent](#gradient-descent)
    - [Back propagation](#back-propagation)
    - [Regularization Techniques](#regularization-techniques)
    - [LLM](#llm)
- [Integral](#integral)

---

## Derivative

- Derivative doesn’t exist, when the function is not continuous

### Loss function

- says how wrong our model is and it is back-propagated to adjust the weight matrices.
- To improve the model predictions → Minimize the loss

### Gradient

- The gradient says in which direction the params needs to be changed in order to reduce the error the fastest
- It is a vector of derivatives of the loss w.r.t all params
- Optimization; Minimize the loss function

### Partial Derivative

- Measures change in one variable at a time, keeping others constant

---

## Applications of Derivatives in ML

### Gradient Descent

- Goal → Minimize the loss function
- The gradient of the loss function is a vector of partial derivatives. Each component shows how fast the loss changes if we change that parameter slightly
- **Example**: If  ∇L(θ1)=2, increasing θ1 by 1 increases the loss roughly by 2
    - So the gradient points in the direction where the loss increases the fastest — that’s why it’s called steepest ascent
- Since Gradient points uphill, moving in the exact opposite direction takes us down the slope fastest
    
    $$
    θ_{new}=θ_{old}−η∇L(θ)
    $$
    
- η is learning rate (How big the step is)
- **Gradient = direction of maximum increase;  
Opposite of gradient = direction of maximum decrease**

### Back propagation

- By using chain rule of derivatives, the weights at each layer is modified
- **Process**
    - From the output layer, derivative of loss w.r.t output neurons is computed
    - Propagate these derivatives backward through the network using the chain rule
        
        $$
        \frac {∂L}{∂w}= \frac {∂L}{∂y} . \frac {∂y}{∂w}
        $$
        
    - Every derivative tells use the rate of change of loss w.r.t a weight
    - **gradient = sum of all paths to the next layer × weight × activation derivative**
- Each layer receives a signal about how much it contributed to the error and adjusts accordingly
- **Activation function** → Neural networks are non-linear, during back propagation, derivatives of activation are used to propagate gradients

### Regularization Techniques

- Used to prevent over-fitting by adding a penalty term to the loss function
- Derivatives are used to compute the gradients of these regularized loss functions, ensuring that the penalty terms are incorporated into the optimization process

### LLM

**Attention Mechanisms**

- In transformers, Query Q, key K and values V matrices are derived form input embedding using trainable weights
- During back propagation, Derivatives tell us how much each Q, K, V weight contributes to the final prediction error

**Embedding matrices**

- Each embedding vector is adjusted slightly depending on how the corresponding word influenced the loss

---

## Integral
- In Probabilistic models (Bayesian inference or Gaussian processes) →Used to calculate probabilities and and expectations.
    - For ex, the probability density function must be integrated over a range to find expected values and likelihoods
- Data Integration
- Integrating performance data, user feedback and embedding to adapt models for specific tasks
    - Example, Aggregating results over many queries to optimize a model’s response in a recommendation engine

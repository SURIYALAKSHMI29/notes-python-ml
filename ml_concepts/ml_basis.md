## **Table of Contents**

* [Machine Learning](#machine-learning)

  * [Types of Machine Learning](#types-of-machine-learning)
  * [Reinforcement Learning](#reinforcement-learning)
  * [Self-Supervised Learning](#self-supervised-learning)
* [Linear Regression](#linear-regression)
* [Naive Bayes Algorithm](#naive-bayes-algorithm)
* [Decision Tree](#decision-tree)
* [Logistic Regression](#logistic-regression)
* [Neural Network](#neural-network)
* [Support Vector Machine](#support-vector-machine)
* [K-Means Clustering](#k-means-clustering)
* [Hierarchical Clustering](#hierarchical-clustering)
* [Independent Component Analysis](#independent-component-analysis)

---

# Machine Learning

- Make the machine to learn from data
- **Types of Machine Learning**
    - Supervised - labeled data (Regression, Classification)
    - Unsupervised - no labels (Clustering, Dimensionality Reduction)
    - Reinforcement Learning - Agent learns by reward/penalty
    - Semi-supervised - Mix of Labelled and unlabelled
    - Self-supervised - Learns labels from data itself

### Reinforcement Learning

- Focuses on how agents can learn to make decisions through trial and error to maximize cumulative rewards
- Allows machines to learn by interacting with an environment and receiving feedback based on their actions

**Working**

- The agent observes the current state of the environment, chooses and performs an action based on its policy
- The environment responds by transitioning to a new state and provides reward/penalty
- The agent updates its knowledge based on the reward and the new state
- This cycle repeats with the agent balancing exploration(new actions) and exploitation(using known good actions) to maximize the cumulative reward over time

### Self-Supervised Learning

- A model is trained using data that does not have any labels provided. The model finds patterns and creates its own labels from the data automatically

## Linear Regression

- Finding the best fit line of the data
- Best fit line → line with minimum error
- Error, calculated by the distance between the line and the points
- Gradient descent → Iteratively trying to decrease the error, and find the most appropriate model parameters (here best fit line)
    - If the error is increasing → move in opp direction
    - If the error is decreasing → move in that direction
- **Assumption**: Relationships should be linear [ y = mx +c ]
- **Example**: House value based on its size

## Naive Bayes Algorithm

- **Assumption**: All features are independent
- To find impact of x on y P(y|x), we need impact of y on x P(x|y) as well as independence of y P(y). Learns the P(x|y) and P(y)
- Can be Non-linear → Learns full probability distribution → boundary depends on shape of distribution → can bend.
- **Example**: Detecting Spam e-mails classifier
- Sum of Probabilities of all the features → determine the class

## Decision Tree

- Based on important features, the data is subdivided (based on splitting criteria - gini impurity or information gain(entropy))
- Decisions are made at each step
- **Example**: App recommendation

## Logistic Regression

- Separates the data linearly
- Unlike naive bayes, handles correlated data as well
- How to find the best fit line that separates the classes?
    - How many points are misclassified → Error
    - Lesser the error, better the fit (Gradient descent)
    - Uses log-loss functionability (0-1) using sigmoid function
- Produces a probability of an element to be in that class
- **Example**: Acceptance at a University
    - Based on the marks, students get accepted

## Neural Network

- Can learn non-linear relationships; So they work even when data doesn’t follow a straight line
- Flexible → By changing number of layers, neurons, activation functions
- Neuron → Weighted sum + bias + activation
- Learn automatically

## Support Vector Machine

- If we have 2 lines that separates the data correctly, then the line that is spaced well and far away from all the points is chosen as the best
- Allows the infinite dimensional vector
- Data need not be linearly separable
- **Linear Optimization** → Used to find the line that maximizes the distance from the boundary points
- **Large Margin classifier →** chooses a boundary that maximizes margin
- **Kernel Trick**
    - If the points were not separable by a lines, then we use a curve to separate them. (i.e)
    - Separate the points into 2 different planes and separate them by an another plane that lies in-between them
    - Find the equation(hyperbola) that can separate the points
    - Example: Need to split the oranges and apples that are arranged in mixed way. Idea → Move the apples up, oranges down, and split them apart
- Supports infinite-dimensional input vector
- Kernel helps to work with infinitely long list of features → computer memory or processor speed is not affected
  
## K-Means Clustering

- Calculate the distance of the points from the centroid
- Move the centroid to the center of the cluster
- Reevaluate the data points into clusters
- Repeat until no data points are moving

## Hierarchical Clustering

- If the number of clusters are unknown, Group the points that are closer
- Cluster them until the distance is greater than threshold
- Visual tool - dendrogram is used
- Types
    - Agglomerative (Bottom-up)
        - Single data point clusters → One single cluster or desired number of clusters
    - Divisive clustering (Top-down)
        - A cluster that has all data points → Each data point as separate cluster

### Independent Component Analysis

- A technique used to separate mixed signals into their independent, non-Gaussian components
    - Non-Gaussian  components → do not follow a normal(Gaussian) distribution
    - These are important for finding meaningful patterns in noisy data
- It aim to find linear transformation of data that maximizes statistical independence among the components.
    - statistical independence → Joint probability of X and Y = Product of their individual probabilities
    - Mutually exclusive → X and Y are independent if knowing one does not affect the probability of the other
- Example: Cocktail party problem


> Running time, Accuracy → helps to evaluate the model

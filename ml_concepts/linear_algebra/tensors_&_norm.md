#Table of Contents
- [Tensors](#tensors)
- [Norms](#norms)
  - [L1 Norm](#l1-norm)
  - [Squared L2 Norm](#squared-l2-norm)
  - [Max Norm](#max-norm)
  - [Generalized Lp Norm](#generalized-Lp-norm)

---


### Tensors

- ML generalization of vectors and matrices to any number of dimensions
- 0 dimensional tensor → scalar. Has magnitude only
- 1 dimensional tensor → vector. Has magnitude and direction
- 2 dimensional tensor → matrix
- 3 dimensional tensor → 3D space
- n dimensional tensor → n-tenson (higher dimensional)

### Norms

- Function that quantify vector magnitude → distance from the origin
- Most common → **L2 norm**
    
    $$
    ||x||_2 = \sqrt {\sum_i x_i^2}
    $$
    
    - Measures Euclidean distance from origin
    - Numpy has linear algebra module, that can be used to calculate norm
        
        ```python
        np.linalg.norm(vector)
        ```
        
- **L1 norm**
    
    $$
    ||x||_1 = \sum_i |x_i|
    $$
    
    - Also known as Manhattan norm
    - Represents the total distance from the origin, by moving along the grid lines
- **Squared L2 norm**
    
    $$
    	||x||_2^2 = \sum_i x_i^2
    $$
    
    - Computationally better than L2 norm because,
        - Since squared L2 norm is equal to x transpose. x
- **Max Norm**
    - Also known as L inifinity norm
        
        $$
        ||x||_\infin = max_i |x_i|
        $$
        
    - Returns the absolute value of the largest-magnitude element

**Generalized Lp norm**

$$
||x||_p = {(\sum_i |x_i|^p)}^\frac {1}{p}
$$

p must be a real number; greater than or equal to 1

Can derive L1, L2, and L inifinity norm formulae by substituting for p

> Norms particularly L1 and L2 are used to regularize objective functions

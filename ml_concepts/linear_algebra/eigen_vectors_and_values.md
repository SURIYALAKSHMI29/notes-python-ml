Eigen vectors and values
---

## Table of Contents
- [Eigen vectors and values](#eigen-vectors-and-values)
- [Trick to compute eigen values (for 2*2 matrices)](#trick-to-compute-eigen-values-for-22-matrices)

# Eigen vectors and values

- Due to transformations, the span of a vector changes usually
    
    > The **span** of a vector (or a set of vectors) is the set of all possible **linear combinations** of those vectors.
    > 
- But there are some vectors whose span remains the same even after linear transformations called eigen vectors
- Each eigen vector is associated with a value called eigen value
- **Eigen value** is the **scalar** is scales the vector and its span in a transformation
- Eigen vector in a 3D transformation is **“axis of rotation”**
    - The corresponding eigen value needs to be 1 → the transformation never streatch or squishes anything, just rotates
    - So length of the vector will remain same

$$
A\vec{v}=λ\vec{v} \\ 
 
λ\vec{v}=(λI)\vec{v}\\

A\vec{v}=(λI)\vec{v}
$$

Here, A → transfromation matrix  
v → Eigen vector  
λ → Eigen value  

The LHS is vector multiplication, RHS is scalar multiplication. To make RHS is vector multiplacation, we multiplied  λ with a identity matrix

$$
A\vec{v} - (λI)\vec{v} = \vec{0} \\
(A - λI)\vec{v} = \vec{0}
$$

The resultant vector will be zero, if

- the transformation squishes space into a lower dimension or
- The vector is zero vector

The squishification corresponds to a zero determinant for the matrix

$$
det(A - λI) = 0
$$

By this way, eigen value can be determined. Then solve

$$
(A - λI)\vec{v} = \vec{0}
$$

If the eigen values are not real (imaginary), then there is no eigen vector exists for that transformation

> Eigen values which are complex numbers generally correspond to some kind of rotation in the transformation
> 

A single eigen value can have more eigen vectors

<aside>
💡

All the basis vectors are eigen vectors, with diagonal entries of the matrix being their eigen values

Scaling a diagonal matrix is easier than scaling in a non-diagonal vectors, so it is better to use eigen vectors as basis vectors

For that, we need to find the eigen vectors that spans the full space. 

Transform this eigen basis matrix by the transformation matrix, and then transform the resultant back to standard co-ordinate system

The resultant matrix is the diagonal matrix (**called eigen basis**), it represents the same transformation, but from the perspective of the new(eigen vector) basis

$$
V⁻¹ A V = D
$$

Here, V → eigen basis matrix  
A → transformation matrix

AV → applying a A transformation on V → results in V in standard co-ordinate system  
V⁻¹(resultant) → changing the resultant transformation matrix from standard to eigen basis 

Thus, the required transformation is represented in the eigen basis

</aside>

### Trick to compute eigen values (for 2*2 matrices)

1. Mean of diagonal elements  = Mean of eigen values    (or)
    
    Sum of diagonal elements (Trace) = Sum of eigen values 
    
2. Determinant of a matrix = Product of eigen values

By knowing the mean, the eigen values are must be something + and - of some value  
And product is also known

product = (mean + d) (mean - d)  
product = mean^2 - d^2

d^2 = mean^2 - product

1. Thus, 
    
    $$
    λ1, λ2 = m ± sqrt(m^2 - (ad - bc))
    $$

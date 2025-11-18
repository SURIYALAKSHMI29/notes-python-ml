# Table of Contents
- [Inverse matrices](#inverse-matrices)
- [Rank](#rank)
- [Column space](#column-space)
- [Null Space or Kernel](#null-space-or-kernel)
- [Non-Square matrices](#non-square-matrices)
  - [Linear Systems and Non-Square Matrices](#linear-systems-and-non-square-matrices)

# Inverse matrices

- Used to derive the input from output vector
- For Example,

  $$
  Ax⃗ = v⃗
  $$

  - Here, A is the transformation applied on x vector, the resultant is v vector
  - If the transformation is reversed from v vector, we can get x vector
  - To reverse the transformation inverse of A is used

  $$
  x⃗=A⁻¹v⃗
  $$

  - Applying A inverse transformation on v vector → resultant x vector
- A transformation can be reversed only if the resultant vector’s dimension is not squished
  - For 2D, it shouldn’t result in a line or point
  - For 3D, it should’t result in a plane or line or point
  - If the dimension is reduced → det(A) will become 0
- Applying a transformation, and applying reverse of the transformation results in initial vector

  $$
  A A⁻¹ = I 
  A⁻¹ A = I
  $$

  - Here I is the identity matrix
  - I vector as unit vectors as its columns
  - Ix = x, leaves every vector unchanged

# Rank

- Number of dimensions of a matrix is said to be Rank of the matrix
- Number of dimensions in a column space
- **Rank tells how much the transformation preserves dimensions**
  - Higher the rank, the less collapsing occurs
- Full rank transformation → When rank is equal to number of columns in transformation matrix

# Column space

- Span of all columns of transformation matrix is called as column space
- set of all possible outcomes that happens by applying the transformation
- The columns of the matrix defines where the input vector lands (output vector)
  - And so, the span of those transformed basis vectors gives the all possible outputs
- **A vector equation Ax = v has a solution *if and only if* v lies in the column space of A**
- **Zero vector** is always included in the column space, since linear transformations must keep the origin fixed in place

  $$
  ⎡ 0 ⎤ \\
  ⎣ 0 ⎦
  $$

  - For a full rank(invertible) transformation, the only vector that lands at the origin is the zero vector itself
    - It does **not collapse** space.
    - It only stretches, rotates, flips → but **preserves dimension**.
    - No direction is destroyed.
  - For matrices that aren’t full rank (which squish to a smaller dimension) → have number of vectors that land on zero

# Null Space or Kernel

- Null space of a matrix is the set of all vectors x such that

  $$
  Ax=0
  $$

- It contains all input vectors that the matrix transformation sends to the zero vector
- For example,
  - If 2D transformation squishes space into a line then there is a separate line in a different direction full of vectors that get squished onto origin
    - If the resultant lies in 1 direction means, the perpendicular direction is get destroyed (squished onto origin)
  - If a 3D transformation
    - Squishes space onto a plane → full line of vectors that land on the origin (The vector perpendicular to that plane is the only one that collapses to 0)
    - Squishes space onto a line → whole plane of vectors that land on the origin
- If v vector is zero vector in a linear system of equations, then null space gives all the possible solutions to the equation

  $$
  Ax=0
  $$

  If RHS is zero vector → system is called homogeneous

  Homogeneous equation → all solutions are exactly the null space

  Since null space → vectors that A sends to 0

> **A⁻¹  exists if and only if Null(A)={0}**
>
> → If ANY non-zero vector collapses to 0 → inverse cannot exist  
> → If the only input giving 0 is the zero vector → inverse exists  

> For any matrix *A* with *n* columns:
>
>                          Rank(A) + Nullity(A) = n
>
> where:
> - **Rank** = number of dimensions of column space
> - **Nullity** = dimension of null space (how many directions collapse to 0)
> - **n** = input dimension (number of columns)

# Non-Square matrices

- A matrix with m rows and n columns (m×n) encodes a transformation from an n-dimensional space (input vectors) to an m-dimensional space (output vectors)

  $$
  \begin{bmatrix}
  1 & 0 \\
  0 & 1 \\
  1 & 1
  \end{bmatrix}
  $$

- Here, we have 3*2 matrix
- We are transforming 2D to 3D
  - 2 basis vectors, 3 co-ordinate points

## Linear Systems and Non-Square Matrices

- Such matrices can still be used in linear systems, but the system may be underdetermined (more variables than equations - ex. 2*3) or overdetermined (more equations than variables - ex. 3*2)
- These cases lead to infinite solutions, no solutions, or projecting onto the closest point in the column space.

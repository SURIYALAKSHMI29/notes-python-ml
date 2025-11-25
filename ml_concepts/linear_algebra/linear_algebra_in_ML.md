# Table of Contents
- [Data Representation](#data-representation)
- [Data Preprocessing](#data-preprocessing)
- [Word Embeddings](#word-embeddings)
- [Dimensionality Reduction](#dimensionality-reduction)
- [Real World Examples](#real-world-examples)
- [Vectors](#vectors)
  - [Token Embeddings](#token-embeddings)
  - [Hidden State in LLMs](#hidden-state-in-llms)
  - [Sentence Embeddings / BERT Embeddings](#sentence-embeddings--bert-embeddings)
  - [Vector Operations](#vector-operations)
- [Matrices](#matrices)
  - [Data Storage](#data-storage)
  - [Enable vectorized Linear Algebra operations](#enable-vectorized-linear-algebra-operations)
  - [Matrix Operations](#matrix-operations)
  - [Determinant](#determinant)
  - [Inverse](#inverse)
  - [Column Space](#column-space)
  - [Null Space](#null-space)
  - [Transpose](#transpose)
  - [Eigen vectors and values](#eigen-vectors-and-values)

---

# Data Representation

- Using vectors, matrices and tensors to represent data

# Data Preprocessing

- Technique like normalization and standardization rely on matric operations to rescale features, ensuring no single features dominates the learning process

# Word Embeddings

- Embedding vectors to efficiently represent words for NLP problems
- Replacing a large dimensional vector with smaller one
- Example: 2D plane is embedded into a 3D space
- Similar words(meaning) have similar vectors
- For example, banana and orange vectors will be similar, where the word water will be different from these
- Used for text, search, recommendation, chatbots, etc

# Dimensionality Reduction

- Using eigen vectors and eigen values to deal with large-dimensional data
    - Rotate and project high-dimensional data into a smaller space (PCA)
- Allows to reduce the number of features or dimensions of the data, keeps most important structure (variance) of the data
- Example: Principle Component Analysis(PCA)
- Goal: To narrow down our search and analysis to a lower umber of dimensions and features

> Numpy can be used to represent vectors

# Real World Examples

**Personalized Recommendation Feature (YT, Spotify,.) → Uses Vector Embedding in some form**

For example, *Movie Recommendation*

Factors → User’s age group, Movie type, Movie rating

These are represented in Matrix structure, User matrix, and movie matrix (represented in a way that computation will be efficient)

**By taking dot product, we can find which user prefers which movie**  
The movie vectors closure to a user, will be the movies preferred by them. To find how close they (user and movie) are, **dot product** can be used


# Vectors

- In ML, it is a list of numbers that represents data
- This data could be an image, a sentence, a token, a user, a product, a data point, a hidden state, or even an entire context window
- So, **Vector is a numeric identity of something**
    
    **Why?**
    
    - Because computers only understand numbers
    - So, ML convert everything into vector. And ML models can compare, transform, add, scale, optimize it using LA operations on these vectors
- Vector → point in a high-dimensional space
    - For example, If a word has a 768-dimensional embedding means,
        - its meaning is stored as a position in a 768D space
        - similar words are close
        - opposite words are far
- In ML,
    - **vector → concept**
    - **Distance between vectors → Relation between vectors**

## Token Embeddings

- Every token(word/piece) is converted to a vector
- This vector captures meaning, context behavior, grammar role, emotion, relation with other words
- **Process**
    - **Tokenizer builds a vocabulary list** and assigns IDs (token, ID)
    - **Embedding matrix is initialized randomly -** every token ID gets a random vector (id, vector values)
    - During training, backpropagation updates those vectors so that tokens used in similar contexts get similar embeddings
    - The mapping token → ID is fixed; the embedding vectors themselves are updated during training

## Hidden State in LLMs

- At each layer, the model produces a new vector representing its meaning, context, deeper understanding
- Every layer transforms vectors → more expressive vectors
- For example, word “apple” has same embedding in the embedding matrix
    - But based on its usage, and context in a sentence its meaning varies
    - “Apple is a fruit” and “Apple released a new product”. Here in 1st sentence, apple represents fruit, where in second it refers to a company
    - So when the word comes, it’s vector is passed into a neural network, where the vector gets changed at each layers based on the sentence, its meaning, and context
    - Each layer’s hidden state contributes to predicting the next token; the final layer hidden state is used by the output head to predict probabilities for the next token

## Sentence Embeddings / BERT Embeddings

- BERT → Bidirectional Encoder Representations from transformers
- Whole sentence is embedded into a single vector
- Useful for search, retrieval, chatbots, similarity and recommendation
- **Process**
    - A new vector is created with IDs of each token as rows
    - Each token is passed into a neural network(transformer) to make it context-aware token
    - After that, these tokens are combined into one sentence vector. Different methods exists for this process
        - **CLS token** → the model attaches a hidden vector at the front which is taken as the sentence vector that captures information from all tokens because attention allows it to ‘look’ at every token
        - **Mean Pooling** → It averages all token vectors
        - **Max pooling** → Take the max value per dimension
- This sentence vector can be used for all reasoning tasks and making decisions.
- **Example**
    - In classifier → whether the email is spam or not
    - In similarity → cosine similarity, how this sentence is similar to another one
    - In translation → Sentence in English is converted into a vector, decoder turns this vector into Tamil
- **How do they interpret meaning** → During training, model reads millions of sentences and tries to predict the nest word. To minimize error, it slowly changed vectors so similar meaning come together

> →Vectors live in 768D or 1024D space  
> →Distance (cosine or euclidean) ~ similarity  
> →Cosine similarity (dot product)  
> →Contextual Embeddings: Word embedding are static; Hidden states are context-aware

## Vector Operations

- Addition/subtraction → combining meanings  
    - Example: king - man + woman ~ Queen
- Scaling → emphasizing some features
- Matrix multiplication → linear transformation (used in transformers)

---

# Matrices

- Collection of vectors
    - Columns → features or dimensions
    - Rows → samples or data points
- **Why matrix?**
    - Store all samples and features together in one structured object
    - Can transform all samples in one step, compute predictions efficiently, apply linear transformations
    - Batch computation → compute predictions for all samples at once, Faster
    - Matrices runs efficiently on GPUs / TPUs. GPUs have hardware built for
        - Matrix Multiply Units (MMUs)
        - Tensor cores
        - SIMD operations
    - All ML math is Matrix math
        - Forward pass → Matrix multiplications
        - Backpropagation
- **Why not arrays / list?**
    - Lists are fine for single vectors but
        - No formal support for linear algebra operations
        - Cannot compute batch(all at once) operations efficiently
    - ML requires huge parallel computation, which lists/arrays lacks

## Data Storage

- Stores data in matrix structure.
- **Example**
    - Image batch - stores images as tensors(multi-dimensional matrices)
        - No.of color channels per image → 3 (RGB)
        - Image height and width → 224 * 224
        - This one image is basically 3 matrices of 224*224
    - Text batch - After embeddings, sentences are represented in matric format

## Enable vectorized Linear Algebra operations

- ML models apply linear transformation in Dense layers, Embeddings, Gradient calculations
- Here, matrices are suitable. Because Matrices have strict shape rules, predictable memory layout

## Matrix Operations

- Addition / subtraction → combine features or add bias
- Multiplication / Dot product → Combine input with weights; Projection, similarity
- Transpose → swap rows and columns; Needed in solving equations
- Inverse → Solve linear systems (linear regression, least squares)
- Eigen vectors / eigen values → directions of variance; used in PCA or understanding transformations

## Determinant

- Determinant → how much a linear transformation stretches or shrinks space

**Invertibility of matrices**

- If det = 0, matrix cannot be inverted
- Neural networks need
    - Weight matrices that don’t collapse input directions
    - gradients that don’t vanish because of singular mappings
- This idea underlies rank, null space and stable training

**Principal Component Analysis**

Covariance matrix det is used for

- Determining variance (total variance in data)
- Checking if covariance matrix is singular, PCA cannot proceed

PCA uses eigen values of covariance matrix and determinant is product of eigen values → describes total variance

## Inverse

- Reverse/undoing the transformation

## Column Space

- All directions that a model layer can produce
- If weight matrix W is low-rank, then its column space is small and model cannot represent complex functions
- Affects training, accuracy, and generalization

## Null Space

- All directions a model destroys (the info the model discards)
- If W has a nontrivial null space, some inputs are mapped to zero, gradients vanish → model stops learning in those directions

## Transpose

- Flips rows and columns
- In ML, matrix multiplication requires matching dimensions. Sometimes the shapes don’t match, so we need transpose
- Example: In attention mechanism, We compute Q.k. Where Q and k are of same dimension, so Q. (transpose of k) is done

## Eigen vectors and values

- **Gradient** = direction + size of adjustment
    - If eigenvalue > 1 → gradient explodes
    - If eigenvalue < 1 → gradient vanishes
    - A gradient passes through many layers, this is basically multiplying the matrices over and over
    - When repeatedly multiply by a matrix, the result is dominated by the matrix’s largest eigen value
- In PCA,
    - Covariance matrix is calculated, and after that eigen vectors and values are computed.
    - Eigen vector with largest eigen value preserves the information the most
    - Project the data in the new co-ordinate system whose axes are principal direction

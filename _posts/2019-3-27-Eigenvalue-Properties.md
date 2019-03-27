When I took the math subject GRE I learned that in order to solve common linear algebra questions on the exam quickly, you should keep in mind a few facts about eigenvalues

* The product of the eigenvalues of a matrix equals the determinant of the matrix
* The sum of the eigenvalues of a matrix equals the trace of the matrix
* If a matrix is invertible, the inverse matrix has reciprocal eigenvalues

I'm going to prove each of these facts.

1. (product of eigenvalues equals determinant) Thinking back to your linear algebra, remember that we compute the characteristic polynomial by expanding \\(\det(A - \lambda I)\\). Since the eigenvalues, \\(\lambda_1, ..., \lambda_n\\), are the roots of the characteristic polynomial, we can factor it as follows

$$\det(A-\lambda-I) = (\lambda_1 - \lambda) ... (\lambda_n - \lambda).$$

If we set \\(\lambda = 0\\) we get

$$\det(A) = \lambda_1 \cdot ... \cdot \lambda_n.$$

Which shows that the product of the eigenvalues of a matrix equals its determinant (and this is the constant term for the characteristic polynomial).

2. (sum of eigenvalues equals trace) Again, we can find the characteristic polynomial

$$\det(A-\lambda-I) = (\lambda_1 - \lambda) ... (\lambda_n - \lambda)$$

$$ (-1)^n \lambda^n + (\lambda_1 + ... + \lambda_n) \lambda^{n-1} + ... + (-1)^n \det(A)).$$

Notice that the coefficient of \\(\lambda^{n-1}\\) is the sum of the eigenvalues, but this term is also the trace of \\(A\\) (look at the characteristic polynomial of a \\(2 \times 2\\) matrix for an example).

3. (inverse has reciprocal eigenvalues) This is pretty simple. Remember that an eigenvalue satisfies

$$A x = \lambda x$$

multiplying by $A^{-1}$ yields

$$x = \lambda A^{-1} x$$

and rearranging gives

$$A^{-1} x = \frac{1}{\lambda} x.$$

This is symmetric, so for each eigenvalue of \\(A\\) (or \\(A^{-1}\\)) there is a reciprocal eigenvalue for the inverse. Notice that if the matrix is invertible it doesn't have 0 as an eigenvalue since the determinant is non-zero.

---
layout: post
title: Fibonacci numbers and linear algebra
---

Remember the Fibonacci numbers?

$$0,1,1,2,3,5,8,...$$

They are famous in mathematics and have a neverending list of properties and connections to other mathematical objects. They are defined by the following recurrence relation

$$F_n = F_{n-1} + F_{n-2}$$

with initial conditions \\(F_0 = 0, F_1 = 1\\). It turns out that there are many other ways to compute the \\(n\\)th Fibonacci number besides using the recurrence relation. One way is called the Binet formula

$$F_n = \frac{\varphi^n - \psi^n}{\varphi - \psi} = \frac{\varphi^n - \psi^n}{\sqrt{5}}$$

where \\(\varphi = \frac{1 + \sqrt{5}}{2}\\) and \\(\psi = 1 - \varphi = -\frac{1}{\varphi} = \frac{1 - \sqrt{5}}{2}\\). The number \\(\varphi\\) is referred to as the golden ratio.

As an undergrad, I took a course in combinatorics and we proved many facts about the Fibonacci numbers (and other related sequences). It turns out that we can derive some of these facts by reframing the Fibonacci numbers in terms of linear algebra. Consider the following system of equations

$$F_n = F_{n-1} + F_{n-2}$$

$$F_{n-1} = F_{n-1} + 0F_{n-2}.$$

We can rewrite this as 

$$\begin{pmatrix}
F_{n} \\
F_{n-1}
\end{pmatrix} = \begin{pmatrix}
1 & 1 \\
1 & 0
\end{pmatrix}
\begin{pmatrix}
F_{n-1} \\
F_{n-2}
\end{pmatrix}.$$

Conveniently, this matrix also contains the initial values for the Fibonacci sequence, which yields the following identity (which can be used to compute Fibonacci numbers via repeated squaring)

$$\begin{pmatrix}
1 & 1 \\
1 & 0
\end{pmatrix}^n = \begin{pmatrix}
F_{n+1} & F_n \\
F_n & F_{n-1}
\end{pmatrix}.$$

From this representation, we can easily derive the following identity (called Cassini's identity)

$$(-1)^n = F_{n+1} F_{n-1} - F_n^2.$$

The proof is as follows

$$(-1)^n = \left( \det \begin{pmatrix}
1 & 1 \\
1 & 0
\end{pmatrix} \right)^n = \det \begin{pmatrix}
1 & 1 \\
1 & 0
\end{pmatrix}^n = \det \begin{pmatrix}
F_{n+1} & F_n \\
F_n & F_{n-1}
\end{pmatrix} = F_{n+1} F_{n-1} - F_n^2.$$

We can also derive the Binet formula mentioned earlier. Recall (or be introduced to) the eigendecomposition of a matrix

$$A = Q \Lambda Q^{-1}$$

where \\(\Lambda\\) is a diagonal matrix of the eigenvalues of \\(A\\) and \\(Q\\) is the square matrix of the corresponding eigenvectors. One reason why this factorization is useful is because

$$A^n = Q \Lambda Q^{-1} Q \Lambda Q^{-1} ... Q \Lambda Q^{-1} Q \Lambda Q^{-1}$$

$$ = Q \Lambda^n Q^{-1}$$

and computing powers of a diagonal matrix is equivalent to taking powers of the entries on the diagonal (so we don't actually need to compute any matrix multiplications except for multiplying by \\(Q\\) and \\(Q^{-1}\\)).

This factorization exists if and only if the sum of the dimensions of the eigenspaces of \\(A\\) is equal to \\(n\\) if \\(A\\) is an \\(n \times n\\) matrix.

This means we need to compute the eigenvectors and eigenvalues of 

$$A = \begin{pmatrix}
1 & 1 \\
1 & 0
\end{pmatrix}$$

to determine if it is diagonalizable. The characteristic polynomial is \\(\lambda^2 - \lambda -1\\) which has roots at 

$$\frac{1-\sqrt{5}}{2}, \frac{1+\sqrt{5}}{2}$$

which are \\(\varphi, \psi\\) as defined above. As a sidenote, you can derive this polynomial from the definition of the golden ratio \\(\varphi = \frac{a}{b} = \frac{a+b}{a} \\). The corresponding eigenvectors of \\(A\\) are

$$ \begin{pmatrix}
\varphi \\
1 
\end{pmatrix}, \begin{pmatrix}
\psi \\
1 
\end{pmatrix}.$$

which gives us the following eigendecomposition

$$ A = \begin{pmatrix}
\varphi & \psi \\
1 & 1 
\end{pmatrix}
\begin{pmatrix}
\varphi & 0 \\
0 & \psi 
\end{pmatrix}
\begin{pmatrix}
\varphi & \psi \\
1 &  1 
\end{pmatrix}^{-1}.$$

From the identity 

$$\begin{pmatrix}
1 & 1 \\
1 & 0
\end{pmatrix}^n = \begin{pmatrix}
F_{n+1} & F_n \\
F_n & F_{n-1}
\end{pmatrix}$$

we obtain

$$ \begin{pmatrix}
F_{n+1} & F_n \\
F_n & F_{n-1}
\end{pmatrix} = A^n = 

\begin{pmatrix}
\varphi & \psi \\
1 & 1 
\end{pmatrix}
\begin{pmatrix}
\varphi^n & 0 \\
0 & \psi^n
\end{pmatrix}
\begin{pmatrix}
\varphi & \psi \\
1 &  1 
\end{pmatrix}^{-1}$$

and if we write out the result of this matrix multiplication, we obtain the Binet formula.



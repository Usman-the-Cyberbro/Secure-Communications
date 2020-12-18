In the last challenge we saw that there is a special kind of basis called an orthogonal basis. Given a basis v1, v2, ..., vn ∈ V for a vector space, the Gram-Schmidt algorithm calculates an orthogonal basis u1, u2, ..., un ∈ V.

In "An Introduction to Mathematical Cryptography", Jeffrey Hoffstein, Jill Pipher, Joseph H. Silverman, the Gram-Schmidt algorithm is given as:

Algorithm for Gram-Schmidt

u1 = v1
Loop i = 2,3...,n
   Compute μij = vi ∙ uj / ||uj||2, 1 ≤ j < i.
   Set ui = vi - μij * uj (Sum over j for 1 ≤ j < i)
End Loop


To test your code, let's grab the flag. Given the following basis vectors:

v1 = (4,1,3,-1), v2 = (2,1,-3,4), v3 = (1,0,-2,7), v4 = (6, 2, 9, -5),

use the Gram-Schmidt algorithm to calculate an orthogonal basis. The flag is the float value of the second component of u4 to 5 significant figures.

Note that this algorithm doesn't create an orthonormal basis! It's a small change to implement this. Think about what you would have to change. If you're using someone else's algorithm and the flag is incorrect, this might be the issue. If everything seems good and you're still not having your answer accepted, check your rounding when you take 5.s.f. for the solution.
If you look closely enough, lattices start appearing everywhere in cryptography. Sometimes they appear through manipulation of a cryptosystem, breaking parameters which were not generated securely enough. The most famous example of this is Coppersmith's attack against RSA cryptography.

Lattices can also be used to build cryptographic protocols, whose security is based on two fundamental "hard" problems:

The Shortest Vector Problem (SVP): find the shortest non-zero vector in a lattice L. In other words, find the non-zero vector within v ∈ L such that ||v|| is minimised.

The Closest Vector Problem (CVP): Given a vector w ∈ Rm that is not in L, find the vector v ∈ L that is the closest to w, i.e. find the vector v ∈ L such that ||v - w|| is minimised.

The SVP is hard for a generic lattice, but for simple enough cases there are efficient algorithms to compute either a solution or an approximation for the SVP. When the dimension of the lattice is four or less, we can compute this exactly in polynomial time; for higher dimensions, we have to settle for an approximation.

Gauss developed his algorithm to find an optimal basis for a two-dimensional lattice given an arbitrary basis. Moreover, the output v1 of the algorithm is a shortest nonzero vector in L, and so solves the SVP.

For higher dimensions, there's a basis lattice reduction algorithm called the LLL algorithm, named after Lenstra, Lenstra and Lovász. If you play CTFs regularly, you'll already know about it. The LLL algorithm runs in polynomial time. For now though, lets stay in two dimensions.


Gauss's algorithm roughly works by subtracting multiples of one basis vector from the other until it's no longer possible to make them any smaller. As this works in two-dimensions, it's nice to visualise. Here's a description of the algorithm from "An Introduction to Mathematical Cryptography", Jeffrey Hoffstein, Jill Pipher, Joseph H. Silverman:

Algorithm for Gaussian Lattice Reduction

Loop
   (a) If ||v2|| < ||v1||, swap v1, v2
   (b) Compute m = ⌊ v1∙v2 / v1∙v1 ⌋
   (c) If m = 0, return v1, v2
   (d) v2 = v2 - m*v1
Continue Loop


Note the similarity to Euclid's GCD algorithm with the "swap" and "reduction" steps, and that we have to use the floor, as on a lattice we may only use integer coefficients for our basis vectors.

For the flag, take the two vectors v = (846835985, 9834798552), u = (87502093, 123094980) and by applying Gauss's algorithm, find the optimal basis. The flag is the inner product of the new basis vectors.
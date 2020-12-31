We're now ready to start talking about lattices. Given a set of linearly independent vectors v1, v2, ..., vn ∈ Rm, the lattice L generated by v1, v2, ..., vn is the set of linearly independent vectors v1, v2, ..., vn with integer coefficients.

L = {a1*v1 + a2*v2 + ... + ak*vk : a1, a2, ..., an ∈ Z}.

The basis for the lattice L is any set of independent vectors that generates L. The choice of basis is far from unique. In the image below, we show a two dimensional lattice with two different basis vectors given by u1, u2 and v1, v2.


diagram of lattice



Using a basis, we can reach any point within the lattice with integer multiples of the basis vectors. The basis vectors also define the fundamental domain:

F(v1,...,vn) = {t1 v1 + t2 v2 + ... + tn vn : 0 ≤ ti < 1}.

As a two dimensional example, the fundamental domain is the parallelogram with sides u1 and u2.

We can calculate the volume of the fundamental domain from the basis vectors. As an example, let us take a two dimensional lattice with basis vectors v = (2,5), u = (3,1). Create a matrix A with rows corresponding to the basis vectors: A = [[2,5],[3,1]]. The volume of the fundamental domain is the magnitude of the determinant of A: Vol(F) = |det(A)| = |2*1 - 5*3| = |-13| = 13.

For the flag, calculate the volume of the fundamental domain with the basis vectors v1 = (6, 2, -3), v2 = (5, 1, 4), v3 = (2, 7, 1).
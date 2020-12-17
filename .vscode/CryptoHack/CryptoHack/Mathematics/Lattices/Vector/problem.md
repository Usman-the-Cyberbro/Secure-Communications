Before defining a lattice or talking about how lattices appear in cryptography, let's review some of the basics of linear algebra. The following challenges should be considered as revision, if this is totally new to you, you might need to do a bit of background reading. As usual, we recommend "An Introduction to Mathematical Cryptography" by Hoffstein, Pipher, Silverman, as well as this excellent introduction to lattices and their applications.

A vector space V over a field F is a set defined with two binary operators. For a vector v ∈ V, and a scalar a ∈ F, vector addition takes two vectors and produces another vector: v + w = z, for v,w,z ∈ V and scalar multiplication takes a vector and a scalar and produces a vector: a*v = w, for v,w ∈ V, a ∈ F.

You will probably have first seen vectors in the context of a two dimensional vector space defined over the reals. We'll use this here too as an example!


Let's consider a two dimensional vector space over the reals. A vector v ∈ V can be considered as a pair of numbers: v = (a,b) for a,b ∈ R. Vector addition works as v + w = (a,b) + (c,d) = (a+c, b+d), and scalar multiplication by c*v = c*(a,b) = (c*a, c*b).

One can also define the inner product (also called the dot product), which takes two vectors and returns a scalar. Formally we think of this as v ∙ w = a for v,w ∈ V, a ∈ F. In our two-dimensional example, the inner product works as v ∙ w = (a,b) ∙ (c,d) = a*c + b*d.

Time for the flag! Given a three dimensional vector space defined over the reals, where v = (2,6,3), w = (1,0,0) and u = (7,7,2), calculate 3*(2*v - w) ∙ 2*u.
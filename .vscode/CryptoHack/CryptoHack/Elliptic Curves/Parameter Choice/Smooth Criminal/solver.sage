# This file was *autogenerated* from the file solver.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_280810182131414898730378982766101210916 = Integer(280810182131414898730378982766101210916); _sage_const_105268671499942631758568591033409611165 = Integer(105268671499942631758568591033409611165); _sage_const_291506490768054478159835604632710368904 = Integer(291506490768054478159835604632710368904); _sage_const_179210853392303317793440285562762725654 = Integer(179210853392303317793440285562762725654); _sage_const_310717010502520989590157367261876774703 = Integer(310717010502520989590157367261876774703)
p = _sage_const_310717010502520989590157367261876774703 
a = _sage_const_2 
b = _sage_const_3 
E = EllipticCurve(Integers(p),[_sage_const_0 ,_sage_const_0 ,_sage_const_0 ,a,b])
g_x = _sage_const_179210853392303317793440285562762725654 
g_y = _sage_const_105268671499942631758568591033409611165 
a_x = _sage_const_280810182131414898730378982766101210916 
a_y = _sage_const_291506490768054478159835604632710368904 
G = E.point((g_x, g_y))
A = E.point((a_x, a_y))

fac = list(factor(G.order()))
moduli = []
remainders = []
for i in fac:
    G0 = G * ZZ(G.order()/(i[_sage_const_0 ]**i[_sage_const_1 ]))
    A0 = A * ZZ(G.order()/(i[_sage_const_0 ]**i[_sage_const_1 ]))
    moduli.append(i[_sage_const_0 ]**i[_sage_const_1 ])
    remainders.append(discrete_log(A0,G0, operation = '+'))
shared_secret = crt(remainders,moduli)
print (shared_secret)


import hashlib
from Crypto.Util.number import *

def Point_addition(v1,v2):
	if v1 == O:    
		return v2
	elif v2 == O:  
		return v1
	else:          
		x1,y1 = v1
		x2,y2 = v2

		if (x1 == x2) and (y1 == -y2): 
			return O
		else: 
			if v1 != v2: 
				l = (y2 - y1) * inverse(x2-x1,p)
			else: 
				l = ( ( 3*pow(x1,2) + a ) * inverse(2 * y1, p) ) 
	x3 = (l**2 - x1 - x2 ) % p     
	y3 = (l*(x1 - x3) - y1) % p 
	return (x3,y3)

def Scalar_Multiplication(n,Q,R):
	while n > 0: 
		if n % 2 == 1: 
			R = Point_addition(R, Q)

		Q = Point_addition(Q,Q) 
		n = n//2

	return R




a = 497
b = 1768
p = 9739

P = (815, 3190)
O = (0,0)

Q = P 
R = O

n = 1829

Qn =  Scalar_Multiplication(n,P,R) 

m = hashlib.sha1()
m.update(str(Qn[0]).encode())
print(m.hexdigest()) 
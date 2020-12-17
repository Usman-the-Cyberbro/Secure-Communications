class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a 
        self.b = b 
        self.p = p 

class Point:
    def __init__(self, x=False, y=False):
        self.x = x 
        self.y = y 
        self.o = not (type(x) == int and type(y) == int)

    def __eq__(self, q): 
        return (self.x == q.x and self.y == q.y) or (self.o and q.o)
    def __ne__(self, q): 
        return not (self == q)

    def __str__(self):
        return (f"Point({self.x},{self.y})" if not self.o else "Point(O)")
    
    def point_add(p, q, ec = EllipticCurve(497, 1768, 9739)):
	    # P + point at infinity = P
	    if p.o:
	        return q
	    if q.o:
	        return p

	    # P + -P = point at infinity
	    if p.x == q.x and p.y == -q.y:
	        return Point()

	    # Else, point add algorithm
	    if p != q:
	        x_inv = inverse(q.x - p.x, ec.p)
	        l = ((q.y - p.y) * x_inv) % ec.p
	    else:
	        y_inv = inverse(2 * p.y, ec.p)
	        l = (((3*(p.x**2)) + ec.a) * y_inv) % ec.p
	    res_x = ((l**2) - p.x - q.x) % ec.p
	    res_y = ((l * (p.x - res_x)) - p.y) % ec.p
	    return Point(res_x, res_y)
	    
	p = Point(493, 5564)
	q = Point(1539, 4742)
	r = Point(4403, 5202)
	s = point_add(point_add(point_add(p, p), q), r)
	print(s)
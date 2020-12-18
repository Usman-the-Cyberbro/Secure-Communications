import numpy as np 


def gauss_reduction(v1, v2):
    while True:
        if np.linalg.norm(v2) < np.linalg.norm(v1):
            v1, v2 = v2 , v1
        m = round(np.inner(v1, v2)// np.inner(v1, v1))
        if m == 0:
            return np.inner(v1,v2) 
        v2 = v2 - m*v1

print(f'The flag is : {gauss_reduction( np.array([846835985, 9834798552]), np.array([87502093, 123094980]) ) }')
import numpy as np

vect = np.array(([[6,2,-3], [5,1,4], [2,7,1]]))

print("{0:.5f}".format(abs(np.linalg.det(vect))))
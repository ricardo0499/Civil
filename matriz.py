import numpy as np
a=np.array([[6,3,0,0,0],[3,8,1,0,0],[0,1,4,1,0],[0,0,1,4,1],[0,0,0,1,2]])
b=np.array([-43.75,-64.25,-31.5,-15,-6])
x=np.linalg.solve(a,b)
print(x)

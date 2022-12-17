import numpy as np
from ctypes.wintypes import SIZE

x = np.matrix([150, 250, 450, 600, 725])
y = np.matrix([74.3, 127, 230, 289, 367])
m, n = x.size, y.size

X, Y = np.empty((m, 2)), np.empty((n, 1))

X[:,0], X[:,1], Y[:,0] = 1, x, y

X_T, Y_T = X.transpose(), Y.transpose()
X_T_X, Y_T_Y = X_T@X, X_T@Y

inv_X_T_X = np.linalg.inv(X_T_X)

B_B = inv_X_T_X@Y_T_Y

B0, B1 = B_B[0], B_B[1]

print(f"{B_B}, B0 = {B0} och B1 = {B1}")
print("---------------")
print(f"y= {B1}x + {B0}")
import numpy as np

x = np.array([150, 250, 450, 600, 725])
y = np.array([74.3, 127, 230, 289, 367])

X, Y = np.empty((len(x), 2)), np.empty((len(y), 1))

X[:,0], X[:,1], Y[:,0] = 1, x, y

XT_X, YT_Y = X.T@X, X.T@Y

inv_X_T_X = np.linalg.inv(XT_X)

B_B = inv_X_T_X@YT_Y

B0, B1 = B_B[0], B_B[1]

print(f"""{B_B}, B0 = {B0} och B1 = {B1}""")
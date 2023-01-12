import numpy as np

#Element
x = np.array([150, 250, 450, 600, 725])
y = np.array([74.3, 127, 230, 289, 367])

#Skapar tomma arrayes (kallar dem matriser i detta fall)
X, Y = np.empty((len(x), 2)), np.empty((len(y), 1))

#Sätter in elemnten i matriserna
X[:,0], X[:,1], Y[:,0] = 1, x, y

#Ger oss bl.a en 2X2 vilket vi enkelt kan arbeta med
XT_X, YT_Y = X.T@X, X.T@Y

#Skapar inversen till XT_X och multiplicerar på båda sidorna så vi får värderna för [B0, B1]    
B_B = np.linalg.inv(XT_X)@YT_Y

B0, B1 = B_B[0], B_B[1]

print(f"""{B_B}, B0 = {B0} och B1 = {B1}""")
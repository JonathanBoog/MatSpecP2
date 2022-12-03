# INTE FÄRDIG; DET ÄR NÅGOT SOM INTE RIKTIGT FUNGERAR SOM DET SKA; JONATHAN HAR JOBBAT HÄR;


import numpy as np

 
x = np.matrix([1, 2, 3])
m = x.size #Antal tal i x
y = np.matrix([2, 4, 6]) # Hur annars ska jag göra än så här???


A = np.empty((m,2))
A[:,1] = x
A[:,0] = 1
A_T = A.transpose()

VL = np.empty((2,2))
#Vänsterled
for row in range (2):
    for column in range(2):
        sum = 0
        for numbers in range(0, m):
            sum += A_T[row][numbers]*A[numbers][column] #Måste använda numbers innan column för att python är scuffed


        VL[row][column] = sum
print(VL)

#Högerled
HL = np.empty((m))
print(HL)
for row in range(2):
        sum = 0
        for numbers in range(0, m):
            sum += A_T[row][numbers]*y[numbers]


        HL[row] = sum
print(VL)
from numpy import *

ar1 = array([
    [1, 2, 3],
    [4, 5, 6]
])

ar2 = array([
    [1, 4],
    [2, 6],
    [8, 9]
])

res = array([
    [0, 0],
    [0, 0]
])

for i in range(len(ar1)): # Here we find the row number which remains the same till the end of nested loop
    for j in range(len(ar2[0])): # Here we find the column number which remains the same till the end of nested loop
        for k in range(len(ar2)): # Here we find the row numbers for the same column in 2nd array
            res[i][j] += ar1[i][k] * ar2[k][j]

print(res)

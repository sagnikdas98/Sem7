import numpy as np
a = input("Correct Word: ")
b = input("Human Input: ")
mat = np.zeros((len(b)+1, len(a)+1 ))
for i in range (1,len(b)+1):
    for j in range (1,len(a)+1):
        cost = 1
        if(b[i-1] == a[j-1]): cost = 0
        mini = min(mat[i-1][j],mat[i-1][j-1], mat[i][j-1])
        mat[i][j] = int(mini + cost)
print(mat[1:,1:])
print("Min Edit Dis: ", mat[-1][-1])

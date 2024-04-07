import numpy as np
# it is assumed that the matrix used for this calculation must be a square matrix
order = input("Order of Matrix A, rxc: ")
n = eval(order[0])
A = []
Minus_I = []
U = []
LT = []
U = []
# this code arranges the negative identity and the matrix A properly
# Matrix A is defined by user, matrix -I is auto_gen, matrix U and LT are null (default)
for i in range(n):
    row = input(f"Row_{i+1} e.g a,b,c: ")
    resolved = [float(a) for a in row.split(',')]
    # Negative Identity
    I = [0 for c in range(n)]
    I[i] = -1
    # Default Lower Transpose
    L = [0 for c in range(n)]
    L[i] = 1
    # Default Upper Transpose
    upp = [0 for c in range(n)]
    # Default Inverse
    Minus_I.append(I)
    A.append(resolved)
    LT.append(L)
    U.append(upp)

# inter matrix addition multiplication
count = 1

for i in range(1, n+1):
    # xCount it used to know when to shift from updating U values and LT values
    xCount = i
    for k in range(1, n+1):
        interMult = 0
        for j in range(1, n+1):
            mult1 = A[j-1][i-1] * Minus_I[j-1][k-1]
            interMult += mult1
            mult2 = U[j-1][i-1] * LT[j-1][k-1]
            interMult += mult2
            
        rmv = U[i-1][k-1]*LT[i-1][k-1]
        interMult -= rmv
        
        if i==k:
            res = interMult * -1
            U[i-1][k-1] = res
        else:
            if xCount > 0:
                res = interMult * -1
                U[k-1][i-1] = res
            else:
                res = (interMult * -1)/U[i-1][i-1]
                LT[i-1][k-1] = res
        xCount-=1

# converting LT to L
L=[[] for i in range(n)]
for li in LT:
    for ind,l in enumerate(li):
        L[ind].append(l)

# getting L_Inv
L_Mat = np.array(L)
L_Inv = np.linalg.inv(L_Mat)

U_Mat = np.array(U)
U_Inv = np.linalg.inv(U_Mat)

A_Inv = np.matmul(U_Inv, L_Inv)

A_Inv_A = np.matmul(A_Inv, np.array(A))

print({'U': U, 'LT': LT, 'L': L})
print({'U_INV': U_Inv.round(decimals=3).tolist(), 'L_Inv': L_Inv.round(decimals=3).tolist(), 'A_Inv': A_Inv.round().tolist(), 'A_Inv_A': A_Inv_A.round().tolist()})

# A
# 2,1,2
# 4,0,4
# -4,2,-1
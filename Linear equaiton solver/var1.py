import random

A = [16 , 3 , 2 , 13, 34]
B = [5, 10, 11 , 8, 41 ]
C = [9, 6, 7, 12, 34]
D = [5, 15, 14, 1, 35]

if A[0] != 0:
    print(" ")
else:
    if B[0] != 0:
        updatedA = B
        updatedB = A
        A = updatedA
        B = updatedB
    else:
        if C[0] != 0:
            updatedA = C
            updatedC = A
            C = updatedA
            A = updatedC
        else:
            if D[0] != 0:
                updatedA = D
                updatedD = A
                A = updatedA
                D = updatedD
            else:
                print("Infinitely many solutions")

bb0 = B[0] - A[0] * B[0] / A[0]
bb1 = B[1] - A[1] * B[0] / A[0]
bb2 = B[2] - A[2] * B[0] / A[0]
bb3 = B[3] - A[3] * B[0] / A[0]
bb4 = B[4] - A[4] * B[0] / A[0]

cc0 = C[0] - A[0] * C[0] / A[0]
cc1 = C[1] - A[1] * C[0] / A[0]
cc2 = C[2] - A[2] * C[0] / A[0]
cc3 = C[3] - A[3] * C[0] / A[0]
cc4 = C[4] - A[4] * C[0] / A[0]

dd0 = D[0] - A[0] * D[0] / A[0]
dd1 = D[1] - A[1] * D[0] / A[0]
dd2 = D[2] - A[2] * D[0] / A[0]
dd3 = D[3] - A[3] * D[0] / A[0]
dd4 = D[4] - A[4] * D[0] / A[0]

BB = [bb0, bb1, bb2, bb3, bb4]
CC = [cc0, cc1, cc2, cc3, cc4]
DD = [dd0, dd1, dd2, dd3, dd4]

#print(BB, CC, DD)

if BB[1] != 0:
    print(" ")
else:
    if CC[1] != 0:
        updatedBB = CC
        updatedCC = BB
        BB = updatedBB
        CC = updatedCC
    else:
        if DD[1] != 0:
            updatedBB = DD
            updatedDD = BB
            BB = updatedBB
            DD = updatedDD
        else:
            print("Infinitely many solutions")

ccc0 = CC[0] - BB[0] * CC[1] / BB[1]
ccc1 = CC[1] - BB[1] * CC[1] / BB[1]
ccc2 =CC[2] - BB[2] * CC[1] / BB[1]
ccc3 = CC[3] - BB[3] * CC[1] / BB[1]
ccc4 = CC[4] - BB[4] * CC[1] / BB[1]

ddd0 = DD[0] - BB[0] * DD[1] / BB[1]
ddd1 = DD[1] - BB[1] * DD[1] / BB[1]
ddd2 = DD[2] - BB[2] * DD[1] / BB[1]
ddd3 = DD[3] - BB[3] * DD[1] / BB[1]
ddd4 = DD[4] - BB[4] * DD[1] / BB[1]

CCC = [ccc0, ccc1, ccc2, ccc3, ccc4]
DDD = [ddd0, ddd1, ddd2, ddd3, ddd4]

#print(CCC,DDD)

if CCC[2] != 0:
    print(" ")
else:
    if DDD[2] != 0:
        updatedCCC = DDD
        updatedDDD = CCC
        CCC = updatedCCC
        DDD = updatedDDD
    else:
        print("infinitely many solutions")

dddd0 = DDD[0] - CCC[0] * DDD[2] / CCC[2]
dddd1 = DDD[1] - CCC[1] * DDD[2] / CCC[2]
dddd2 = DDD[2] - CCC[2] * DDD[2] / CCC[2]
dddd3 = DDD[3] - CCC[3] * DDD[2] / CCC[2]
dddd4 = DDD[4] - CCC[4] * DDD[2] / CCC[2]

DDDD = [dddd0, dddd1, dddd2, dddd3, dddd4]

#print(DDDD)

ref = [A, BB, CCC, DDDD]
print("matrix",ref)

var4 = DDDD[4] / DDDD[3]
var3 = (CCC[4] - (CCC[3] * var4)) / CCC[2]
var2 = (BB[4] - (BB[3] * var4 + BB[2] * var3)) / BB[1]
var1 = (A[4] - (A[3] * var4 + A[2] * var3 + A[1] * var2)) / A[0]

print("variables", var1, var2, var3, var4)

dev1 = A[4] - (var1 * A[0] + var2 * A[1] + var3 * A[2] + var4 * A[3])
dev2 = BB[4] - (var1 * BB[0] + var2 * BB[1] + var3 * BB[2] + var4 * BB[3])
dev3 = CCC[4] - (var1 * CCC[0] + var2 * CCC[1] + var3 * CCC[2] + var4 * CCC[3])
dev4 = DDDD[4] - (var1 * DDDD[0] + var2 * DDDD[1] + var3 * DDDD[2] + var4 * DDDD[3])

deviationmatrix = [dev1, dev2, dev3, dev4]


deviation = dev1 ** 2 + dev2 **2 + dev3 ** 2 + dev4 ** 2
print("initial deviation:",deviation)

e = []
while deviation >= 0.0000000000000000000000000000000000000000000000000005:
    for i in range(4):
        vale = random.randint(-10, 10)/1000 
        e.append(vale)
    print(e)
    A[4] = A[4] + e[0]
    BB[4] = BB[4] + e[1]
    CCC[4] = CCC[4] + e[2]
    DDDD[4] = DDDD[4] + e[3]

    var4 = DDDD[4] / DDDD[3]
    var3 = (CCC[4] - (CCC[3] * var4)) / CCC[2]
    var2 = (BB[4] - (BB[3] * var4 + BB[2] * var3)) / BB[1]
    var1 = (A[4] - (A[3] * var4 + A[2] * var3 + A[1] * var2)) / A[0]

    dev1 = A[4] - (var1 * A[0] + var2 * A[1] + var3 * A[2] + var4 * A[3])
    dev2 = BB[4] - (var1 * BB[0] + var2 * BB[1] + var3 * BB[2] + var4 * BB[3])
    dev3 = CCC[4] - (var1 * CCC[0] + var2 * CCC[1] + var3 * CCC[2] + var4 * CCC[3])
    dev4 = DDDD[4] - (var1 * DDDD[0] + var2 * DDDD[1] + var3 * DDDD[2] + var4 * DDDD[3])

    deviation = dev1 ** 2 + dev2 ** 2 + dev3 ** 2 + dev4 ** 2
   

    e = []

sonmatrix=[A,BB,CCC,DDDD]
print(A,BB,CCC,DDDD)
print("new variables:",var1, var2, var3, var4)
print("new deviation:",deviation)

#roundoff sorununu şimdi değil sonra çözeceğiz

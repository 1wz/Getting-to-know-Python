N=int(input("введите N "))

#создание рандомного массива
from random import randint
A=[]
for i in range(N):
    A.append(randint(0, 10))
print(A)
#

import math
X=int(input("введите X "))
delta=(0,abs(A[0]-X))
for i in range(1,N):
    localDelta=abs(A[i]-X)
    if localDelta<delta[1]:
        delta=(i,localDelta)

print(A[delta[0]])
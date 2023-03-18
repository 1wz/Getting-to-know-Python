N=int(input("введите N "))

#создание рандомного массива
from random import randint
A=[]
for i in range(N):
    A.append(randint(0, 10))
print(A)
#

X=int(input("введите X "))
count=0
for a in A:
    if a==X:
        count+=1

print(count)
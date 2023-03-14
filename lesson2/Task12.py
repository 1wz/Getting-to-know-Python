import math

sum=int(input("введите сумму "))
cross=int(input("введите произведение "))

D=sum*sum-4*cross
if D<0:
    print("решений нет ")
else:
    a1=(sum+math.sqrt(D))/2
    b1=sum-a1
    print(int(a1),int(b1))



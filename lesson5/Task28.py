def sum(a,b)->int:
    if b==0:
        return a
    return sum(a,b-1)+1

A=int(input("введите а "))
B=int(input("введите Ь "))
print(f"{A}+{B}={sum(A,B)}")
def exponentiation(a,b):
    if b==1:
        return a
    return a*exponentiation(a,b-1)

A=int(input("введите а "))
B=int(input("введите Ь "))
print(f"{A}^{B}={exponentiation(A,B)}")
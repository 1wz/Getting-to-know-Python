a0=int(input("введите первый элемент "))
d=int(input("введите разность "))
n=int(input("введите количество эементов "))
print(a0, end=" ")
for i in range(n-1):
    a0+=d
    print(a0, end=" ")
number=int(input("введите трехзначное число "))
sum=0
sum+=number%10
number//=10
sum+=number%10
number//=10
sum+=number%10
print("сумма цифр = ",sum)
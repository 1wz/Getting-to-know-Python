number=int(input("введите номер билета "))
sum1=0
sum1+=number%10
number//=10
sum1+=number%10
number//=10
sum1+=number%10
number//=10

sum2=0
sum2+=number%10
number//=10
sum2+=number%10
number//=10
sum2+=number%10

if sum1==sum2:
    print("счастливый билет")
else:
    print("несчастливый билет")

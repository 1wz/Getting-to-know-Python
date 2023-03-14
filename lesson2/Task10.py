from random import randint

coins_count=int(input("введите кол-во монеток "))
coins_list=[]
for i in range(coins_count):
    coins_list.append(randint(0, 1))
print(coins_list)
eagles_count=sum(coins_list)
tails_count=coins_count-eagles_count
print(min(eagles_count,tails_count))


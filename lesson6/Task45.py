import math
def sumOfDev(num)->int:
    nMax=int(math.sqrt(num))
    sum=1
    for i in range(2,nMax):
        if num%i==0:
            sum+=i
            sum+=num//i
        if num%nMax==0:
            sum+=nMax
    return sum

N=int(input(""))
arrayOfSum=[0]*N
for i in range(2,N):
    currentSum=sumOfDev(i)
    arrayOfSum[i]=currentSum
    if currentSum<i and arrayOfSum[currentSum]==i:
        print(i,currentSum)



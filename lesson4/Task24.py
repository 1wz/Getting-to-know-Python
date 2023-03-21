strList=input("введите ").split()
intList=[]
for i in strList:
    intList.append(int(i))

count =len(intList)
currentSum=intList[0]+intList[1]+intList[2]
maxSum=currentSum
for i in range(count-1):
    currentSum=currentSum-intList[i]+intList[(i+3)%count]
    if maxSum<currentSum:
        maxSum=currentSum
print(maxSum)
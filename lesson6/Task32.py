def inputInt(massage:str):
    strList=input(massage+" ").split()
    intList=[]
    for i in strList:
        intList.append(int(i))
    return intList

array=inputInt("введите массив")
Range=inputInt("введите диапазон")
indexes=[]
for i in range(len(array)):
    if(Range[0]<=array[i]<=Range[1]):
        indexes.append(i)

print(indexes)
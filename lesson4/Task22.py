n=input("введите размеры наборов ").split()
n1=int(n[0])
n2=int(n[1])
#не понял зачем эти строки, потом посмотрел решение и... еще раз не понял


list1=input("введите первый набор ").split()
list2=input("введите второй набор ").split()
resultSet=(set(list1)&set(list2))
resultList=[]
for i in resultSet:
    resultList.append(int(i))
resultList.sort()
print(resultList)
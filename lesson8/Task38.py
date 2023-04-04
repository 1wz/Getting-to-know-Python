'''
w - вывести весь справичник
a [string] - добавить запись
s [string] - поиск
c [INDEX] [string] - заменить запись
d [INDEX] - удалить
q - выйти и сохранить
'''


def load(path:str)->list:
    result=[]
    with open(path,"r",encoding="UTF-8") as f:
        [result.append(line) for line in f]
    return result

def append(str,list):
    list.append(str+"\n")

def search(str:str,list:list)->list:
    [print(f"[{i}] {line}") for (i,line) in enumerate(list) if str.casefold() in line.casefold()]

def write(list):
    [print(f"[{i}] {line}") for (i,line) in enumerate(list)]

def change(i:int,str:str,list:list):
    list[i]=str+"\n"

def save(path:str,list:list):
    with open(path,"w",encoding="UTF-8") as f:
        [f.write(line) for line in list]

def delit(i:int,list:list):
    list.__delitem__(i)

def split_args(str:str):
    first=""
    i=0
    while(i<len(str) and str[i]!=" "):
        first+=str[i]
        i+=1
    if i>=len(str):
        return (first,"")
    others=str[i+1:]
    return (first,others)

path="guide.txt"
guide=load(path)
while((inp:=input("введите команду "))!="q"):
    (command,args)=split_args(inp)
    if inp=="w":
        write(guide)
        continue
    if args!="":
        if command=="a":
            append(args,guide)
            continue
        if command=="s":
            search(args,guide)
            continue
        (index,str)=split_args(args)
        index=int(index)
        if 0<=int(index)<len(guide):
            if command=="c" and str!="":
                change(index,str,guide)
                continue
            if command=="d":
                delit(index,guide)
                continue
        print("некорректно введена команда ")
save(path,guide)

    
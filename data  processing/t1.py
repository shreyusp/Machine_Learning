str1=input("enter string1")
str2=input("enter string2")
def count_unique(str1,str2):
    str=str1+str2
    count=0
    exist=[]
    str.split()
    for letter in str:
        if letter in exist:
            count=count+0
            
        else:
            count+=1
            exist.append(letter)
    print(count)

count_unique(str1,str2)

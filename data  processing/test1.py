def count_unique(s1,s2):
    s=s1+s2
    count=0
    dict1=dict()
    for i in range(len(s)):
        if s[i] in dict1.keys():
               dict1[s[i]]=dict1[s[i]]+1
        else:
               dict1[s[i]]=1
    for key in dict1.keys():
        if dict1[s[i]].values()==0:
            count=count+1
    return count
print("Enter two strings: ")
s1=input("s1:")
s2=input("s2:")
print("No. of unique charachters=",count_unique(s1,s2))


                
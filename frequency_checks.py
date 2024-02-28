list1=[1,2,3,1,4,5,2,1,3,1,6,6]
count=0
element=0
for i in range(0,len(list1)):
    count=0
    for j in range(0,len(list1)):
        if list1[i] is list1[j]:
            count+=1
            element=list1[i]
print(f"{list1[i]} is {count} times repeated")     

 

list1=[1,2,3,1,4,5,2,1,3,1,6,6]
count=0
check=[]
#element=int(input("enter the number : "))
for i in range(0,len(list1)):
    count=0
    if list1[i] not in check:
        for j in range(0,len(list1)):
            if list1[i]==list1[j]:
                count=count+1
                element=list1[i]
                check.append(element)
                
        print(f"{element} is {count} times repeated")     

 

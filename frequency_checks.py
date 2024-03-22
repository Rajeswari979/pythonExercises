list1=[1,2,3,1,4,5,2,1,3,1,6,6]
count=0
element=int(input("enter the element to check : "))

for j in list1:
    if j == element:
        count+=1

print(f"{element} is {count} times repeated")     

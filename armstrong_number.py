string=input("enter the number")
numbers=list(string)
addition=0


for number in numbers:
    addition+=pow(int(number),len(string))
    
   
answer=str(addition)

if answer == string:
    print(f"{string} is Armstrong number")
else:
    print(f"{string} is not a Armstrong number")
    

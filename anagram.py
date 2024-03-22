number1=input("enter a number")
string1=list(number1)
number2=input("enter a number")
string2=list(number2)
count=0
if len(string1)== len(string2):
    for i in string1:
        if i in string2:
            count+=1
    if count==len(string2):
        print(f"The given string is anagram")
    else:
        print("The given string is not anagram")
                
else:
    print("Please, enter the right string ")
        

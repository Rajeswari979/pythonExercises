
status=0
for i in [23,45,78,71,83,4,6,78]:
    status=0
    if i==1 or i==2:
        print(f"{i} is a prime number")
    else:
        for j in range(2,i):
            if i%j==0:
                status=1

        if status != 1 :
            print(f"{i} is a prime number")    
        else:
            print(f'{i} is a not prime number')

            

#include <stdio.h>

int main() {
    // Write C code here
    int n=3,i,j;
    int check=0;
    for(j=21;j<40;j++)
    {
        check=0;
    for (i=2;i<j;i++)
    {
        if (j%i==0)
        {
            check=1;
        }
    }
    if (check ==0)
    {
        printf("\n %d is prime number",j);
    }
    else
    {
    printf("\n %d is not a prime number",j);
    }
    }


    return 0;
}

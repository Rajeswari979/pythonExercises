#include <stdio.h>

int main() {
    // Write C code here
    int n=3,i;
    int check=0;
   
    for (i=2;i<n;i++)
    {
        if (n%i==0)
        {
            check=1;
        }
    }
    if (check ==0)
    {
        printf("%d is prime number",n);
    }

    return 0;
}

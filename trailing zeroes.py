import math
def trailnum(x):
    count=0
    while(x%10==0):
        count=count+1
        x=x//10

    return(count)

n=int(input('enter number of test cases:'))
for i in range(n):
    z=int(input('enter the number:'))
    f=math.factorial(z)
    print('the number of zeroes in the end is:',trailnum(f))
   


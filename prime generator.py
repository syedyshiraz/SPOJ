import math
def isprime(n):
    m=2
    while True:
        if(n==2 or n==3):
            m=1
            break
        elif(n==1):
            m=0
        else:
            m=1
            for i in range(2,n//2+1):
                if(n%i==0):
                    m=0
                    break
            
        break
                
    return(m==1)
num=int(input('enter the number of test cases:'))
for j in range(num):
   a,b=map(int,input().split())
   print('printing prime numbers from',a,'to',b)
   for k in range(a,b+1):
      if(isprime(k)==True):
        print(k)
            
  
                           

n=int(input("enter the number of fibonacci numbers to be displayed(starts from 1): "))
t1=0
t2=1
t=1
strin=''
for i in range(n):
   print(t,end=' ')
   t=t1+t2
   t1=t2
   t2=t
   
    
    

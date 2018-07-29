t=int(input('enter test cases:'))
for i in range(t):
    if(i>0):
        print('\n')
    print('enter number of columns to be printed and char per line:',end='')
    x,y=map(int,input().split())
    print('printing',x,'number of lines')
    print('printing',y,'number of columns in the pattern')
    for j in range(x):
         if(j>0):
             print('\n')
         for k in range(y):
            if(j+k)%2==0:
                 print('*',end='')
            else:
                  print('.',end='')
           

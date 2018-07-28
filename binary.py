i=int(input("enter the number to be converted to binary: "))
s=''
while(i>0):
    s=s+str(i%2)
    i=i//2

print(s[::-1])

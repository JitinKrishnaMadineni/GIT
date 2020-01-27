s=input().split(',')
l=[]
j=len(s)
for i in range(0,j):
    l.append(int(s[i]))
a=l[0]
b=l[1]
if(a<b):
    k=b
else:
    k=a
for i in range(1,k+1):
    if ((a%i==0) and (b%i==0)):
        y=i
print(y)
    
    

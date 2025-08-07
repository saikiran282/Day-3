#Right-angle triangle print using stars
n=int(input())
p=n
for i in range(1,n+1):
    print('* '*i)

while(p>0):
    print('* '*(n-(p-1)))
    p-=1

#priramid star
#method1
n=int(input())
for i in range(1,n+1):
    s=(n-i)
    print(" "*s+"* "*i)
#method2
t=n
while(t>0):
    s=(n-(t-1))
    print(" "*(t-1)+"* "*s)
    t-=1
    

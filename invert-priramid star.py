#invert-priramid star
n=int(input())
m=n
for i in range(n,0,-1):
    s=(n-i)
    print(" "*s+"* "*i)

while(m>0):
    s=(n-m)
    print(" "*s+"* "*m)
    m-=1

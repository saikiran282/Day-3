#method1
n=int(input())
for i in range(n,0,-1):
    str1="" 
    for k in range(i,0,-1):
        str1=str1+str(k)+" " 
    print(str1)
#method2
o=n
s=o   
while(o>0):
     str1=""
     s=o
     while(s>0):
         str1=str1+str(s)+" "
         s-=1
     print(str1)
     o-=1

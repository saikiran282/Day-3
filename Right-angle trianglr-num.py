#Right-angle triangle print using numbers
n=int(input())

for i in range(n,0,-1):
    str1="" 
    for k in range(1,i+1):
        str1=str1+str(k)+" "
    print(str1)

#meth1
n=5
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)
#meth2
fact1=1
for i in range(n,1,-1):
     fact1*=i
print(fact1)
#meth3
fact2=1
k=1
while (k<n+1):
    fact2*=k
    k+=1
print(fact2)
    

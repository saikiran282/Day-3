list=[1,5,8,2,6,8]
target=8
k=0
for i in range(len(list)):
    if target==list[i]:
        print(i)
        break
while (k<len(list)):
    k+=1
    if target==list[k]:
        print(k)
        break
    

            

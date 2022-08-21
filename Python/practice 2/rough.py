l1 =[2,3,9]
l2=[1,2,3]
l1.reverse()
l2.reverse()
l3=[]
for i in range(len(l1)):
    l3.append(l1[i]+l2[i])

print(l3)
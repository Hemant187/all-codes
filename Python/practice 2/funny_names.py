n = int(input('Enter the number of friends:\n '))
name=[]
lname=[]
for i in range(n):
    i= input(f"Enter the name of {i+1} friend\n")
    # i = i.split(' ')
    name.append(i[0])
    lname.append(i[1])
import random
funname =[]

for element in range(0,n-1):
    
    s1 = random.randint(0,n-1)
    fun = name[s1] + lname[s1]
    funname.append(fun)
    element +=1
    print(funname)
# Least Comman Number
a = int(input("Enter the first number\n"))
b = int(input("Enter the second number\n"))

MaxNum = max(a,b)
while(True):
    if MaxNum%a ==0 and MaxNum%b==0:
        break
    MaxNum+=1

print(f"The Lcm of {a},{b} is {MaxNum}")
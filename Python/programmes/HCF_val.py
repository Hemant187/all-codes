# Highest Comman factor
# GCD
a = int(input('Enter your 1st number\n'))
b = int(input('Enter your 2nd number\n'))

MinNum = min(a, b)
# print(MinNum)


# # Method 1st
for i in range(1, MinNum+1):
    if a % i == 0 and b % i == 0:
        hcf = i
print(f"The HCF/GCD of {a},{b} is {hcf}")


# Method 2nd
# while(True):
#     if a % MinNum == 0 and b % MinNum == 0:
#         break
#     MinNum -= 1

# print(f"The Hcf of {a},{b} is {MinNum}")

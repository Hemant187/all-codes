# Divide the apple
try:
    n = int(input('Enter number of apples:'))
    mn = int(input('Minimum number to check:'))
    mx = int(input('Maximum number to check:'))
except:
    print('Enter Integer only!')
    exit()
if mn>mx:
    print('This can not be the range as the min should be less than max')
if mn == mx:
    print("This is not a range and mn is equal to mx")
    if n%mn == 0:
        print(f'{mn} is a divisor of {n}')
    elif n%mn != 0:
        print(f'{mn} is a not divisor of {n}')
else:
    for i in range(mn,mx+1):
        if n%i == 0:
            print(f"{i} is a divisor of {n}")
        elif n%i != 0:
            print(f"{i} is not a divisor of {n}")
    
        
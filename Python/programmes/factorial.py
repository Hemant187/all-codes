def factorial(number):
    if number ==0 or number ==1:
        return 1
    else:
        return number *factorial(number-1)
def factorialTrailingZeros(number):
    fac = factorial(number)
    print(fac)
    count =0
    while (fac%10 ==0):
        count += 1
        fac = fac/10
    return count
'''i =5
while(number//i !=0):
    count += int(number/i)
    i = i+5
return count'''


if __name__ == '__main__':
    number = int(input('Enter a number: '))
    fac = factorial(number)
    print(f'The factorial is {fac}')
    print(factorialTrailingZeros(number))
 
def is_palindrome(n):
    n= str(n)
    return str(n)==str(n)[::-1]
def next_palindrome(n):
    n=n+1
    while not is_palindrome(n):
        n+=1
    return n
    

if __name__ =='__main__':
    n = int(input('Enter numbers the number of test cases: '))
    numbers  =[]
    for i in range(n):
        numbers.append(int(input("Enter the number: ")))
    
    for i in range(n):
        print(f'Next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}')
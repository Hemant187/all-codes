
def merafun():
    print('''choose the operation:
            + for addition
            - for subtraction
            * for mulpitly
            / for divition''')
    operation = input()
    print('enter first number')
    a=int(input())
    print('enter second number')
    b=int(input())




    if operation =='+':
        print(a+b)
    elif operation =='-':
        print(a-b)
    elif operation =='*':
        print(a*b)
    elif operation =='/':
        print(a/b)
    else:
        print('invalid key')

    again()

def again():
    n =input('press y for again calculate: ' )
    if n=='y':
        merafun()
    else:
        exit()

    
merafun()

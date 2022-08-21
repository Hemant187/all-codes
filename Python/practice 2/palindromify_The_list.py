'''Hemant
5 april 2022'''



def is_palindrome(n):
    n= str(n)
    return n==n[::-1]

def next_palindrome(n):
    n=n+1
    while not is_palindrome(n):
        n+=1
    return n

if __name__ == '__main__':
    n= int(input("Enter the number of case in list:\n"))
    numb_list =[]
    for element in range(n):
        Number= int(input('Enter the list element:\n'))
        numb_list.append(Number)
    print(f"You have entered {numb_list}")
    print(f"output list: {list(numb_list[i] if numb_list[i]<10 else next_palindrome(numb_list[i]) for i in range(n))}")

    # new_list=[]
    # for element in numb_list:
    #     if element >10:
    #         n = next_palindrome(element)
    #         new_list.append(n)
    #     else:
    #         new_list.append(element)


    # print(f"output List: {new_list}")

    

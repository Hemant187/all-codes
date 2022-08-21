def rohanTable(number):
    import random
    wrong = random.randint(1,9)
    table= [number*i for i in range(1,11)]
    table[wrong] = table[wrong] + random.randint(1,9)
    return table
    
def myTable(table,number):
    for i in range(1,11):
        if table[i-1]!=i*number:
            return i-1
    return None

if __name__ == "__main__":
    number = int(input("Enter the number\n"))
    table= rohanTable(number)
    print(table)
    wrongindex =(myTable(table,number))
    print('The Wrong index is',wrongindex)
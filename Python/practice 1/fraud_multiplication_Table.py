import random

def RohanTable(number):
    wrong = random.randint(1,9)
    Table = [i* number for i in range(1,11)]
    Table[wrong] = Table[wrong] + random.randint(2,10)
    return Table


# print(RohanTable(4))

def is_correct(Table,number):
    for i in range(1,11):
        if Table[i-1] != i*number:
            return i-1
    return None
    

if __name__ == '__main__':
    number = int(input("Enter a number: "))
    myTable = RohanTable(number)
    print(myTable)
    wrongindex = is_correct(myTable, number)
    print(f"The wrong index is {wrongindex}")


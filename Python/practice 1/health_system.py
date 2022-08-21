def gettime():
    import datetime
    return datetime.datetime.now()

def take(k):
    if k==1:
        c=int(input('Enter 1 for exercise or 2 for food '))
        if c==1:
            value= input('text here \n')
            with open('Hemant_ex.txt', 'a') as op:
                op.write(str([str(gettime())])+': '+value+'\n')
            print('Successful Written')
        elif c==2:
            value = input('text here \n')
            with open('Hemant_food.txt','a') as op:
                op.write(str([str(gettime())])+': '+value+'\n')
            print('Successful Written')
    elif k==2:
        c=int(input('Enter 1 for exercise or 2 for food '))
        if c==1:
            value= input('text here \n')
            with open ('Anurag_ex.txt', 'a') as op:
                op.write(str([str(gettime())])+': '+value+'\n')
            print('Successful Written')
        elif c==2:
            value = input('text here \n')
            with open('Anurag_food.txt','a') as op:
                op.write(str([str(gettime())])+': '+value+'\n')
            print('Successful Written')
    elif k==3:
        c=int(input('Enter 1 for exercise or 2 for food '))
        if c==1:
            value= input('text here \n')
            with open ('Shubham_ex.txt', 'a') as op:
                op.write(str([str(gettime())])+': '+value+'\n')
            print('Successful Written')
        elif c==2:
            value = input('text here \n')
            with open('Shubham_food.txt','a') as op:
                op.write(str([str(gettime())])+': '+value+'\n')
            print('Successful Written')
    
    else: 
        print('Please Enter valid input (1(Hemant),2(Anurag),3(Shubham))')

def retrieve(k):
    if k==1:
        c=int(input('Enter 1 for exercise or 2 for food '))
        if c==1:
            with open("Hemant_ex.txt") as op:
                for i in op:
                    print(i, end=" ")
        elif c==2:
            with open('Hemant_food.txt') as op:
                for i in op:
                    print(i, end=" ")

    elif k==2:
        c=int(input('Enter 1 for exercise or 2 for food '))
        if c==1:
            with open('Anurag_ex.txt') as op:
                for i in op:
                    print(i, end=" ")
        elif c==2:
            with open('Anurag_food.txt') as op:
                for i in op:
                    print(i, end=" ")
    elif k==3:
        c=int(input("Enter 1 for exercise or 2 for food"))
        if c==1:
            with open('Shubham_ex.txt') as op:
                for i in op:
                    print(i,end=" ")
        elif c==2:
            with open('Shubham_food.txt') as op:
                for i in op:
                    print(i,end='')
    else:
        print('Please Enter valid input (1:Hemant,2:Anurag,3:Shubham)')
print("Health Management system: ")
choice=int(input('Press 1 for log the value and 2 for retrieve '))
# name= int(input("Enter 1 for Hemant's details or 2 for Anurag's details or 3 for Shubham's details: "))
if choice ==1:
    name=int(input("Press 1 for Hemant, 2 for Anurag, 3 for Shubham: "))
    take(name)
if choice==2:
    name=int(input("Press 1 for Hemant, 2 for Anurag, 3 for Shubham:"))
    retrieve(name)
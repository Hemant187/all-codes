from numpy import bool_


num =int(input('Enter number of rows: '))
val =int(input('Enter 0 for false or 1 for true: '))
bool_val =bool_(val)
if bool_val == True:
    for i in range(0,num+1):
        print('*'*i)
if bool_val == False:
    for i in range(num,0,-1):
        print('*'* i)
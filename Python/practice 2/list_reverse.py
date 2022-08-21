#  Take the size of the list from the user
try:
    size = int(input('Enter size of list:\n'))
    mylist =[]
    # Take the element of the list from the user
    for i in range(size):
        mylist.append(int(input('enter list element:\n')))
except:
    print('Enter only integers!')
reverse1 =mylist[:] #[:] This will make a copy of mylist in reverse1
reverse1.reverse()
print(f'My first reversed list of {mylist} is {reverse1}\n')

reverse2 =mylist[::-1]
print(f'My second reversed list of {mylist} is {reverse2}\n')

reverse3 = mylist[:]
for i in range(len(mylist)//2):
    reverse3[i],reverse3[len(reverse3) -i -1] = reverse3[len(reverse3) -i -1],reverse3[i]
    # print(f'the reversed list at i={i} is {reverse3}')

print(f'My second reversed list of {mylist} is {reverse3}\n')

if reverse1 ==reverse2 and reverse2 == reverse3:
    print('All three methods give same result')

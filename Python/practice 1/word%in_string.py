print('welcome to my code . I am an application that takes a message and a letter from you . My task is to count how many times this letter occured and to calculate its percentage')

message_user = str(input('enter your message: '))
word = str(input('enter your letter: '))
cot= len(message_user)
opr = message_user.count(word)
percentage = (opr/cot)*100
print('lenght of message is',cot)
print(f'The count of the {word} is {opr}\nThe persentage of the {word} is {percentage}')

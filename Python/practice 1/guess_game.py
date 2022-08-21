from random import randint
n =randint(a=0,b=15) #it automatic generate random number between a and b
print(n)
number_of_guesses =1
print('you have 9 attempt for guessing a number')
while number_of_guesses<=9:
    guess_number = int(input('guess the number: '))
    if guess_number==n:
        print("You Won! your guess is right ")
        break
    elif guess_number<n:
        print('your guess is too small')
    elif guess_number>n:
        print('your guess is too big')
    number_of_guesses +=1
    print(f"you have left only {10-number_of_guesses} attempt")
    if number_of_guesses==9:
        print('you have no attempt left')
    else:
        print('invalid key')


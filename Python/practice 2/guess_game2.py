'''Hemant
06 April 2022'''
import random


def guessGame(a, b, actual):
    guess = int(input(f'Guess a number between {a} and {b}\n'))
    nguess = 0
    while guess != actual:
        if guess < actual:
            guess = int(input('Enter a bigger number\n'))
            nguess += 1
        else:
            guess = int(input('Enter a smaller number\n'))
            nguess += 1

    print(f"You guess the correct number in {nguess} turns\n")
    return nguess


if __name__ == '__main__':
    a = int(input('Enter the value of a\n'))
    b = int(input('Enter the value of b\n'))
    actual1 = random.randint(a, b)
    print("Player 1's turn: ")
    g1 = guessGame(a, b, actual1)
    actual2 = random.randint(a, b)
    print("Player 1's turn: ")
    g2 = guessGame(a, b, actual2)
    if g1 > g2:
        print('Player 1 won the match')
    elif g1 < g2:
        print('Player 2 won the match')
    else:
        print("Game Tie!")

    print(
        f"The number of player 1 was {actual1} and for Player 2 was {actual2}")


# import random
# a= int(input("Enter the value of a\n"))
# b= int(input("Enter the value of b\n"))
# i=0
# j=0
# r = random.randint(a,b)
# # print(r)
# print("Player 1:")
# while(1):
#     i+=1
#     player1 = int(input(f"Please guess the number between {a} and {b}\n"))
#     if player1>r:
#         print('Wrong! guess a smaller number again')
#     if player1<r:
#         print('Wrong! guess a greater number again')
#     if player1==r:
#         print(f'correct, You took {i} trail to guess the number.')
#         break
# print("Player 2:")
# r = random.randint(a,b)
# # print(r)
# while(1):
#     j+=1
#     player2 = int(input(f"Please guess the number between {a} and {b}\n"))
#     if player2>r:
#         print('Wrong! guess a smaller number again')
#     if player2<r:
#         print('Wrong! guess a greater number again')
#     if player2==r:
#         print(f'correct, You took {j} trail to guess the number.')
#         break

# if i==j:
#     print('Game Tie!')
# elif i>j:
#     print('Player 1 wins!')
# else:
#     print("Player 2 wins")

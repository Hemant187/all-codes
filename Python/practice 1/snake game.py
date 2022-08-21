# snake,water or gun Game
chance = 10
n = 1
comp_sc = 0
player_sc = 0
print('You have only 9 chances')
while n <= chance:

    import random

    def gameWin(comp, you):
        if comp == you:
            return None
        elif comp == 's':
            if you == "w":
                print('saap pani pi gya!!')
                return False
            elif you == 'g':
                print("saap ko goli se uda diya!!")
                return True
        elif comp == 'w':
            if you == "g":
                print('gun pani pe duuub gyi')
                return False
            elif you == 's':
                print('Saap ne pani pi liya')
                return True
        elif comp == 'g':
            if you == "s":
                print('gun se saap ko maar diya')
                return False
            elif you == 'w':
                print('gun pani me kharab ho gyi')
                return True

    # a=input("comp Turn: Snake(s) Water(w) or Gun(g)?")
    # randNO = random.randint(1,3)
    # if randNO==1:
    #     comp ='s'
    # elif randNO==2:
    #     comp ='w'
    # elif randNO==3:
    #     comp='g'
    L1 = ['s', 'g', 'w']
    comp = random.choice(L1)

    you = input("your Turn: Snake(s) Water(w) or Gun(g)?")

    a = gameWin(comp, you)

    print(f'computer chosse {comp}')
    print(f'you chosse {you}')
    if a == None:
        print("The game is a tie!")
    elif a == True:
        player_sc += 1
        print("you win!!")
    else:
        comp_sc += 1
        print("you loss!!")

    n += 1
    print(f"You have only {chance-n} chance left")

    print(f'Player score: {player_sc}')
    print(f'computer score: {comp_sc}')
    if n == chance:
        print('Game over')
        break
print("overall result")
if player_sc > comp_sc:
    print("Player win! ")
elif comp_sc > player_sc:
    print('Computer Win! ')
else:
    print("Game Tie!")
def sum(a, b, c):
    return a+b+c


def printboard(xstate, zstate):
    zero = 'X' if xstate[0] == 1 else ('O' if zstate[0] == 1 else 0)
    one = 'X' if xstate[1] == 1 else ('O' if zstate[1] == 1 else 1)
    two = 'X' if xstate[2] == 1 else ('O' if zstate[2] == 1 else 2)
    three = 'X' if xstate[3] == 1 else ('O' if zstate[3] == 1 else 3)
    four = 'X' if xstate[4] == 1 else ('O' if zstate[4] == 1 else 4)
    five = 'X' if xstate[5] == 1 else ('O' if zstate[5] == 1 else 5)
    six = 'X' if xstate[6] == 1 else ('O' if zstate[6] == 1 else 6)
    seven = 'X' if xstate[7] == 1 else ('O' if zstate[7] == 1 else 7)
    eight = 'X' if xstate[8] == 1 else ('O' if zstate[8] == 1 else 8)
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")


def checkwin(xstate, zstate):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
            [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum(xstate[win[0]], xstate[win[1]], xstate[win[2]]) == 3:
            print("X won the match")
            return 1
        if sum(zstate[win[0]], zstate[win[1]], zstate[win[2]]) == 3:
            print("O won the match")
            return 0
    return -1


if __name__ == "__main__":
    xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1 of X or 0 of O
    print("Welcome to Tic-Tac-Toe Game")
    while(True):
        printboard(xstate, zstate)
        if turn == 1:
            print("X's Chance")
            value = int(input('Enter the value: '))
            xstate[value] = 1
        else:
            print("O's Chance")
            value = int(input('Enter the value: '))
            zstate[value] = 1
        cwin = checkwin(xstate, zstate)
        if cwin != -1:
            print('Game Over')
            break
        turn = 1-turn
    q = input()

import time
from os import system

def choosing_position(ply):
    while True:
        pos = int(input('{}, Please select a position (not an already used slot): '.format(ply)))
        if pos < 1 or pos > 9:
            print('ERROR! Please enter a place in range 1-9.')
            continue
        result = SIL(shape, pos)
        if result == -1:
            print('ERROR! Please enter another place, This is already selected.')
            continue
        else:
            shape[result[0]][result[1]] = ply
            break

def clear_console():
    """In this function, we clear the console"""
    system('cls')

def show_players(ply1, ply2):
    """This function keeps players on the console for 5 seconds"""
    print("The player1 is: {}\nThe player2 is: {}".format(ply1, ply2))
    counter = 5
    while counter >= 1:
        print('After {}s you will go to the next page'.format(counter))
        counter -= 1
        time.sleep(1)
        print("\033[A{}\033[A".format(38*' '))

def SIL(ls_2D, item):
    """SIL stands for <searching in list>"""
    for i, ls in enumerate(ls_2D):
        if item in ls:
            return list((i, ls.index(item)))
    return -1

def check_winner(shape):
    """In this function, we examine the winning modes of each player"""
    if len(set(shape[0])) == 1:
        winner = shape[0][0]
        if winner == ply1: return 'The player1 wins.'
        else: return 'The player2 wins.'
    elif len(set(shape[1])) == 1:
        winner = shape[1][0]
        if winner == ply1: return 'The player1 wins.'
        else: return 'The player2 wins.'
    elif len(set(shape[2])) == 1:
        winner = shape[2][0]
        if winner == ply1: return 'The player1 wins.'
        else: return 'The player2 wins.'
    elif shape[0][0] == shape[1][0] == shape[2][0]:
        winner = shape[0][0]
        if winner == ply1: return 'The player1 wins.'
        else: return 'The player2 wins.'
    elif shape[0][1] == shape[1][1] == shape[2][1]:
        winner = shape[0][1]
        if winner == ply1: return 'The player1 wins.'
        else: return 'The player2 wins.'
    elif shape[0][2] == shape[1][2] == shape[2][2]:
        winner = shape[0][2]
        if winner == ply1: return 'The player1 wins.'
        else: return 'The player2 wins.'
    elif shape[0][0] == shape[1][1] == shape[2][2]:
        winner = shape[0][0]
        if winner == ply1: return 'The player1 wins.'
        else: return 'The player2 wins.'
    elif shape[0][2] == shape[1][1] == shape[2][0]:
        winner = shape[0][2]
        if winner == ply1: return 'The player1 wins.'
        else: return 'The player2 wins.'
    else:
        return -1

def check_the_end(ls_2D):
    """This function checks whether they are equal or not"""
    SumOfString = 0
    for ls in ls_2D:
        SumOfString += ls.count('X') + ls.count('O') + ls.count('x') + ls.count('o')
    if SumOfString == 9:
        return 1

ply1 = str()
ply2 = str()
shape = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]

step = 1
while True:
    print('Welcome to simple tic tac toe game!')
    print('   {}   |   {}   |    {}\n'
          '-----------------------\n'
          '   {}   |   {}   |    {}\n'
          '-----------------------\n'
          '   {}   |   {}   |    {}'
          .format(shape[0][0], shape[0][1], shape[0][2],
                  shape[1][0], shape[1][1], shape[1][2],
                  shape[2][0], shape[2][1], shape[2][2]))

    if check_winner(shape) != -1:
        print(check_winner(shape))
        counter_of_error_win = 0
        while True:
            question = input('Do you want to play from the beginning (Y,N)? ')
            if question == 'Y':
                shape = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
                step = 1
                Flag_win = 'Y'
                clear_console()
                break
            elif question == 'N':
                for i in range(counter_of_error_win):
                    print("\033[A{}\033[A".format(100*' '))
                print("\033[A{}\033[A".format(100 * ' '))
                print("\033[A{}\033[A".format(100*' '))
                print('Thank you for playing, Goodbye ^-^')
                Flag_win = 'N'
                break
            else:
                print("\033[A{}\033[A".format(100 * ' '))
                print('ERROR! Please choose between Y and N ')
                counter_of_error_win += 1
        if Flag_win == 'Y':
            continue
        elif Flag_win == 'N':
            break

    elif check_the_end(shape):
        print('No one won! You are equal.')
        counter_of_error_end = 0
        while True:
            question = input('Do you want to play from the beginning (Y,N)? ')
            if question == 'Y':
                shape = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
                Flag_end = 'Y'
                step = 1
                clear_console()
                break
            elif question == 'N':
                for i in range(counter_of_error_end):
                    print("\033[A{}\033[A".format(100*' '))
                print("\033[A{}\033[A".format(100*' '))
                print("\033[A{}\033[A".format(100*' '))
                print('Thank you for playing, Goodbye ^-^')
                Flag_end = 'N'
                break
            else:
                print("\033[A{}\033[A".format(100 * ' '))
                print('ERROR! Please choose between Y and N ')
                counter_of_error_end += 1
        if Flag_end == 'Y':
            continue
        elif Flag_end == 'N':
            break

    if step == 1:
        Flag_error = False
        while True:
            if Flag_error:
                print("\033[A{}\033[A".format(100 * ' '))
            ply1 = input('Would you choose x/X as player 1 or o/O? ')
            if ply1 == 'X' or ply1 == 'x':
                if ply1 == 'X':
                    ply2 = 'O'
                elif ply1 == 'x':
                    ply2 = 'o'
                break
            elif ply1 == 'O' or ply1 == 'o':
                if ply1 == 'O':
                    ply2 = 'X'
                elif ply1 == 'o':
                    ply2 = 'x'
                break
            else:
                Flag_error = True
        show_players(ply1, ply2)

    elif step % 2 == 0:
        choosing_position(ply1)
    elif step % 2 == 1:
        choosing_position(ply2)

    step += 1
    clear_console()

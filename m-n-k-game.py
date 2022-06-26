

import numpy as np
import sys





def initialize() -> np.array:
    # initial_params = [int(x) for x in (input('Insert expected initial parameters: field size [m, n] and length of winning join [k]!').split())]
    # m, n, k = initial_params[0], initial_params[1], initial_params[2]

    m, n, k = 10, 15, 2

    if (k > m) & (k > n):  
        sys.exit('The game cannot be played. k needs to be smaller!')
    
    return np.zeros((m, n), dtype=int), k
    


def is_win(x, y, dir_x, dir_y, k, array, player) -> bool:  # considers only end of the line addition!
    if k == 0:
        return True
    
    if array[x, y] != player:
        return False
    
    return is_win(x + dir_x, y + dir_y, dir_x, dir_y, k - 1, array, player)


def move(array, k, player):  # check and change considering is_win(), returns array and bool - win
    correct_move = True
    while(correct_move == False):
        correct_move = True
        try:
            movement = [int(x) for x in (input(f'Player {player} is on the move! [x, y]').split())]
            x, y = movement[0], movement[1]
            if array[x, y] != 0:
                print('Selected spot is not empty!')
                correct_move = False

        except:
            print('This move cannot be done!')
            correct_move = False

    return is_win(x, y, -1, -1, k, player) or is_win(x, y, -1, 0, k, player) ...



def game():
    game_board, k = initialize()
    
    r = is_win(5, 4, -1, 1, k, game_board, 1)
    print(r)

    game_board[5, 4] = 1
    game_board[4, 5] = 1

    r = is_win(5, 4, -1, 1, k, game_board, 1)
    print(r)
    print(game_board)





if __name__=='__main__':
    game()

print('Yay')
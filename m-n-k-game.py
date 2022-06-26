

import numpy as np
import sys





def initialize() -> np.array:
    # initial_params = [int(x) for x in (input('Insert expected initial parameters: field size [m, n] and length of winning join [k]!').split())]
    # m, n, k = initial_params[0], initial_params[1], initial_params[2]

    m, n, k = 10, 15, 5

    if (k > m) & (k > n):  
        sys.exit('The game cannot be played. k needs to be smaller!')
    
    return np.zeros((m, n), dtype=int)
    


def is_win(x, y, dir_x, dir_y, k, array) -> bool:  # check
    if k == 0:
        return True
    
    if array[x, y] != 0:
        return False
    
    return is_win(x + dir_x, y + dir_y, dir_x, dir_y, k - 1, array)


def move():
    ...


def game():
    game_board = initialize()
    

    print(game_board)





if __name__=='__main__':
    game()

print('Yay')
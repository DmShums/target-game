from typing import List
import random
import string

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    lis = []
    for i in range(3):
        temporary_list = []
        for j in range(3):
            temporary_list.append(random.choice(string.ascii_letters).lower())
        lis.append(temporary_list)
    return lis

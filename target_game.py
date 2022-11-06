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
# print(generate_grid())

def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    >>> get_words('en.txt', ['w', 'u', 'm', 'r', 'o', 'v', 'k', 'i', 'f'])
    ['fork', 'form', 'forum', 'four', 'fowk', 'from', 'frow', 'irok', 'komi', 'kori', 'miro', 'miro', 'moki', 'ovum', 'work', 'worm', 'wouf']
    >>> get_words('en.txt', 11)

    """
    if not isinstance(f, str):
        return None
    if not isinstance(letters, list):
        return None

    bufer_letters = []
    for i in letters:
        bufer_letters.append("".join(i))
    letters = list("".join(bufer_letters))
    list_of_words = []
    with open(f, 'r') as file:
        file_data = file.read().lower().split('\n')

    for i in file_data:
        if i.find(letters[4]) != -1 and len(i) >= 4:
            list_of_words.append(i)

    final_list = []

    for i in list_of_words:
        for j in list(set(i)):
            if (j not in letters):
                break
            if (list(i).count(j) > letters.count(j)):
                break
        else:
            final_list.append(i)

    return final_list

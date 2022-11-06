from typing import List
import random
import string

# Create list out of function in order to prevent random outputs while calling the same function
lis = []
for i in range(3):
    temporary_list = []
    for j in range(3):
        temporary_list.append(random.choice(string.ascii_letters).lower())
    lis.append(temporary_list)

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    return lis
# print(generate_grid())

def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    Rules:
    1. Words' length must be >= 4
    2. Word must have middle letter from letters
    3. There doesn't have to be more same letters in word than in letters argument
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


# print(get_words('en.txt', ['w', 'u', 'm', 'r', 'o', 'v', 'k', 'i', 'f']))
# print(get_words('en.txt', generate_grid()))

def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter 
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    list_of_words = []
    print(f'Please enter words in this letter range:\n{generate_grid()}')
    while True:
        try:
            list_of_words.append(input())
        except:
            break
    return list_of_words
# print(get_user_words())

def get_pure_user_words(user_words: List[str],
                        letters: List[str],
                        words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    Reads the file f. Checks the words with rules and returns a list of words.
    Rules:
    1. Words' length must be >= 4
    2. Word must have middle letter from letters
    3. There doesn't have to be more same letters in word than in letters argument
    """
    # change grid letters to normal
    bufer_letters = []
    for i in letters:
        bufer_letters.append("".join(i))
    letters = list("".join(bufer_letters))

    list_of_words = []
    for i in user_words:
        if i.find(letters[4]) != -1 and len(i) >= 4:
            list_of_words.append(i)

    central_letter_list = []
    for i in list_of_words:
        for j in list(set(i)):
            if (j not in letters):
                break
            if (list(i).count(j) > letters.count(j)):
                break
        else:
            central_letter_list.append(i)

    final_list = []
    for i in central_letter_list:
        if i not in words_from_dict:
            final_list.append(i)
    return final_list
# print(get_pure_user_words(get_user_words(), generate_grid(), get_words('en.txt', generate_grid())))
# print(get_pure_user_words([1,2,3], generate_grid(), get_words('en.txt', generate_grid())))

def results():
    # change grid letters to normal
    letters = generate_grid()
    bufer_letters = []
    for i in letters:
        bufer_letters.append("".join(i))
    letters = list("".join(bufer_letters))

    # number of correct words
    list_of_words = []
    user_words = get_user_words()
    for i in user_words:
        if i.find(letters[4]) != -1 and len(i) >= 4:
            list_of_words.append(i)

    central_letter_list = []
    for i in list_of_words:
        for j in list(set(i)):
            if (j not in letters):
                break
            if (list(i).count(j) > letters.count(j)):
                break
        else:
            central_letter_list.append(i)
    count_correct = len(central_letter_list)

    # all missed words
    words_from_dict = get_words('en.txt', generate_grid())
    for i in user_words:
        if i in words_from_dict:
            words_from_dict.remove(i)

    # pure user words
    pure_user_words = get_pure_user_words(user_words, generate_grid(), get_words('en.txt', generate_grid()))

    with open('result.txt', 'w') as file:
        file.write(f'Number of correct words: {count_correct}\n')
        file.write(f'All possible missed words: {", ".join(words_from_dict)}\n')
        file.write(f'User words that are not in dictionary: {", ".join(pure_user_words)}\n')

# print(results())
if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # base case
    if len(word) < 2:
        return 0
    else:
        x = 0
        # check if first 2 letters of word are "th"
        if word[0:2] == "th":
            x = 1
        # new variable that represents word, starting with next character
        sliced_word = word[1:]
        # repeat steps with sliced word, until sliced word < 2 characters long
        return x + count_th(sliced_word)

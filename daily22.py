"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""


def get_sequence(words, word):
    ret_val = []
    start_index = 0
    for i in range(len(word) + 1):
        if word[start_index:i] in words:
            ret_val.append(word[start_index:i])
            start_index = i
    return ret_val


words = ['quick', 'brown', 'the', 'fox']
word = "thequickbrownfox"

print(get_sequence(words, word))

words = ['bed', 'bath', 'bedbath', 'and', 'beyond']
word = "bedbathandbeyond"

print(get_sequence(words, word))

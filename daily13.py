"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

# Use an expanding "window" to find longest string


def find_ans(s, k):
    unique_chars = 0
    count = [0] * 26

    for char in s:
        curr_index = ord(char) - ord('a')
        if count[curr_index] == 0:
            unique_chars += 1
        count[curr_index] += 1

    if unique_chars < k:
        return

    curr_start = 0
    curr_end = 0

    window_start = 0
    window_size = 1

    count = [0] * len(count)

    for char in s:
        curr_index = ord(char) - ord('a')

        count[curr_index] += 1
        curr_end += 1

        while k < sum(1 for i in count if i > 0):
            count[ord(s[curr_start]) - ord('a')] -= 1
            curr_start += 1

        new_window_size = curr_end - curr_start
        if new_window_size > window_size:
            window_size = new_window_size
            window_start = curr_start

    return s[window_start:window_start + window_size], window_size


s = "abcba"
k = 2

print(find_ans(s, k))

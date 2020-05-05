'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''


def num_of_ways_to_decode(encoded_message):
    n = len(encoded_message)

    memo = [0] * (n + 1)
    memo[0] = 1
    memo[1] = 1

    for i in range(2, n + 1):
        memo[i] = 0

        if (encoded_message[i - 1] > '0'):
            memo[i] = memo[i - 1]

        if (encoded_message[i - 2] == '1' or
                (encoded_message[i - 2] == '2' and encoded_message[i - 1] < '7')):
            memo[i] += memo[i - 2]

    return memo[n]


def helper(msg, n):
    if n == 0 or n == 1:
        return 1
    count = 0
    if msg[n - 1] > "0":
        count = helper(msg, n - 1)
    if msg[n - 2] == '1' or (msg[n - 2] == '2' and msg[n - 1] < '7'):
        count += helper(msg, n - 2)

    return count


print(num_of_ways_to_decode('111'))
print(num_of_ways_to_decode('121'))
print(num_of_ways_to_decode('1234'))

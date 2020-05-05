"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""

# Ends up being fibonacci algorithm fib(n)


def fib(n):
    # memo = [0] * (n + 1)
    # memo[0] = 1
    # memo[1] = 1

    # return fib_helper(n, memo)

    last_two = 1
    last_one = 1
    curr = 2
    for i in range(n - curr):
        last_two = last_one
        last_one = curr
        curr = last_one + last_two

    return curr


def fib_helper(n, memo):
    if memo[n] > 0:
        return memo[n]
    if n < 2:
        return 1

    memo[n] = fib_helper(n - 1, memo) + fib_helper(n - 2, memo)
    return memo[n]


def fib2(n, steps):
    memo = [0] * (n + 1)
    memo[0] = 1
    memo[1] = 1

    return fib_helper2(n, memo, steps)


def fib_helper2(n, memo, steps):
    if memo[n] > 0:
        return memo[n]
    if n < 2:
        return 1

    for i in steps:
        if n >= i:
            memo[n] += fib_helper2(n - i, memo, steps)

    return memo[n]


print(fib(4))
assert(fib(4) == 5)

print(fib2(4, {1, 3, 5}))
assert(fib2(4, {1, 3, 5}) == 3)

def josephus(N, K):
    ans = [i for i in range(1, N + 1)]
    i, pos = 0, 0
    while len(ans) > 2:
        if (i + 1) % K == 0:
            ans.pop(pos)
        else:
            pos += 1

        i += 1

        if pos >= len(ans):
            pos = 0

    # print(i)
    print(ans)


def josephus_rec(n, k):
    if n == 1:
        return 1

    return (josephus_rec(n - 1, k) + k - 1) % n + 1


# josephus(11, 3)
# josephus(20, 3)

# print(josephus_rec(11, 3))
print(josephus_rec(41, 3))


def msbPos(n):
    pos = 0
    while n != 0:
        pos += 1
        n = n >> 1
    return pos


def josephify(n):
    position = msbPos(n)
    print(position)

    j = 1 << (position - 1)
    print(j)

    n = n ^ j
    print(n)

    n = n << 1
    print(n)

    n = n | 1
    print(n)


josephify(41)

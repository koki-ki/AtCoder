n = int(input())
# memo = [-1] * (n + 1)


# def rec(n):
#     if n == 0:
#         return 1
#     if (memo[n] != -1):
#         return memo[n]
#     memo[n] = rec(n // 2) + rec(n // 3)
#     return memo[n]


# ans = rec(n)
# print(ans)
memo = {0: 1}


def rec(n):
    if n == 0:
        return 1
    if n not in memo.keys():
        memo[n] = rec(n // 2) + rec(n // 3)
    return memo[n]


ans = rec(n)
print(ans)

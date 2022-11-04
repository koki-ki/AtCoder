n = int(input())
memo = [-1] * (n + 1)


def rec(n):
    # if n == 0:
    #     return 1
    # else:
    #     return rec[n // 2] + rec[n // 3]
    if n == 0:
        return 1
    if (memo[n] != -1):
        return memo[n]
    memo[n] = rec(n // 2) + rec(n // 3)
    return memo[n]


ans = rec(n)
print(ans)


# vector<ll> memo;

# ll rec(ll n) {
#     if (n == 0) return 1;
#     if (memo[n] != -1) return memo[n];
#     return memo[n] = rec(n / 2) + rec(n / 3);
# }

# int main() {
#     ll n;
#     cin >> n;
#     memo.assign(n + 1, -1);
#     ll ans = rec(n);
#     cout << ans << endl;
# }

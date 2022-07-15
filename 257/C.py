n = int(input())
s = list(input())
w = list(map(int, input().split()))

cnt_child = w.count('0')
cnt_adult = n - cnt_child

def f(x):
    true_cnt = 0

    for i in range(n):
        if w[i] < x and s[i] == '0':
            true_cnt += 1
        elif w[i] >= x and s[i] == '1':
            true_cnt += 1

    return true_cnt

z = zip(w, s)
zsort = sorted(z)
w, s = zip(*zsort)

may_miss_ad = 0

print(w)
print(s)


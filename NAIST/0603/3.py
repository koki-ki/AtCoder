n = int(input())
dict_ = {}
for i in range(n):
    s = input()
    if s in dict_:
        dict_[s] += 1
    else:
        dict_[s] = 1

ans = max(dict_, key=dict_.get)
print(ans)
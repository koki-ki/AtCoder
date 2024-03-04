def run_length_compression(s):
    if type(s) != list:
        s = list(s)
    new_s = []
    i = 0
    cnt = 1
    while i < len(s) - 1:
        if s[i] != s[i + 1]:
            new_s.append((s[i], cnt))
            cnt = 0
        i += 1
        cnt += 1
    new_s.append((s[i], cnt))
    return new_s

s = input()
t = input()

s = run_length_compression(s)
t = run_length_compression(t)

if len(s) != len(t):
    print("No")
    exit()

for s_, t_ in zip(s, t):
    if s_ == t_:
        continue
    if s_[0] != t_[0] or (s_[1] == 1 and t_[1] >= 2) or s_[1] > t_[1]:
        print("No")
        exit()

print("Yes")


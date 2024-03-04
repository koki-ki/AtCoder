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
new_s = run_length_compression(s)
ans = len(new_s) - 1
print(ans)

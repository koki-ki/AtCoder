def split_s(s):
    chars = []
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] != s[j]:
                chars.append(s[i:j])
    return chars

def shorten_s(s):
    new_s = []
    for i, char in enumerate(s):
        if len(char) == 1 or len(char) == 2:
            new_s.append(char)
        elif len(char) >= 3:
            new_s.append(char[:2])
    return s


# main #
s = input()
t = input()

chars_s = shorten_s(split_s(s))
chars_t = shorten_s(split_s(t))
if chars_s == chars_t:
    print('Yes')
else:
    print('No')


print(chars_s)
print(chars_t)
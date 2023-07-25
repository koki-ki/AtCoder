normal_x = list('abcdefghijklmnopqrstuvwxyz')
new_x = list(input())

new2normal = dict(zip(new_x, normal_x))
normal2new = dict(zip(normal_x, new_x))

n = int(input())
s = [input() for _ in range(n)]
changed_s = []

for i in range(n):
    changed_si = ''
    listed_si = list(s[i])
    for char in listed_si:
        changed_si += new2normal[char]
    changed_s.append(changed_si)

changed_s.sort()
ans = []

for i in range(n):
    motono_si = ''
    listed_si = list(changed_s[i])
    for char in listed_si:
        motono_si += normal2new[char]
    ans.append(motono_si)

for a in ans:
    print(a)

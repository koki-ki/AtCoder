from collections import defaultdict
n = int(input())
x = defaultdict(int)
for _ in range(n):
    x[input()] += 1
print('AC' + ' x ' + str(x['AC']))
print('WA' + ' x ' + str(x['WA']))
print('TLE' + ' x ' + str(x['TLE']))
print('RE' + ' x ' + str(x['RE']))

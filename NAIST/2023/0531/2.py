s = input()
cnt = 1 if s.count('R') else 0
cnt = max(cnt, 2 if s.count('RR') else 0)
cnt = max(cnt, 3 if s.count('RRR') else 0)

print(cnt)

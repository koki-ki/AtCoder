sx, sy, tx, ty = map(int, input().split())
ans = ''
ans += (tx - sx) * 'R'
ans += (ty - sy) * 'U'
ans += (tx - sx) * 'L'
ans += (ty - sy) * 'D'
ans += 'D'
ans += (tx - sx + 1) * 'R'
ans += (ty - sy + 1) * 'U'
ans += 'L'
ans += 'U'
ans += (tx - sx + 1) * 'L'
ans += (ty - sy + 1) * 'D'
ans += 'R'
print(ans)

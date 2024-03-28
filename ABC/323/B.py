n = int(input())
s = [input() for _ in range(n)]
cnt_win = [si.count("o") for si in s]
player_nums = [i + 1 for i in range(n)]
player_nums.sort(key=lambda x: cnt_win[x - 1], reverse=True)
print(*player_nums)

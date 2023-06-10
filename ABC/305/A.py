n = int(input())
spots = [5 * i for i in range(21)]
dist_spots = [abs(spot - n) for spot in spots]
min_ = min(dist_spots)

arg_min = dist_spots.index(min_)
ans = spots[arg_min]

53
print(ans)



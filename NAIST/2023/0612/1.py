s = input()
weekdays = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
countdays = [i for i in range(7)]
day_count_dist = dict(zip(weekdays, countdays))
ans = (day_count_dist['SUN'] - day_count_dist[s]) % 7
ans = 7 if ans == 0 else ans
print(ans)
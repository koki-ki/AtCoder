import math
a, b, k = map(int, input().split())
ans = math.ceil(math.log(b/a, k))
print(ans)

n = int(input())
a = list(map(int, input().split()))


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


ans = 0
two = []
three = []
others = {}
twom = 1000000000
threem = 1000000000
arrs = []
for i in range(n):
    arr = factorization(a[i])
    arrs.append(arr)
    for j in range(len(arr)):
        if n % 2 != 0:
            two.append(0)
        if n % 3 != 0:
            three.append(0)
        if arr[j][0] == 2:
            two.append(arr[j][1])
        elif arr[j][1] == 3:
            three.append(arr[j][1])
if two == []:
    twom = 0
else:
    twom = min(two)
if three == []:
    threem = 0
else:
    threem = min(three)
nums = []
ans = 0
for i in range(n):
    arr = arrs[i]
    for j in range(len(arr)):
        if arr[j][0] == 2:
            ans += arr[j][1] - twom
            arr[j][1] = twom
        elif arr[j][0] == 3:
            ans += arr[j][1] - threem
            arr[j][1] = threem
    num = 1
    for j in range(len(arr)):
        num *= arr[j][0] ** arr[j][1]
    nums.append(num)

nums = list(set(nums))
if len(nums) == 1:
    print(ans)
else:
    print(-1)

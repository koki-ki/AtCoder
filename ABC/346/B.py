from collections import Counter

w, b = map(int, input().split())
keyboard = "wbwbwwbwbwbw" * 30
n = len(keyboard)
window = w + b

for i in range(n - window):
    count = Counter(keyboard[i:i + window])
    if count["w"] == w and count["b"] == b:
        print("Yes")
        exit()

print("No")

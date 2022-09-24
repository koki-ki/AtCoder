a, b = map(int, input().split())
scores = [0]
if a == 1:
    scores.append(1)
if a == 2:
    scores.append(2)
if a == 3:
    scores.append(1)
    scores.append(2)
if a == 4:
    scores.append(4)
if a == 5:
    scores.append(1)
    scores.append(4)
if a == 6:
    scores.append(2)
    scores.append(4)
if a == 7:
    scores.append(1)
    scores.append(2)
    scores.append(4)

if b == 1:
    scores.append(1)
if b == 2:
    scores.append(2)
if b == 3:
    scores.append(1)
    scores.append(2)
if b == 4:
    scores.append(4)
if b == 5:
    scores.append(1)
    scores.append(4)
if b == 6:
    scores.append(2)
    scores.append(4)
if b == 7:
    scores.append(1)
    scores.append(2)
    scores.append(4)

scores = list(set(scores))
ans = sum(scores)
print(ans)

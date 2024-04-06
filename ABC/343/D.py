n, t = map(int, input().split())
scores = [0 for _ in range(n)]
scores_dict = {0: n}

for _ in range(t):
    a, b = map(int, input().split())
    a -= 1
    scores_dict[scores[a]] -= 1
    if scores_dict[scores[a]] == 0:
        del scores_dict[scores[a]]

    scores[a] += b
    if scores[a] in scores_dict:
        scores_dict[scores[a]] += 1
    else:
        scores_dict[scores[a]] = 1
    print(len(scores_dict))

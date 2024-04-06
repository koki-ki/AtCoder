def process_queries(n, q, x):
    a = [0] * n  # 配列Aを0で初期化
    s = set()  # 集合Sを空で初期化
    s_size = 0  # 集合Sの要素数

    for xi in x:
        if xi in s:
            s.remove(xi)  # Sからxiを削除
            s_size -= 1  # 要素数を減少
        else:
            s.add(xi)  # Sにxiを追加
            s_size += 1  # 要素数を増加
        a[xi - 1] += s_size  # xiに対応するAの値を更新

    return a


# 例の入力
n, q = map(int, input().split())
a = [0 for _ in range(n)]
x = list(map(int, input().split()))
s = set()

# 関数をテスト
print(*process_queries(n, q, x))

class Segtree:
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2

        self.data = [0 for _ in range(2 * self.size)]


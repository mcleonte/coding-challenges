def solution(n, b):
    n = list(map(int, n))
    ids = [n]
    while True:
        y = sorted(n)
        x = y[::-1]
        z = []
        borrow = False
        for a, c in zip(y, x):
            a -= borrow
            borrow = a < c
            z.append(a - c + b * borrow)
        n = z[::-1]
        try:
            return len(ids) - ids.index(n)
        except ValueError:
            ids.append(n)

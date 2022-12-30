def solution(pegs):
    spaces = [b - a for a, b in zip(pegs[:-1], pegs[1:])]
    n = 2 * sum(s * (-1) ** i for i, s in enumerate(spaces))
    d = 1
    if len(pegs) % 2 == 0:
        if n % 3 == 0:
            n //= 3
        else:
            d = 3
    r = n / d
    for s in spaces:
        r = s - r
        if r < 1:
            return -1, -1
    return n, d

# O(n) O(n) - Manacher's algorithm
def longestPalindromicSubstring(string):
    t = "#".join(f"^{string}$")
    l, p, c, r = len(t), {}, 0, 0
    for i in range(1, l - 1):
        p[i] = min(r - i, p[2 * c - i]) if r > i else 0
        while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1
        if i + p[i] > r:
            c, r = i, i + p[i]
    c, l = max(p.items(), key=lambda t: t[1])
    return string[(c - l) // 2 : (c + l) // 2]

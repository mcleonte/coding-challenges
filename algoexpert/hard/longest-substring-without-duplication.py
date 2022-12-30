def longestSubstringWithoutDuplication(string):
    """
    O(n) O(s) | n = len(string), s = len(set(string))
    """
    d = {}
    si = lsi = lei = 0
    for i, c in enumerate(string):
        if c in d:
            si = max(si, d[c] + 1)
        if i - si > lei - lsi:
            lsi, lei = si, i
        d[c] = i
    return string[lsi : lei + 1]

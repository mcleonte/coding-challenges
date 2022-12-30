# O(n) O(n)
def runLengthEncoding(string):
    i, p, out = 0, string[0], []
    for c in string:
        if c == p and i < 9:
            i += 1
        else:
            out += str(i), p
            i = 1
            p = c
    out += str(i), p
    return "".join(out)

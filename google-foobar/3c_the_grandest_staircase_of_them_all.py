def solution(n):
    """
    Time and space complexity: O(n^2) O(n)

    Solution derived from the generating function Product(1+x**i) of sequence A000009:
    Number of partitions of n into distinct parts - https://oeis.org/A000009
    """
    # given the power series sum( c[i] * x ** i for i in range(n + 1) ),
    # initialize the coefficients
    c = [1] + n * [0]
    # for every term x ** i in the power series, except first term x ** 0
    for i in range(1, n + 1):
        # multiply the power series with (1 + x ** i), by looping through every
        # c[j] * x ** j between c[0] * x ** 0 and c[n-i] * x ** (n - i), in reversed order
        for j in range(n - i, -1, -1):
            # and multiply it with (1 + x ** i) to obtain
            # c[j] * x ** j + c[j] * x ** (i + j), which results in increasing the
            # coefficient of term x ** (i + j) with the coefficient of term x ** j
            c[i + j] += c[j]
    # get the coefficient c[n] of term x ** n, which represents the number of
    # partitions of n into distinct parts, and return it after subtracting 1,
    # to exclude (n,) as a step configuration, since at least 2 steps are required
    return c[-1] - 1

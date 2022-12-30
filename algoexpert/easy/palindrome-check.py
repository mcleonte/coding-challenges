# O(n) O(1)
def isPalindrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[-i - 1]:
            return False
    return True


# O(n) O(1)
def isPalindrome2(string):
    return all(string[i] == string[-i - 1] for i in range(len(string) // 2))


# O(n) O(n)
def isPalindrome3(string):
    return string == string[::-1]

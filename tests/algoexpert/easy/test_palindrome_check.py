from mcleonte.dsa.algoexpert.easy.palindrome_check import is_palindrome


def test_1():
  assert is_palindrome("abcdcba") is True


def test_2():
  assert is_palindrome("a") is True


def test_3():
  assert is_palindrome("ab") is False


def test_4():
  assert is_palindrome("aba") is True


def test_5():
  assert is_palindrome("abb") is False


def test_6():
  assert is_palindrome("abba") is True


def test_7():
  assert is_palindrome("abcdefghhgfedcba") is True


def test_8():
  assert is_palindrome("abcdefghihgfedcba") is True


def test_9():
  assert is_palindrome("abcdefghihgfeddcba") is False

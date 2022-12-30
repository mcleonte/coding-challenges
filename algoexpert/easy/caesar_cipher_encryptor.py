# O(n) O(n)
def caesarCipherEncryptor(string, key):
  a = ord("a")
  ka, za = key - a, ord("z") - a + 1
  return "".join(chr((ord(s) + ka) % za + a) for s in string)

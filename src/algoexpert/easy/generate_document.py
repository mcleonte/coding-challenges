from collections import Counter


# O(n) O(n)
def generateDocument(characters, document):
  return not Counter(document) - Counter(characters)

from collections import Counter, defaultdict


# O(nw) O(nw) | n = number of words, w = length of longest word
def groupAnagrams(words):
  out = defaultdict(list)
  for w in words:
    out[frozenset(Counter(w).items())].append(w)
  return list(out.values())

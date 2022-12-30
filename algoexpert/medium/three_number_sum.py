"""
Write a function that takes in a non-empty array of distinct integers and an
integer representing a target sum. The function should find all triplets in the
array that sum up to the target sum and return a two-dimensional array of all
these triplets. The numbers in each triplet should be ordered in ascending
order, and the triplets themselves should be ordered in ascending order with
respect to the numbers they hold.

If no three numbers sum up to the target sum, the function should return an
empty array.
"""


def three_number_sum(arr, tgt):
  """
  O(n^2) O(n)
  """
  arr.sort()  # O(nlogn)
  out, l = [], len(arr)
  for i in range(l - 1):
    j, k, t = i + 1, l - 1, tgt - arr[i]
    while j < k:
      s = arr[j] + arr[k]
      if s == t:
        out.append([arr[i], arr[j], arr[k]])
        j += 1
        k -= 1
      elif s < t:
        j += 1
      else:
        k -= 1
  return out


def three_number_sum_2(arr, tgt):
  """
  O(n^3) O(n)
  """
  arr.sort()  # O(nlogn)
  out, l = [], len(arr)
  for i in range(l - 2):
    t = tgt - arr[i]
    for j in range(i + 1, l - 1):
      t2 = t - arr[j]
      for k in range(j + 1, l):
        if arr[k] == t2:
          out.append([arr[i], arr[j], arr[k]])
  return out

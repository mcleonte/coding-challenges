"""
Write a function that takes in a list of numbers and returns a dictionary
containing the following statistics about the numbers : the mean, median, mode,
sample variance, sample standard deviation, and 95% confidence interval for the
mean.

Note that :
  • You can assume that the given list contains a large-enough number of samples
    from a population to use a z-score of 1.96
  • If there's more than one mode, your function can return any of them.
  • You shouldn't use any libraries.
  • Your output values will automatically be rounded to the fourth decimal.
"""

from typing import List, Dict, Union
from collections import Counter


def get_statistics(nums: List[int]) -> Dict[str, Union[float, List[float]]]:

  stats = {}
  total = sum(nums)
  count = len(nums)
  nums.sort()

  stats["mean"] = total / count
  stats["mode"] = Counter(nums).most_common(1)[0][0]

  if count % 2 == 0:
    stats["median"] = (nums[count // 2] + nums[count // 2 - 1]) / 2
  else:
    stats["median"] = nums[count // 2]

  stats["sample_variance"] = sum((num - stats["mean"])**2 for num in nums) / (
      count - 1)
  stats["sample_standard_deviation"] = stats["sample_variance"]**.5

  dev = 1.96 * stats["sample_standard_deviation"] / (count**.5)
  stats["mean_confidence_interval"] = [stats["mean"] - dev, stats["mean"] + dev]

  return stats

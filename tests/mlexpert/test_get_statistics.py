"""
Tests for mlexpert/get_statistics.py
"""

from typing import List, Dict, Union
from mcleonte.dsa.mlexpert.get_statistics import get_statistics


def deep_round(
    result: Dict[str, Union[float, List[float]]]
) -> Dict[str, Union[float, List[float]]]:

  return {
      k: [round(v[0], 4), round(v[1], 4)]
      if isinstance(v, list) else round(v, 4) if isinstance(v, float) else v
      for k, v in result.items()
  }


def test_3():
  inp = [0, 1]
  assert deep_round(get_statistics(inp)) == {
      "mean": 0.5,
      "mean_confidence_interval": [-0.48, 1.48],
      "median": 0.5,
      "mode": 0,
      "sample_standard_deviation": 0.7071,
      "sample_variance": 0.5
  }


def test_4():
  inp = [13, 14, 17, 2, 16, 17, 1, 15, 4, 18, 7, 6, 11, 18, 18, 6, 12, 3, 6]
  assert deep_round(get_statistics(inp)) == {
      "mean": 10.7368,
      "mean_confidence_interval": [8.0188, 13.4549],
      "median": 12,
      "mode": 6,
      "sample_standard_deviation": 6.0447,
      "sample_variance": 36.538
  }

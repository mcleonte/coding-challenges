"""
https://leetcode.com/problems/convert-the-temperature/


You are given a non-negative floating point number rounded to two decimal places
celsius, that denotes the temperature in Celsius.

You should convert Celsius into Kelvin and Fahrenheit and return it as an array
ans = [kelvin, fahrenheit].

Return the array ans. Answers within 10-5 of the actual answer will be accepted.
"""

from typing import List


def convert_temperature(celsius: float) -> List[float]:
  return [celsius + 273.15, celsius * 1.8 + 32.]

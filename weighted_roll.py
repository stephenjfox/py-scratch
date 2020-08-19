"""
Description: given a list of weights (from which the size of die is derived)
  produce a roll die. This "weighted die roll" should produce dissimilarly
  likely outcomes.

Example:
  Given weights = [0.1, 0.1, 0.3, 0.1, 0, 0.4], there should never be a 5
    and there should be many 3's and 4's.
  
-----
First implementation: integer weights

  For weights = [1, 99], (a heavily weighted coin flip) we should see tails
    roughly 99 times in a hundred
"""

from collections import Counter
from random import randint
from typing import List
from unittest import TestCase, main as test_main


def weightedRoll(weights: List[int]) -> int:
  """Rolls a weighted die outputing an int of [1, len(weights)]"""
  if any(map(lambda x: (x < 0) or (int(x) != x), weights)):
    raise ValueError("All weights must be positive integers")

  if not weights:
    raise ValueError("Must have at least one weight")

  total_weight = sum(weights)
  selection = 0
  # roll once, find the weight that captures this roll
  roll = randint(0, total_weight)
  cumsum = 0
  for i, w in enumerate(weights):
    cumsum += w
    if roll < cumsum:
      selection = i
      break

  return selection + 1


class TestAlgorithm(TestCase):

  def test_weightedRoll_degenerateTestCase(self):
    self.assertEqual(weightedRoll([50]), 1, "degenerateTestCase")

  def test_coinFlip(self):
    subject = [1, 1]
    test = weightedRoll(subject)
    print("Coinflip:", test)
    self.assertTrue(test in {1, 2}, 'coinFlip should be produce reasonable values')

  def test_probabilityIsWithinReason(self):
    subject = [1, 99]
    frequencies = Counter((weightedRoll(subject) for _ in range(100)))
    print(frequencies)
    self.assertTrue(frequencies[2] > frequencies[1], 'probabilityIsWithinReason')


if __name__ == "__main__":
  test_main()
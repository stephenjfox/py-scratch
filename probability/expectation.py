from operator import mul, truediv
from itertools import starmap, repeat, cycle

# def expectation(probabilities, outcomes):
#   pass


def expectation(weights, outcomes):
  total_weight = sum(weights)  # integral or floating.
  # this step is a waste if we're floating point, because it will just
  # recalculate the values
  # p(xs) = { |X| / |Omega| forall x_i in X for X in Omega }
  # that is, for all states (x_i) which match some event (X) in the state space (Omega)
  probabilities = list(starmap(truediv, zip(weights, repeat(total_weight))))
  return sum(starmap(mul, zip(probabilities, outcomes)))


from unittest import TestCase, main as test_main


class TestAlgorithm(TestCase):

  def test_expectation_countsFairDieCorrectly(self):
    fair_die = list(repeat(1, 6))
    die_roll_state_space = list(range(1, 7))
    E = sum(die_roll_state_space) / len(die_roll_state_space)
    self.assertEqual(expectation(fair_die, die_roll_state_space), E,
                     "countsFairDieCorrectly")


if __name__ == "__main__":
  test_main()
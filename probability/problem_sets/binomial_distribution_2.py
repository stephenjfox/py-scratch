"""
A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are
incorrectly sized. What is the probability that a batch of 10 pistons will contain:
1. No more than 2 rejects?
2. At least 2 rejects?

Print the answer to each question on its own line:

1. The first line should contain the probability that a batch of 10 pistons will contain no more than 2 rejects.
2. The second line should contain the probability that a batch of 10 pistons will contain at least 2 rejects.

Round both of your answers to a scale of 3 decimal places (i.e., 1.234 format).


"""

from math import factorial


def format_answer(value) -> str:
  return "{value:0.3f}".format(value=value)


def product(i, j) -> int:
  """Multiply every integer from i -> j inclusive"""
  out = 1
  for x in range(i, j + 1):
    out *= x

  return out


def n_choose_k(n, k):
  if n - k > k:
    divisor = product(n - k + 1, n)
    denominator = factorial(k)
  else:
    divisor = product(k + 1, n)
    denominator = factorial(n - k)

  comb = divisor / denominator
  return comb


def binomial_dist(prob_success, prob_fail, trials, choices) -> float:
  # dist = nCk * p_success^(k) * p_fail^(n-k)
  coefficient = n_choose_k(trials, choices)
  positive = prob_success**choices
  negative = prob_fail**(trials - choices)
  prob = coefficient * positive * negative
  return prob


if __name__ == '__main__':

  fails_in_100, batch_count = [int(x) for x in input().split(' ')]

  # translate the values into probabilities
  # p = boy, q = girl, because the question is about getting boys
  fail_rate = fails_in_100 / 100.
  p = 1 - fail_rate

  n_trials = batch_count # aliasing

  # we're seeking after the rate of failures, just treat that as the success criteria
  binomial_result_2_fails = binomial_dist(fail_rate, p, n_trials, 2)
  prob_2_rejects = binomial_dist(fail_rate, p, n_trials, 0) +\
                    binomial_dist(fail_rate, p, n_trials, 1) +\
                   binomial_result_2_fails

  prob_at_least_2_rejects = 1 - prob_2_rejects + binomial_result_2_fails

  print(prob_2_rejects)
  print(prob_at_least_2_rejects)

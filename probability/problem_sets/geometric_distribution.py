"""
Day 4: Geometric Distribution I

#############
Tutorial
#############

Negative Binomial Experiment
* Experiment consists of n-repeated trials
* Independent trials
* The outcome of each trial is either success (s) or failure (f)
* P(s) is the same for every trial
* The experiment continues until x-success are observed

If X is a number of experiments until the xth success, then X is a discrete
  random variable called a negative binomial.

Negative Binomial Distribution

b*(x, n, p) = {n - 1}C{x - 1} * p^x * q^(n - x), (def.) q = 1 - p

* Total n trials, waiting for x-success 
* The probability of success of 1 trial is p; q = 1 - p
* This is a distribution of x - 1 success after n - 1 trials and x successes after n trials

Geometric Distribution: a special case of the negative binomial distribution
* Where the number of successes is 1
* g(n, p) = q^(n - 1) * p
* Example:
  * Basketball player is a 70% free throw shooter. What is the probability that they make
    the first free throw on the FIFTH show?
  * Given: n = 5, p = 0.7, q = 0.3
  * Computation: g(5, 0.7) = (0.3^4)*0.7 = 0.00567
"""

def geometric_dist(n, p) -> float:
  return (1 - p) * p ** (n - 1)

if __name__ == "__main__":
  numerator, denominator = [int(x) for x in input().split(' ')]
  p_fail = numerator / denominator

  trials = int(input())

  # We want the probability of failing to fail for n-1 trials,
  # and desirably failing on the n-th trial
  outcome = geometric_dist(trials, p_fail)
  print(f"{outcome:0.3f}")


  """
  Geometric Distribution II

  Task:
  What is the probability that the first defect is found during the first 5 inspections?

  Same input.
  """

  # The geometric distribution gives the probability that we have a failure.
  # We pass p = 1 - p_fail because we want to compute the likelihood of success
  # after 1 through 5 trials. Why? Because that is conceptually the additive
  # compliment to failing within those same "1 through 5 trials"
  outcome = sum(geometric_dist(t, 1 - p_fail) for t in range(1, trials + 1))
  print(f"{outcome:0.3f}")
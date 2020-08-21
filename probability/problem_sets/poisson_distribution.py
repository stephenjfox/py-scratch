"""
Motivation: what do we do when we can't compute p (or q) within the binomial random variable formula?

#############
Tutorial
#############

A Poisson experiement
  is a statistical experiement with the following properties
* The outcome of each trial is a success or failure
* The average number of success (lambda) that occurs in a specificied region is known/given
* The probability of success is proportional to the size of the regioun
* Probability that success will occur in an extremely small region (like a point) is ~0.

Poisson Distribution is the number of successes that result from a Poisson experiment.
* Its probability distribution is:

P(k, λ) = (λ^k)(e^(-λ)) / k!
* λ = average number of successes in the specified region e.g. (0.5 < x < 0.6, 0.6 >= y)
* k = actual number of successes that occur in a specified region
* P(k, λ) is the Poisson probability which is the probability of getting exactly k successes when
  the average number of success is λ
------------
Example:

Suppose the aerage number of lions seens by tourists on a one-day safari is 5
* What is the probability that tourists will see fewer than 4 lions on the next one-day safari?

P(k <=3, λ = 5) = Summation{r=0->3} { (λ^r) * e^(-λ) / r! }
We can extract a variable for e^(λ=5), then just do the computation:
  (5^0) * e^(-5) / 0! + (5^1) * e^(-5) / 1! + (5^2) * e^(-5) / 2! + (5^3) * e^(-5) / 3! = 0.2650
* Accounting for every outcomes beneath 4 lions, we have a 26.5% chance of seeing less than the
  average number of lions.
------------



Note that
* Expectation is the expected value, mean, weighted average, center of mass, and 1st moment of a
  random variable.
* In machine learning, a random variable tends to match the task at hand
  * Classification? Discrete random variable
  * Regression or another real-valued task? Continuous random variable

#############
Retain
#############

For Poisson Random Variables, Var(X) = E[X] = λ (eq. i)
If we want to find the E[X^2], we can do some algebra on the Variance definition
1. Var(X) = E[X^2] - (E[X])^2
2. => E[X^2] = Var(X) + (E[X])^2
3. By substitution with (eq. i): E[X^2] = λ + λ^2

############################
Task: Poisson Distribution I
############################

A random variable, X, follows a Poisson distribution with mean of 2.5. Find the probability which
  the random variable X is equal to 5.

Thoughts
---------
* The mean is the average, so λ = 2.5
* We want a value of 5, which is well above the mean, so would shouldn't expect a high probability
"""

λ = 2.5
k = 5

from math import exp, factorial

def poisson_probability(successes, average_successes) -> float:
  """P(k, λ) = (λ^k)(e^(-λ)) / k!"""
  return (average_successes ** successes) * exp(-average_successes) / factorial(successes)

print(f"{poisson_probability(k, λ):0.3f}")

"""
#############################
Task: Poisson Distribution II
#############################

Expected value of a random variable
"""
"""
The ratio of boys to girls for babies born in Russia is 1.09:1.
  If there is  child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?

Write a program to compute the answer using the above parameters.
  Then print your result, rounded to a scale of  decimal places (i.e.,  format).

Input Format

A single line containing the following values:

1.09 1

If you do not wish to read this information from stdin, you can hard-code it into your program.


"""
from math import factorial

def format_answer(value) -> str:
    # they really need to update the linter to Python 3.7+
    return "{value:0.3f}".format(value=value)

def product(i, j) -> int:
    """Multiply every integer from i -> j inclusive"""
    out = 1
    for x in range(i, j + 1):
        out *= x
    
    # print("\tProduct ({} -> {}) =".format(i, j), out)
    return out

def n_choose_k(n, k):
    # print("Computing combinations {}C{} =".format(n, k))
    if n - k > k:
        # print("\t\tFactoring out (n - k)=", n - k)
        divisor = product(n - k + 1, n)
        denominator = factorial(k)
    else:
        # print("\t\tFactoring out (k)=", k)
        divisor = product(k + 1, n)
        denominator = factorial(n - k)
    # print("\tComputed divisor =", divisor)
    # print("\tComputed denominator =", denominator)
    comb = divisor / denominator
    # print("Result =", comb)
    return comb

boy_occur, girl_occur = [float(x) for x in input().split(' ')]

print(boy_occur, girl_occur)

# translate the values into probabilities
# p = boy, q = girl, because the question is about getting boys
p_boy = boy_occur / (boy_occur + girl_occur)
p_girl = girl_occur / (boy_occur + girl_occur)

n_trials = 6

cum_prob = 0

for n_boys in range(3, n_trials + 1): # 3-6
    coeff = n_choose_k(n_trials, n_boys)
    boy_outcomes = p_boy ** n_boys # 3, 4, 5, 6
    girl_outcomes = p_girl ** (n_trials - n_boys) # 3, 2, 1, 0
    prob = coeff * boy_outcomes * girl_outcomes
    cum_prob += prob

print("Answer:", format_answer(cum_prob))


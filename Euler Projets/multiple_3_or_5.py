# If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.
# Find the sum of all the multiples of $3$ or $5$ below $1000$

def check_multiples(number):
    resault = False
    if number%3 == 0 or number%5 == 0:
        resault = True
    return resault

sum_multiples = 0

for i in range(1,1000):
    if check_multiples(i):
        sum_multiples = sum_multiples + i

print(sum_multiples)

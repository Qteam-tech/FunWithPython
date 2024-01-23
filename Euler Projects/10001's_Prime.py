# By listing the first six prime numbers: $2, 3, 5, 7, 11$, and $13$, we can see that the $6$th prime is $13$.
# What is the $10\,001$st prime number?

def checkPrime(n):
    prime = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            prime = False
            break
    return prime

prime_count = 0
i = 2
prime = 2

while prime_count < 10001:
    if checkPrime(i):
        prime_count = prime_count + 1
        prime = i
    i = i + 1
print(prime)
print(prime_count)

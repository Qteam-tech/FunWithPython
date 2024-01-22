# The prime factors of $13195$ are $5, 7, 13$ and $29$.
# What is the largest prime factor of the number $600851475143$?

n = 600851475143

def check_prime(n):
    prime = True
    for i in range (2, n):
        if n % i == 0:
            prime = False
            break
    return prime

for i in range(2, int(n ** 0.5)+1):
    if n % i == 0 and check_prime(i):
        print(i)
            
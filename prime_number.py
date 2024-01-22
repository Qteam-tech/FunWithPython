
def checkPrime(n):
    prime = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            prime = False
            break
    return prime
prime_count = 0
for i in range(1,1001):
    if checkPrime(i):
        prime_count = prime_count +1
        print(i,'is prime number.')
print('there are', prime_count, 'in first 1000 numbers')
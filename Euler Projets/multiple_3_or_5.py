
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

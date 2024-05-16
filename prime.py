import sympy

def find_primes_with_condition(limit):
    primes = []
    sum_primes = 0

    for prime in sympy.primerange(2, limit):
        if sum_primes % prime == 0:
            primes.append(prime)
            print(sum_primes,prime)
        sum_primes += prime

    return primes

limit = int(input("Enter the limit for prime numbers: "))
result = find_primes_with_condition(limit)
print("Prime numbers satisfying the condition:", result)


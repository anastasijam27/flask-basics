def factorize(n):
    factors = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n //= i
                factors.append(i)
    return factors
def number_of_digits(n):
    count = 0
    while n!=0:
        n //= 10
        count += 1
    return count
num = int(input(
    "Choose the number whose largest prime factor is to be found: "))
primeFactors = []
# Fundamental theorem of arithmetic : Every number > 1 an be expressed uniquely
# as a product of prime numbers.
# Start searching from 2 for factors, the first factor found is necessarily
# prime. The prime factors of the remaining number are > 2, so increment to
# find its first factor(necessarily prime) and repeat till n is a prime number.

d = 2
while num > 1:
    while num%d == 0:
        print(d)
        primeFactors.append(d)
        # // to return an int rather than a float
        num //= d
    d += 1
    if d*d > num and num > 1:
        # A composite number must have at least one prime factor < sqrt(num).
        # If at any point, the factor being considered is larger than num, this
        # means that num is a prime number.
        primeFactors.append(num)
        break

print("Largest prime factor is {}".format(max(primeFactors)))

# Adding the check for d > sqrt(n) redues the complexity from O(n) to
# O(sqrt(n)).

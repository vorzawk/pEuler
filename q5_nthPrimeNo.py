n = 1
def chkPrime(num):
    d = 2
    while (d*d <= num):
        if (num%d == 0):
            return False
        d = d + 1
    return True

def nthPrime(n):
    cntPrime = 1    # Counting 2 right away so that only odd nos can be checked
    for i in range(3,150000,2):
        if chkPrime(i):
            cntPrime = cntPrime + 1

        if cntPrime == n:
            print(i)
            return

nthPrime(10001)




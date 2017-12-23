n = 3
sum = 0
while n < 1000:
    sum += n
    n += 3

n = 5
while n < 1000:
    if n%3 != 0:
        sum += n
    n += 5

print("sum is {}".format(sum))

# Don't use an array to store the fibonacci numbers, totally unnecessary!
x = y = 1
sum = 0
thres = 4000000

while y <= thres:
    if y%2 == 0:
        sum += y
    y = x+y
    x = y-x

print("sum is {}".format(sum))

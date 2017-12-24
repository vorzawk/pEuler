def checkPalindrome(string):
    size = len(string)
    i = 0
    j = size-1
    while i < j:
        if string[j] != string[i]:
            return False
        i = i+1
        j = j-1
    return True

def findLargestPalindrome():
    # Finds palindrome but not neessarily the largest
    maxPalindrome = 0
    for i in range(999,99,-1):
        for j in range(999,99,-1):
            prod = i*j
            if checkPalindrome(str(prod)):
                if prod > maxPalindrome:
                    maxPalindrome = prod
    print(maxPalindrome)

findLargestPalindrome()

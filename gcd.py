def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)
# whyyyyyyyyyyyyyyyyyyy

# Please use only positive integers
a = 2
b = 3

print(gcd(a, b))

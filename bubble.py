x = [5, 4, 3, 2, 1]

n = len(x)
count = 0
for i in range(0, n):
    for j in reversed(range(i+1, n)):
        count += 1
        if x[j] < x[j-1]:
            # interchange using temp variable
            temp = x[j-1]
            x[j-1] = x[j]
            x[j] = temp

print(x, count)

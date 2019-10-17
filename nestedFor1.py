counter = 0

for i in range(1, 11):
    for j in range(1, i+1):
        for k in range(1, j+1):
            print(i, j, k, end = " ")
            counter += 1
            print(counter)

# 20 choose 3 with reps

counter = 10

for i in range(1, 16):
    for j in range(i, 16):
        for k in range(j, 16):
            print(i, j, k)
            counter += 1

print(counter)

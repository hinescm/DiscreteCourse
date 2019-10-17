import time

n = 100000000
# not past  ^ one billion please
sum = 0
t0 = time.clock()
for i in range(n+1):
    sum = sum + i
t1 = time.clock()

print("The total is {0}.".format(sum))
print("That took {0:.4f} seconds.".format(t1-t0))
print("-"*20)
################################################################
t0 = time.clock()
sum = int(n*(n+1)/2)
t1 = time.clock()

print("The total is {0}.".format(sum))
print("That took {0:.4f} seconds.".format(t1-t0))

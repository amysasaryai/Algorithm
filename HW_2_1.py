# importing the required module
import timeit
import random

for i in range(10000, 1000000, 20000):
    t = timeit.Timer("x[(random.randrange(%d))]"%i, 
                     "from __main__ import random, x")


    x = list(range(i))
    indextime = t.timeit(number=100)
    print("%d, %10.4f" %(i, indextime))


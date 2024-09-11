import random
from time import time
from memory_profiler import profile

@profile
def e3_1():
    MAX=int(input("..."))
    start_time = time()
    sum=0
    n=MAX
    while(n>0):
        n=n//2
        i=0
        while(i<n):
            sum +=1
            i +=1
    elapsed_time = time() - start_time
    print("Tiempo trascurrido: %.20f seconds." % elapsed_time)
    return sum

@profile
def e3_2():
    MAX=int(input("..."))
    start_time = time()
    sum=0
    n=MAX
    i = 1
    while (i<n):
        i = i*2
        j=0
        while (j<i):
            sum = sum +1
            j = j+1
    elapsed_time = time() - start_time
    print("Tiempo trascurrido: %.20f seconds." % elapsed_time)
    return sum


@profile
def e3_3():
    MAX=int(input("..."))
    start_time = time()
    sum=0
    n=MAX
    i = 1
    while (i<n):
        i = i * 2
        j = 0
        while (j<n):
            sum=sum+1
            j=j+1
    elapsed_time = time() - start_time
    print("Tiempo trascurrido: %.20f seconds." % elapsed_time)
    return sum


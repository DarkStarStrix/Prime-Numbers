# prime number algorithm using Sieve of Eratosthenes method use graphs to show the results and compare the time complexity of the algorithm

import math
import time
import matplotlib.pyplot as plt


def prime_numbers(n):
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        # if prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
            # update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    # create a list of prime numbers
    prime_numbers = []
    for i in range(2, n+1):
        if prime[i]:
            prime_numbers.append(i)
    return prime_numbers

# plot time complexity of the algorithm
def plot_time_complexity():
    prime_numbers1 = []
    # create a list of n values
    n = [100, 1000, 10000, 100000, 1000000]
    # create a list of time values
    time1 = []
    # calculate time for each n value
    for i in n:
        start = time.time()
        prime_numbers1 = prime_numbers(i)
        end = time.time()
        time1.append(end - start)
    # plot the time complexity
    plt.plot(n, time1, label = "Sieve of Eratosthenes")
    plt.xlabel('n')
    plt.ylabel('time')
    plt.title('Time Complexity of Prime Number Algorithm')
    plt.legend()
    plt.show()

plot_time_complexity()




from matplotlib import pyplot as plt
import timeit


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
        
def fib2(n, cache={}):

    if n == 0 or n == 1:
        return n
    
    else:
        if n in cache:
            return cache[n]
        else:
            cache[n] = fib2(n-1) + fib2(n-2)
            return cache[n]



n_values = []
time_values = []

for i in range(1, 500):
    elapsed_time = timeit.timeit('fib2({})'.format(i), globals=globals(), number=1)
    n_values.append(i)
    time_values.append(elapsed_time)

plt.plot(n_values, time_values, 'ro')
plt.xlabel('nth Fibonacci number')
plt.ylabel('Time (in seconds)')
plt.title('Fibonacci number vs time to compute')

plt.show()
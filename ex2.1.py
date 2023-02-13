
import json
import timeit
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(20000)

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi + 1, high)
        
def partition(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

# Load the JSON file
with open('data.json') as f:
    data = json.load(f)

# Keep track of the time taken to sort each array
times = []
for array in data:
    time_taken = timeit.timeit(lambda: quicksort(array,0,len(array)-1), number=1)
    times.append(time_taken)

# Plot the time taken to sort each array
plt.plot(times,len(array))
plt.xlabel('Array Index')
plt.ylabel('Time (s)')
plt.title('Quicksort Performance')
plt.show()
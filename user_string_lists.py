"""
Modify this docstring.

"""

import math
import statistics

list1 = [62, 37, 45, 39, 40, 41, 65, 44, 56, 46, 64, 35, 46, 22, 2, 65, 245, 22, 25, 78]
listx = list(range(10))
listy = [47, 77, 56, 77, 356, 4, 76, 56, 55, 67]

mean = statistics.mean(list1)
median = statistics.median(list1)
try:
    mode = statistics.mode(list1)
except statistics.StatisticsError:
    mode = None

def CalculateStandardDeviation(lst):
    n = len(lst)
    mean = sum(lst) / n
    variance = sum((x - mean) ** 2 for x in lst) / n
    StandardDeviation = math.sqrt(variance)
    return StandardDeviation

StandardDeviation = CalculateStandardDeviation(list1)
variance = StandardDeviation ** 2

print("Mean: ", mean)
print("Median: ", median)
print("Mode: ", mode)
print("Standard Deviation: ", StandardDeviation)
print("Variance: ", variance)


# Calculate the correlation between listx and listy
correlation = statistics.correlation(listx, listy)

# Calculate the slope and intercept of the best-fit line
slope, intercept, rvalue, pvalue, stderr = statistics.linregress(listx, listy)

# Set a future time = 15
future_time = 15

# Predict the y value at the future time
predicted_y = slope * future_time + intercept

# Print the results
print(f"Correlation between listx and listy: {correlation}")
print(f"Slope of the best-fit line: {slope}")
print(f"Intercept of the best-fit line: {intercept}")
print(f"Predicted y-value at time {future_time}: {predicted_y}")


# task 3

# Use the built-in functions
minimum = min(list1)
maximum = max(list1)
length = len(list1)
total = sum(list1)
average = total / length
unique_elements = set(list1)
sorted_list = sorted(list1)
reverse_sorted_list = sorted(list1, reverse=True)

# Print the results
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Length: {length}")
print(f"Total: {total}")
print(f"Average: {average}")
print(f"Unique Elements: {unique_elements}")
print(f"Sorted List: {sorted_list}")
print(f"Reverse Sorted List: {reverse_sorted_list}")

# list 4
# Create a new list
lst = [2, 4, 6, 8, 10]

# Use the list methods
lst.append(12)
lst.extend([14, 16, 18])
lst.insert(2, 5)
lst.remove(6)
count = lst.count(4)
lst.sort()
lst.sort(reverse=True)
lst_copy = lst.copy()
popped_first = lst.pop(0)
popped_last = lst.pop(-1)

# Print the results
print(f"List after append: {lst}")
print(f"List after extend: {lst}")
print(f"List after insert: {lst}")
print(f"List after remove: {lst}")
print(f"Count of 4: {count}")
print(f"List after sort: {lst}")
print(f"List after reverse sort: {lst}")
print(f"List copy: {lst_copy}")
print(f"Popped first: {popped_first}")
print(f"Popped last: {popped_last}")

# filter
import math

# Using filter() to keep values less than 4
lst = [1, 2, 3, 4, 5, 6, 7]
filtered_list = list(filter(lambda x: x < 4, lst))
print("Values less than 4:", filtered_list)

# Using filter() to keep even values
lst = [1, 2, 3, 4, 5, 6, 7]
filtered_list = list(filter(lambda x: x % 2 == 0, lst))
print("Even values:", filtered_list)

# map
import math

# Using map() to find cube root of values in the list
lst = [1, 2, 3, 4, 5, 6, 7]
cuberoot_list = list(map(lambda x: math.pow(x, 1/3), lst))
print("Cube root of values in the list:", cuberoot_list)

# volume 
# Using map() to calculate volume of a cube
lst = [1, 2, 3, 4, 5, 6, 7]
volume_list = list(map(lambda x: x**3, lst))
print("Volume of cubes with sides equal to values in the list:", volume_list)

# list 6






# imports first

# reusable functions next

# call functions and execute code
# use if __name__ == "__main__":

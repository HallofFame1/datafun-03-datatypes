"""
Modify this docstring.

"""

# import some modules first - how many can you make use of?

import math
import statistics as stats
from statistics import LinearRegression


# define some functions


def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?

    """

    # Use a try / except / finally block when something
    # could go wrong
    try:
        area = 0  # fix this
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("your code here")

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
listx = list(range(10))
listy = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]

# Mean
mean = stats.mean(list1)
print("Mean:", mean)

# Median
median = stats.median(list1)
print("Median:", median)

# Mode
mode = stats.mode(list1)
print("Mode:", mode)

# Standard Deviation
stdev = stats.stdev(list1)
print("Standard Deviation:", stdev)


#LIST Using Python built in functions
# Use the min() function to find the minimum value
minimum = min(list1)
print("The minimum value is:", minimum)

# Use the max() function to find the maximum value
maximum = max(list1)
print("The maximum value is:", maximum)

# Use the len() function to find the length of the list
length = len(list1)
print("The length of the list is:", length)

# Use the sum() function to find the sum of the values in the list
total = sum(list1)
print("The sum of the values is:", total)

# Use the average of the sum and the length to find the average of the values
average = total / length
print("The average of the values is:", average)

# Use the set() function to find the unique values in the list
unique_values = set(list1)
print("The unique values are:", unique_values)

# Use the sorted() function to sort the values in the list
sorted_values = sorted(list1)
print("The sorted values are:", sorted_values)

# Use the sorted() function with reverse=True to sort the values in reverse order
sorted_values_reverse = sorted(list1, reverse=True)
print("The sorted values in reverse order are:", sorted_values_reverse)
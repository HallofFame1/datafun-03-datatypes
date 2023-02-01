import math

lst = [1, 23, 4, 7, 6, 65, 4, 56, 69, 10]

# Use the built in filter() function to keep x such that x is less than 4
filtered_lst = list(filter(lambda x: x < 4, lst))
print("Filtered list:", filtered_lst)

# Use the built in map() function to map each x to cube root of x
cuberoot_lst = list(map(lambda x: math.pow(x, 1/3), lst))
print("Cubed root list:", cuberoot_lst)

# Use the built in map() function to calculate the volume of a cube with a side equal to the value in your list
volume_lst = list(map(lambda x: x * x * x, lst))
print("Volume list:", volume_lst)
import math
import statistics as stats

lst = [3, 5, 6, 6, 4, 7]

# 1. append a single value to the list
lst.append(6)
print("After append:", lst)

# 2. extend the list with a new list
new_lst = [7, 8, 9]
lst.extend(new_lst)
print("After extend:", lst)

# 3. insert at an index
lst.insert(0, 0)
print("After insert:", lst)

# 4. remove a value from the list
lst.remove(5)
print("After remove:", lst)

# 5. count the number of occurrences of a value
print("Count of 2:", lst.count(2))

# 6. sort the list
lst.sort()
print("After sort:", lst)

# 7. sort the list in descending order
lst.sort(reverse=True)
print("After sort, reverse=True:", lst)

# 8. copy the list
copy_lst = lst.copy()
print("After copy:", copy_lst)

# 9. pop the first item off the top of the list
print("Popped first item:", lst.pop(0))
print("After pop:", lst)

# 10. pop the last item off the bottom of the list
print("Popped last item:", lst.pop())
print("After pop:", lst)
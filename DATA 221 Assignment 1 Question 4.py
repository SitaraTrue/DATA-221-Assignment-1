# Sorted Search with Conditions

from random import random

# Generating a list of ascending random values between 0 and 1, and a single threshold value x between 0 and 1
list_of_random_values = [random() for i in range(20)]
sorted_list_of_random_values = sorted(list_of_random_values)
threshold_value_x = random()

# Making a list of all indices corresponding to random values >= x
list_of_indices = []
for index in range(0,len(sorted_list_of_random_values)):
    if sorted_list_of_random_values[index] >= threshold_value_x:
        list_of_indices.append(index)

print(f"The sorted list is {sorted_list_of_random_values} and the value of threshold x is {threshold_value_x}.")
if sorted_list_of_random_values != []: # States the first index of the sorted list that is greater than or equal to x unless none exist
    print(f"The first index that is greater than or equal to x is {list_of_indices[0]}.")
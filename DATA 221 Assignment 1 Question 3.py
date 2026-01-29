# Safe Function Application

# Defining the function to calculate x^y
def compute_power(x, y):
    return x**y

# Defining the function to loop through a nested list of arguments and call compute_power() on each inner list
def make_list_of_compute_power_results(pairs):
    list_of_results = []
    for x_y_pair in pairs:
        if x_y_pair[1] < 0: # Skips any pairs with a negative exponent
            continue
        else:
            result = compute_power(*x_y_pair) # Unpacking arguments
            list_of_results.append(result) # Adding the result to the list
    return list_of_results

# Function call
print(make_list_of_compute_power_results([[5,2], [3,-1], [4,3], [2,0]]))
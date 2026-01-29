# Controlled Multiplication Loop

# Defining variables for the product, the current number to multiply it by, and the threshold for it to pass
product_threshold = 100
total_product = 1
current_number = 1

# Each iteration of the loop multiplies the product by the next consecutive integer
while total_product <= product_threshold:
    total_product *= current_number
    if total_product >= product_threshold:
        break
        # Loop breaks if the product exceeds the threshold (before the current number increases)
    else:
        current_number += 1

print(f"The final product is {total_product}, and the number that pushed it over the threshold of {product_threshold} is {current_number}.")
# Circle Area Comparison with Validation

import math

# Defining function to find two circle areas and the percentage of the larger circle's area that the smaller one covers
def find_circle_area_coverage(radius_of_first_circle, radius_of_second_circle):
    # Calculating the areas
    if radius_of_first_circle > 0 and radius_of_second_circle > 0: # Validates both integers are positive
        area_of_first_circle = math.pi * (radius_of_first_circle**2)
        area_of_second_circle = math.pi * (radius_of_second_circle**2)

        # Making a sorted list of both areas to determine which is smaller
        circle_list = [area_of_first_circle, area_of_second_circle]
        circle_list = sorted(circle_list)

        percent_coverage = (circle_list[0]/circle_list[1]) *100 # Finding the percent coverage
        return percent_coverage
    else: # Met if one or both of the radii were negative
        return "Invalid input provided. Please try again."

# Getting input from the user
circle1_radius = int(input("Enter the radius of the first circle: "))
circle2_radius = int(input("Enter the radius of the second circle: "))

# Function call
print(find_circle_area_coverage(circle1_radius, circle2_radius))
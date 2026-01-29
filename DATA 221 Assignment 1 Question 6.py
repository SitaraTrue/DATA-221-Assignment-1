# Distribution Analysis

# Defining the function to create a dictionary mapping keys to percentages
def create_percentage_dictionary(list_of_numbers):
    percentage_dictionary = {}
    for number in list_of_numbers:
        if number not in percentage_dictionary.keys(): # Will only run for unique keys

            # Determining how many elements are less than or equal to the key
            count_less_than_or_equal_to = 0
            for element in list_of_numbers:
                if element <= number:
                    count_less_than_or_equal_to += 1

            # Determining the percentage of elements that are less than or equal to the key
            percentage_less_than_or_equal_to = 100*(count_less_than_or_equal_to/len(list_of_numbers))
            percentage_dictionary[number] = percentage_less_than_or_equal_to

    percentage_dictionary = dict(sorted(percentage_dictionary.items()))
    return percentage_dictionary

# Function call
print(create_percentage_dictionary([3,1,2,3,4,2]))
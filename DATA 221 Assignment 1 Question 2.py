# Nested Dictionary from Strings

# Defining the function to convert a list of strings to a nested dictionary
def convert_list_to_dictionary(list_of_strings):
    dictionary_of_strings = {}
    for element in list_of_strings: # Traversing through the list to create a new key-value pair for each element
        dictionary_of_length_and_parity = {}

        # Finding the length and mapping it to "length" in the nested dictionary
        string_length = len(element)
        dictionary_of_length_and_parity["length"] = string_length

        # Finding whether string length is even or odd and mapping it to "parity" in the nested dictionary
        if string_length%2 == 0:
            string_parity = "even"
        else:
            string_parity = "odd"
        dictionary_of_length_and_parity["parity"] = string_parity # Maps "parity" to the string parity

        # Creates key value pairs mapping each string to a dictionary of its length and parity
        dictionary_of_strings[element] = dictionary_of_length_and_parity
    return dictionary_of_strings # Returns complete dictionary

# Function call
print(convert_list_to_dictionary(["This", "is", "a", "dictionary", "now."]))

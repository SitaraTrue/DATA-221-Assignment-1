# Time Conversion Function

# Defining function to convert seconds to time
def convert_seconds_to_time(number_of_seconds):
    if number_of_seconds < 86400 and number_of_seconds >= 0: # Validating input

        # Determining AM or PM
        if number_of_seconds <= 43199:
            meridiem = "AM"
        else:
            meridiem = "PM"

        # Calculating the time
        if number_of_seconds > 43199:
            number_of_seconds -= 43200
        number_of_hours = number_of_seconds // 3600
        number_of_minutes = (number_of_seconds - (number_of_hours * 3600)) // 60
        leftover_seconds = number_of_seconds % 60
        if number_of_hours == 0:
            number_of_hours = 12

        return f"{number_of_hours} {number_of_minutes} {leftover_seconds} {meridiem}"
    else:
        return "Invalid input. Please enter a number between 0 and 86,399."

# Getting input from the user and calling the function
given_seconds = int(input("Enter the number of seconds since midnight: "))
print(convert_seconds_to_time(given_seconds))

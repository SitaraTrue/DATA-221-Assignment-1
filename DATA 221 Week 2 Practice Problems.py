'''
1. Even or Odd?
Write a Python function is.even(n) that returns True if even and False otherwise.
'''

def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False

print(is_even(7))
print(is_even(12))
print(is_even(-4))

'''
2. Grade Calculator
Write a function letter_grade(score) that returns a letter grade.
'''

def letter_grade(score):
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 60 and score < 70:
        return "D"
    elif score >= 0 and score < 60:
        return "F"
    else:
        return "Invalid"

print(letter_grade(95))
print(letter_grade(83))
print(letter_grade(72))
print(letter_grade(61))
print(letter_grade(40))
print(letter_grade(-4))
print(letter_grade(101))

'''
3. Sum of Numbers
Write a function sum_to_n(n) that returns the sum 1+2+3+...+n through a loop.
'''

def sum_to_n(n):
    if n<=0:
        return 0
    else:
        total=0
        for num in range(1,n+1):
            total += num
    return total

print(sum_to_n(10))
print(sum_to_n(1))
print(sum_to_n(-1))

'''
4. Multiplication Table
Write a function print_table(n) that prints the multiplication table for n from 1 to 10.
'''

def print_table(n):
    mult_table = []
    for i in range (1,11):
        result = n*i
        mult_table.append(f"{n} x {i} = {result}")
    return mult_table

print(print_table(5))
print(print_table(12))

'''
5. Count Vowels
Write a function count_vowels(s) that counts how many vowels are in a string.
'''

def count_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowel_count = 0
    for char in s:
        if char in vowels:
            vowel_count += 1
    return vowel_count

print(count_vowels("data science"))
print(count_vowels("PYTHON"))

'''
6. Factorial
Write a function factorial(n) that returns n! using a loop.
'''

def factorial(n):
    result = 1
    if n<0:
        return None
    else:
        for i in range(n, 1, -1):
            result *= i
        return result

print(factorial(5))
print(factorial(0))
print(factorial(-1))

'''
7. Prime Checker
Write a function is_prime(n) that returns True if n is prime and False otherwise.
'''

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n%i==0:
                return False
                break
            else:
                continue
        return True

print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(9))
print(is_prime(17))

'''
8. Guess the Number
Write a program that repeatedly asks the user to guess a secret number.
'''

def guess_secret_number(num):
    guess = int(input("Guess a number:"))
    num_guesses = 1
    if guess == num:
        print("You are correct.")
    else:
        while not(guess==num):
            num_guesses += 1
            if guess > num:
                print("Too high")
            elif guess< num:
                print("Too low")
            else:
                print("You are correct")
            guess = int(input("Guess a number:"))
    return num_guesses

print(guess_secret_number(23))

'''
9. Simple Calculator
Write a function calculate(a,b, op) where op is one of +, -, *, /.
'''

def calculate(a, b, op):
    if op == '+':
        return (a+b)
    elif op=='*':
        return (a*b)
    elif op=='-':
        return (a-b)
    elif op == '/':
        if b == 0:
            return "Cannot divide by 0."
        else:
            return (a/b)
    else:
        return "Invalid operator."

print(calculate(2,0,'/'))

'''
10. List Statistics
Write a function list_stats(nums) that takes a list of numbers and returns a tuple (min, max, average).
'''

def list_stats(nums):
    if len(nums) == 0:
        return None
    else:
        min = nums[0]
        for i in nums:
            if i < min:
                min = i
            else:
                continue
        max = nums[0]
        for j in nums:
            if j > max:
                max = j
            else:
                continue
        total = 0
        for k in nums:
            total += k
        avg = total/len(nums)
        return (min, max, avg)

print(list_stats([3,5,7,2,9]))
print(list_stats([10]))
print(list_stats([]))

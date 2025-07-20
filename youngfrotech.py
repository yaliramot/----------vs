num_str="123"
num_int=int(num_str)
result=num_int+10
print(result)

# This code performs basic arithmetic operations based on user input
x=input("enter first number")
operator=input("enter one mathematical operator (+,-,*,/)")
y=input("enter second number")

x=float(x)
y=float(y)

if operator== '+': 
    print(x+y)
elif operator=='-':
    print(x-y)
elif operator=='*':
    print(x*y)
elif operator=='/':
    print(x/y)

else:
    print(" unknown operator")


# This code calculates the sum of squares of even numbers in a list
sum = 0
l = [1, 2, 3, 4, 5]

for item in l:
    if item % 2 == 0:
        square = item * item
        sum += square

print(sum)


    
# Simple number guessing game# This code generates a random number between 1 and 100 and prompts the user to guess it
# The user is informed if their guess is too low or too high until they guess correctly
import random 

secret_number = random.randint(1, 100)
guess=0
attempts = 0

while guess != secret_number:
  guess = int(input("Guess the secret number between 1 and 100: ")) 
  attempts += 1

  if guess < secret_number:
        print("Too low! Try again.")   
  elif guess > secret_number: 
      print("Too high! Try again.")

print("Congratulations! You've guessed the secret number in [attempts] attempts:")

# Function to convert Celsius to Fahrenheit and vice versa
# This function takes a temperature in Celsius and converts it to Fahrenheit
def celcius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Input temperature in Celsius and convert to Fahrenheit
# This code prompts the user to enter a temperature in Celsius and converts it to Fahrenheit
celcius=float(input("Enter temperature in Celsius: "))
fahrenheit=celcius_to_fahrenheit(celcius)
print(f"{celcius}°C is equal to {fahrenheit}°F")



numbers=[3,5,2,8,1,9,4]
max_number=0
# Finding the maximum number in a list
# This code iterates through the list and updates max_number if a larger number is found
for number in numbers:
    if number > max_number:
        max_number = number
print(f"The maximum number in the list is: {max_number}")

# Function to find even numbers in a list
# This function iterates through the original list and appends even numbers to a new list
def evennumber(original_list):
    even_numbers = []
    for number in original_list:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

original_list = [1, 4, 5, 7, 8, 10, 13] 
even_numbers_list = evennumber(original_list)
print(even_numbers_list)

# Function to check if a list is sorted in ascending order
# This function checks if the list is sorted in ascending order by comparing each element with the next
def is_sorted_ascending(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

test_list = [1, 2, 3, 4, 5]
if is_sorted_ascending(test_list):
    print("The list is sorted in ascending order.") 
else:
    print("The list is not sorted in ascending order.")

# Checking if a list is sorted in ascending order
# This code checks if the list is sorted in ascending order by comparing each element with the next
my_list = [1, 2, 3, 4, 5]
sorted = True

for i in range(len(my_list) - 1):
    if my_list[i] > my_list[i + 1]:
        sorted = False
        break   
if sorted:
    print("The list is sorted in ascending order.")
else:
    print("The list is not sorted in ascending order.")


# Function to reverse a string
# This function takes a string and returns its reverse
text = "Hello, World!"
reversed_text = text[::-1]
print(reversed_text)


# Function to check the number of vowel points in a word
word = input("Enter a word: ").lower()  # Convert input to lowercase for consistency
vowels = "aeiou"
vowel_count = 0

# לולאה שעוברת על כל תו במילה
for char in word:
    if char in vowels:
        vowel_count += 1
print(f"The number of vowel points in the word '{word}' is: {vowel_count}")


 
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_in_range(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)

print_primes_in_range(1, 100)


def is_polindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]  # Check if the string is equal to its reverse

check_string = input("Enter a string to check if it's a palindrome: ")
if is_polindrome(check_string):
    print(f"'{check_string}' is a palindrome.")     
else:
    print(f"'{check_string}' is not a palindrome.")



def find_longest_word(sentence):
    words = sentence.split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

sentence = input("Enter a sentence: ")
longest_word = find_longest_word(sentence)
print(f"The longest word is: {longest_word}")

words_list = ["apple", "banana", "cherry", "dateio"]
longest_word = find_longest_word(" ".join(words_list))
print(f"The longest word in the list is: {longest_word}")


words_list = ["level", "radar", "hello", "world", "madam"]
is_polindroms_list = []
for word in words_list:
    if is_polindrome(word):
        is_polindroms_list.append(word)   
print(f"Palindromes in the list: {is_polindroms_list}")


my_set = {1, 2, 3, 4, 5}
print(my_set)

my_set.add(6)  # Add an element to the set
print(my_set)

my_set.remove(3)  # Remove an element from the set
print(my_set)

my_set.discard(2)
print(my_set)


set_a= {1, 2, 3}
set_b = {3, 4, 5}
print(set_a.union(set_b))  # Union of two sets

print(set_a.intersection(set_b))  # Intersection of two sets


new_list = [3, 7, 11, 17, 23]
new_list.append(29)  # Add an element to the end of the list
new_list.append(31)  

new_tuple = tuple(new_list)  # Convert the list to a tuple

lengthe_of_tuple=len(new_tuple)  # Get the length of the tuple

number_to_check = 17
is_number_in_tuple = number_to_check in new_tuple  # Check if a number is in the tuple

first_list = [1, 2, 3]
second_list = [4, 5, 6]
merged_list=[*first_list, *second_list]  # Merge two lists using unpacking
print (merged_list)
 
my_list = [1, 2, 3, 4, 5]
sliced_list = my_list[1:4]  # Slice the list from index 1 to 3
print(sliced_list)  # Output: [2, 3, 4]


def get_value(dictionary, key):
    is_value_in_dictionary = key in dictionary  # Check if the key exists in the dictionary
    if is_value_in_dictionary:
        return dictionary[key]
    else:
        KeyError (f"Key '{key}' not found in the dictionary.")

dictionary = {'a': 1, 'b': 2, 'c': 3}
key_to_check = 'b'
value = get_value(dictionary, key_to_check) 
print(value) # Get the value associated with the key


def uonion_sets(set_a, set_b):
        print (set_a.union(set_b))  # Return the union of two sets   

        set_a = {1, 2, 3}
        set_b = {3, 4, 5}
        uonion_sets(set_a, set_b)  # Call the function to get the union of the sets


# Function to count occurrences of values in a list of tuples
# This function takes a list of tuples and counts how many times each value appears across all tuples
def count_values(tuples_list):
    count={}
    for tup in tuples_list:
        for value in tup:
            if value in count:
                count[value] += 1
            else:
                count[value] = 1

    return count

# Example usage of the count_values function
data = [(1, 2), (3, 2), (1, 4), (2, 2)]
result = count_values(data)
print(result)



def get_grades():
    grades = []
    while True:
        grade = open(input("Enter grades (or 'done' to finish): "))
        if grade.lower() == 'done':
            break
        try:
            grades.append(float(grade))
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
            for line in grades:
                sum_grades=+ line
    average_grades = sum_grades / len(grades) if grades else 0
    print(f"The average of the grades is: {average_grades}")
\
# Class definition for a Dog
class dog:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def bark(self):
            print(f"{self.name} says Woof!")

if __name__ == "__main__":
    my_dog= dog("rex",2)
    my_dog.bark()  # Call the bark method of the Dog class

# Class definition for an Animal with a method to talk
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        def talk(self):
            print(f"Hi I'm {self.name} and my age is str{self.age}")
                
our_animal = Animal("Leo", 5)
our_animal.talk()

our_animal2 = Animal("Milo", 3)
our_animal2.talk()



class Person:
    def __init__(self,  first_name, last_name,):
        self.first_name = first_name
        self.last_name = last_name

        def full_name(self):
            print(f"My full name is {self.first_name} {self.last_name}")
    
    new_person = Person("John", "Doe")
    print(new_person.full_name())  # Output: my full name is John Doe
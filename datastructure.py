#number 1
# Accept user input to create a list of integers
numbers = input("Enter a list of integers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

# Compute the sum of the integers in the list
total_sum = sum(numbers)
print("Sum of the integers:", total_sum)


#number 2
# Prompt the user to enter the names of five favorite books
print("Enter the names of your five favorite books, one at a time:")

favorite_books = tuple(input(f"Book {i + 1}: ") for i in range(5))

# Print each book name on a separate line using a for loop
print("Your favorite books:")
for i, book in enumerate(favorite_books):
    print(f"Book {i + 1}: {book}")


#number 3
# Ask the user for input to store information about a person
person = {}
person['name'] = input("Enter your name: ")
person['age'] = input("Enter your age: ")
person['favorite_color'] = input("Enter your favorite color: ")

# Print the dictionary containing the person's information
print("Person's Information:")
for key, value in person.items():
    print(key + ":", value)



#number 4
# Accept user input to create two sets of integers
set1 = set(input("Enter integers for the first set separated by spaces: ").split())
set2 = set(input("Enter integers for the second set separated by spaces: ").split())

# Find the intersection of the two sets
common_elements = set1.intersection(set2)
print("Common elements in both sets:", common_elements)

#Number 5
# Store a list of words
word_list = ["apple", "banana", "orange", "grape", "kiwi"]

# Use list comprehension to create a new list with words having odd number of characters
odd_length_words = [word for word in word_list if len(word) % 2 != 0]
print("Words with odd number of characters:", odd_length_words)

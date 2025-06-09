#Debugging old code for Module 2.2 Assignment

# This program provides a menu for string manipulation tasks.
# It allows the user to convert a string to uppercase or lowercase,
# count the number of words, count the number of vowels, or exit the program.
#Garrett Rohde 10/31/2022
# File: displayMenu.py

def displayMenu():
    print('Enter 1 to convert a string to uppercase')
    print('Enter 2 to convert a string to lowercase')
    print('Enter 3 to count the number of words in a string')
    print('Enter 4 to count the number of vowels in a string')
    print('Enter 5 to exit')

def get_nonempty_string(prompt):
    user_string = input(prompt)
    while len(user_string.strip()) == 0:
        user_string = input("Incorrect entry.\nEnter a string: ")
    return user_string

def upper(user_string):
    print(f'"{user_string}" to uppercase is {user_string.upper()}')

def lower(user_string):
    print(f'"{user_string}" to lowercase is {user_string.lower()}')

def count_words(user_string):
    user_list = user_string.split()
    print(f'"{user_string}" has {len(user_list)} words')

def count_vowels(user_string):
    count = 0
    vowels = 'aeiou'
    string = user_string.lower()
    for c in string:
        if c in vowels:
            count += 1
    print(f'"{user_string}" has {count} vowels')

def main():
    choice = 0
    while choice != 5:
        displayMenu()
        try:
            choice = int(input('Enter your choice: '))
        except ValueError:
            print("Please enter a valid number from 1 to 5.")
            continue

        if choice == 1:
            user_string = get_nonempty_string('Enter a string: ')
            upper(user_string)
        elif choice == 2:
            user_string = get_nonempty_string('Enter a string: ')
            lower(user_string)
        elif choice == 3:
            user_string = get_nonempty_string('Enter a string: ')
            count_words(user_string)
        elif choice == 4:
            user_string = get_nonempty_string('Enter a string: ')
            count_vowels(user_string)
        elif choice == 5:
            print('Closing program')
        else:
            print('Enter a choice from 1 to 5')

if __name__ == "__main__":
    main()

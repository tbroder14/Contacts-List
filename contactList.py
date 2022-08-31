# Contact List App TODO
# ask user if they want to add, edit or view a contact dictionary
# if they want to view it then show the entire dictionary of names and numbers
# if they want to add then ask for a name and number and add to the contact list
# if they want to edit ask them which name to edit then what the updated number should be
# after getting updated info to edit show them the updated name/number
#
# Example of a Dictionary
# contacts = { "josh": "123-123-1234", "jordan": "234-234-2345" }
# print(contacts{"josh"})
# output: 123-123-1234
#
# NOTES
# Python "Dictionaries" cannot have duplicate keys, so you can't have 2 "josh" in your list (it will just overwrite original)
# If someone tries to add a name that already exists ask if they
# would like to instead edit the current record of that name or change that name to something else

# Bonus
# When a number is added/edited make sure it is a 10 digit long number and add hyphens if user does not include them
# Hint: use "Regex" or "Regular expression" good luck lol

# Super Bonus
# Create a new GitHub repo and push this project to it

# Super Duper Bonus
# save data between executions of the program by saving to a .txt file
# Hint: http://automatetheboringstuff.com/2e/chapter9/
# You don't need to read the whole thing, but it has info about reading/writing to a file

from time import sleep
from newContact import *
from editContact import *

sleep(0.5)
print("Welcome to your contacts list!")
sleep(0.85)

contacts = {"josh": '12345', "Trevor": "12345"}

while True:

    selection = input("Would you like to add a new contact [N], edit an existing contact [E], or view your entire contact list [V]?" + "\n").lower()
    if selection == "n":
        contacts = newContact(contacts)
        print(contacts)

    elif selection == "e":
        contacts = editContact(contacts)

    elif selection == "v":
        for i in contacts:
            print(f"{i}: {contacts[i]}")
            sleep(0.35)

    else:
        print("Please select a valid option by typying either [N], [E], or [V].")
        continue

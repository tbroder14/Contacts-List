from phoneNumberFormat import *

def editContact(contacts):
    print("Which contact would you like to edit?")
    for i in contacts:
        print(f"{i}: {contacts[i]}")

    # ask for user input
    editName = input()

    # check to verify if user input is in dictionary
    nameFound = False
    for name in contacts:
        if editName == name:
            nameFound = True

    # if input is in dictionary, then ask the user for the updated phone number
    if nameFound:
        editNumber = input("Please enter the updated phone number." + "\n")
        editNumber = phoneValidator(editNumber)
        contacts[editName] = editNumber

    else:
        print("Name not found.")

    # once phone number is updated, print the contact name with the updated phone number
    return contacts

from phoneNumberFormat import *

def newContact(contacts):

    newContactName = str(input("Please enter the name of your new contact below:" + "\n"))

    # check to verify if user input is in dictionary
    nameFound = False
    for name in contacts:
        if newContactName == name:
            nameFound = True

    # if input is in dictionary, then ask the user for the updated phone number
    if nameFound:
        duplicate = input(f"This contact already exists. Would you like to update the number for {newContactName}? Type Y or N." + "\n").lower()
        if duplicate == "y":
            editNumber = input(f"Please enter the updated number for {newContactName}."+ "\n")
            editNumber = phoneValidator(editNumber)
            contacts[newContactName] = editNumber

    elif not nameFound:
        newContactNumber = str(input(f"Please enter the telephone number for {newContactName}:" + "\n"))
        newContactNumber = phoneValidator(newContactNumber)
        contacts.update({newContactName: newContactNumber})

    while True:
        mmAfterNew = input("Would you like to add an additional new contact [N] or return to the main menu [M]?" + "\n").lower()
        if mmAfterNew == "n":
            contacts = newContact(contacts)
            # contacts = phoneValidator(newContactNumber)
            # print(contacts)
        else:
            break

    return contacts






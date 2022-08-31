def newContact(contacts):

    newContactName = str(input("Please enter the name of your new contact below:" + "\n"))
    newContactNumber = str(input(f"Please enter the telephone number for {newContactName}:" + "\n"))

    contacts.update({newContactName: newContactNumber})

    while True:
        mmAfterNew = input("Would you like to add an additional new contact [N] or return to the main menu [M]?" + "\n")
        if mmAfterNew == ("N" or "n"):
            contacts = newContact(contacts)
            print(contacts)
        else:
            break

    return contacts
# # CSV (comma separated value), stored in .txt files
import csv
from contactList import *

# openFile = open("numbers.txt", "r")
# openFile.write("lynzi, 12345" + "\n")
# openFile.write("trevor, 1235")
# openFile.close()
#
# # #open file
# openFile = open("numbers.txt", "r")
# #
# # #read contents set to a variable
# readFile = openFile.read()
#
# # #close file
# openFile.close()

#open file

openFile = open("contactList.txt", "w")

openFile.write("Contact List:" + "\n")
content = openFile.write(contactList.py)

print(content)
openFile.close()

# updatedText = readFile + "\n" + userInput
# openFile.write(updatedText)
# print(updatedText)


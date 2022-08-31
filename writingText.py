# # CSV (comma separated value), stored in .txt files
# import csv
#
# openFile = open("numbers.txt", "r")
# openFile.write("lynzi, 12345" + "\n")
# openFile.write("trevor, 1235")
# openFile.close()

# #open file
openFile = open("numbers.txt", "r")
#
# #read contents set to a variable
readFile = openFile.read()

# #close file
openFile.close()

#open file
openFile = open("numbers.txt", "w")
userInput = input("Enter record." + "\n")
updatedText = readFile + "\n" + userInput
openFile.write(updatedText)
# print(updatedText)

openFile.close()
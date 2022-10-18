import re

def phoneValidator(phoneNumber):

    while True:
        if len(phoneNumber) != 10:
            phoneNumber = input("Please type a 10 digit phone numbers (without any special characters or dashes)." + "\n")
        elif len(phoneNumber) == 10:
            try:
                if int(phoneNumber) > 0:
                    cleanPhoneNumber = re.sub('[^0-9]+', '', phoneNumber)
                    formattedPhoneNumber = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(cleanPhoneNumber[:-1])) + \
                                               cleanPhoneNumber[-1]
                    phoneNumber = formattedPhoneNumber
                    return phoneNumber
                else:
                    phoneNumber = input(
                        "Please type a 10 digit phone numbers (without any special characters or dashes)." + "\n")
            except:
                phoneNumber = input(
                    "Please type a 10 digit phone numbers (without any special characters or dashes)." + "\n")
                continue

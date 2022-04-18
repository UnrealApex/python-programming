class SSN:
    def __init__(self, number):
        self.number = number

    def getSSN(self):
        """return the SSN"""
        return self.number

    def validate(self):
        """
        validate if the SSN is in the correct format (xxx-xx-xxxx)
        note that this method does not check if the parts of the SSN are within the correct range
        """
        no_hyphen = self.number.split("-")
        if (not(len(no_hyphen[0]) == 3 and len(no_hyphen[1]) == 2 and len(no_hyphen[2]) == 4)):
            print("Invalid SSN")
        else:
            print("Valid SSN")


x = SSN("123-45-6789")
x.validate()

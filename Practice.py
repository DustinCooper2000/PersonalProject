#################################################################################################################
# Dustin Cooper
# April 3rd
# Just for fun
#
################################################################################################################

class Calculator:

    def __init__(self):
        self.operator = ""
        self.x = 0
        self.y = 0
        self.again = ""
        self.clear = ""
        self.PastResult = 0

    def imply(self):
        while self.again != "n":
            if self.clear == "n":
                self.x = self.PastResult
            else:
                self.x = int(input("what is the first number you would like to use?"))

            self.operator = input("Which operator would you like to use?")
            self.y = int(input("What is the second number you would like to use?"))
            if self.operator == "+":
                self.PastResult = self.add(self.x, self.y)

            elif self.operator == "-":
                self.PastResult = self.subtract(self.x, self.y)

            elif self.operator == "*":
                self.PastResult = self.multiply(self.x, self.y)

            elif self.operator == "/":
                self.PastResult = self.divide(self.x, self.y)

            elif self.operator == "**":
                self.PastResult = self.exponent(self.x, self.y)

            self.again = str(input("Would you like to make another calculation? (y/n)")).lower()
            print(self.again)
            if self.again == "y":
                self.clear = str(input("Would you like to clear your result? (y/n)")).lower()
                if self.clear == "y":
                    self.PastResult = 0


    def add(self, x, y):
        r = x + y
        print(r)
        return r

    def subtract(self, x, y):
        r = x - y
        print(r)
        return r

    def multiply(self, x, y):
        r = x * y
        print(r)
        return r

    def divide(self, x, y):
        r = x/y
        print(r)
        return r

    def exponent(self, x, y):
        r = x**y
        print(r)
        return r

def main():

    calculate = Calculator()
    calculate.imply()


if __name__ == "__main__":
    main()


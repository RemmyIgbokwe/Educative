class Beverage:  # parent class
    def setSales(self, sales):  # defining the set
        self.setSales = sales
        print("The Sales this year is ", self.setSales)


class Juice(Beverage):  # child class of Beverage
    def numberOfLitres(self):
        print("This drink is 300cl. ")


class HappyHour(Juice):  # child class of Juice
    def turnOnHappyHour(self):
        print("Happy Hour is now up for Sale. ")


priusPrime = HappyHour()  # creating an object of the HappyHour class
priusPrime.setSales(500)  # accessing methods from the parent class
priusPrime.numberOfLitres()  # accessing method from the parent class
priusPrime.turnOnHappyHour()  # accessing method from the child class
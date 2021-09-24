class Stadium:  # Parent class
    def setSeats(self, seats):
        self.seats = seats


class Anfield(Stadium):  # Child class inherited from Engine
    def setAnNumberOfSeats(self, AnNumberOfSeats):
        self.AnNumberOfSeats = AnNumberOfSeats


class Old_Trafford(Stadium):  # Child class inherited from Engine
    def setOtNumberOfSeats(self, OtNumberOfSeats):
        self.OtNumberOfSeats = OtNumberOfSeats

# Child class inherited from CombustionEngine and ElectricEngine


class HybridStadium(Anfield, Old_Trafford):
    def printDetails(self):
        print("Seats:", self.seats)
        print("Anfield Number Of Seats:", self.AnNumberOfSeats)
        print("Old Trafford Number Of Seats:", self.OtNumberOfSeats)


Uk = HybridStadium()
Uk.setSeats("Must be under the Government recommended limit.")
Uk.setAnNumberOfSeats("90000")
Uk.setOtNumberOfSeats("100000")
Uk.printDetails()

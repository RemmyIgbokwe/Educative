class Laces():  
    def setLength(self, Length):
        self.Length = Length


class Studs():  
    def setNumberOfStuds(self, NumberOfStuds):
        self.NumberOfStuds = NumberOfStuds

# Child class inherited from CombustionEngine and ElectricEngine
class HybridFeatures(Laces, Studs):
    def printDetails(self):
        print("Length:", self.Length)
        print("Number Of Studs:", self.NumberOfStuds)

car = HybridFeatures()
car.setLength("16 cm")
car.setNumberOfStuds("9")
car.printDetails()

# class CombustionEngine():  
#     def setTankCapacity(self, tankCapacity):
#         self.tankCapacity = tankCapacity


# class ElectricEngine():  
#     def setChargeCapacity(self, chargeCapacity):
#         self.chargeCapacity = chargeCapacity

# # Child class inherited from CombustionEngine and ElectricEngine
# class HybridEngine(CombustionEngine, ElectricEngine):
#     def printDetails(self):
#         print("Tank Capacity:", self.tankCapacity)
#         print("Charge Capacity:", self.chargeCapacity)

# car = HybridEngine()
# car.setChargeCapacity("250 W")
# car.setTankCapacity("20 Litres")
# car.printDetails()
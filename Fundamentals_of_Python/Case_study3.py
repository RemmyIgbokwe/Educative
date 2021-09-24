class Furniture:  # parent class
    def setPrice(self, price):  # defining the set
        self.setPrice = price
        print("Price is set to", self.setPrice)


class Sofa(Furniture):  # child class of Furniture
    pass


class Chair(Furniture):  # child class of Furniture
    pass


MaxPayne = Sofa()  # creating an object of the Car class
MaxPayne.setPrice(220000)  # accessing methods from the parent class

Elas = Chair()  # creating an object of the Truck class
Elas.setPrice(180000)  # accessing methods from the parent class

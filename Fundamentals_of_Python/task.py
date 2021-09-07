class restaurant:
    


    def __init__(self, order, fees):
        self.order = order
        self.fees = fees


    def OrderMade(self):
        print("2 order of ", self.order)



    def OrderAmount(self):
        
        return self.fees * 2
        
        

obj1 = restaurant("Bacon", 3000) 
obj1.OrderAmount() 
obj1.OrderMade()   
print("is worth ", obj1.OrderAmount())
                
        #pass
class Sport:  # parent class
    def setViewers(self, views):  # defining the set
        self.topViews = views
        print("The number of viewers is set to", self.topViews)


class Football(Sport):  # child class
    def governingBody(self):
        print("Under the control of FIFA. ")



Arsenal = Football()  # creating an object of the Car class
Arsenal.setViewers(1000000)  # accessing methods from the parent class
Arsenal.governingBody()  # accessing method from its own class

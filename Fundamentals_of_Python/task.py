class Player:
    teamName = 'Liverpool'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables

    @classmethod
    def getTeamName(cls):
        return cls.teamName

    @classmethod
    def setTeamName(cls, newTeamName):
        cls.teamName = newTeamName


obj1 = Player("Remmy")
print(obj1.getTeamName())
obj1.setTeamName("Chelsea")
print(obj1.getTeamName())


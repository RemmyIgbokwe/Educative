class Television:
    def __init__(self):
        self.powerOn = False
        self.activity = {1: "Record", 2: "Reminder", 3:"Subscribe", 4: "Catch Up"}
        self.mode = None
        self.volume = 67

    def getPower(self):
        return "Power is On" if self.powerOn else "Power is Off"

    def setPower(self, changePower):
        self.powerOn = changePower 

    def getLoudness(self):
        return self.volume

    def setLoudness(self, newVolume):
        self.volume = newVolume      

    def getMode(self):
        return "The mode is current None. please insert mode{}: ". format(self.activity) if self.mode is None else self.mode 

    def setMode(self, newMode):
        self.mode = self.activity[newMode]





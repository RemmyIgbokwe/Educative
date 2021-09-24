#---------------#
#from os import O_NOFOLLOW


# -Create an AC class
# -Functionalities:
#          -on/Off 
#          -get/set temperature *
#          -on/off swinger *
#          -set mode (cool, dry, fan speed and air swing)


class AirConditioner:
    def __init__(self):
        self.powerOn = False 
        self.temperature = 21
        self.swingSwitch = {0: "off", 1: "on"}
        self.swingMode = None
        self.modeStates = {1: "cool", 2: "dry", 3: "fan speed", 4: "air swing"}
        self.mode = None

    def getPower(self):
        # if self.powerOn:
        #     return "AC is On"
        # else: 
        #     return "AC is Off"
        return "AC  is On" if self.powerOn else "AC is off"

    def setPower(self, changePower):
        self.powerOn = changePower

    def getTemp( self):
        # for i in range(16, 31):
        #     if self.temperature != i:
        #         return input ("Error! Please set a temperature between between and including 16-30: ")
        #     else:
        #         return self.temperature    
        if self.temperature <= 30 and self.temperature >=16:
            return self.temperature
        else:
            # for i in range(15, 30):
            #     if self.temperature != i:
            return "Please set a temperature between between and including 16-30: "
                
                

        #return self.temperature 

    def setTemp(self, newTemp):
        self.temperature = newTemp

    def getSwing(self):
        if self.swingMode is None:
            return "The mode is currently None. Please select a mode{}: ". format(self.swingSwitch)
        else:
            return self.swingMode   
        #return "Swing is on" if self.swingOn else "Swing os Off " #ternary 

    def setSwing(self, changeSwing):
        self.swingMode = self.swingSwitch[changeSwing]

    def getMode (self):
        # if self.mode is None:
        #     return "The mode is currently None. Please select a mode{}: ". format(self.modeStates)
        # else:
        #     return self.mode
        return "The mode is currently None. Please select a mode{}: ". format(self.modeStates) if self.mode is None else self.mode

    def setMode(self, newMode):
        self.mode = self.modeStates[newMode]       


ac = AirConditioner()
#print(ac.getTemp()) 
ac.setTemp(14)
print(ac.getTemp())    
#print(ac.getSwing())
# ac.setSwing(1)
# print(ac.getSwing())                                   
        

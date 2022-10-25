'''
Name: Roger Poduska
email: poduskrd@mail.uc.edu
Assignment: Thorin_Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: Roger's class to add to Thorin project; Models a car in real world
Citations: N/a
Anything else that's relevant: N/a
'''

class Car():

    def __init__(self, carID, color, milage):
        self.carID = carID
        self.color = color
        self.milage = milage
        self.isRunning = False
    
    def __str__(self):
        return "The car color is " + self.color + " and the milage is " + str(self.milage) + ". Is the car on? " + self.isRunning
    
    def __repr__(self):
        return "carID = " + str(self.carID)
    
    #Returns the color of the car
    def getCarColor(self):
        return self.color
    
    #Returns the milage on the car
    def getMilage(self):
        return self.milage
    
    #Returns status of the engine
    def getisRunning(self):
        return self.isRunning
    
    #Sets the color of the car
    def setCarColor(self, newColor):
        self.color = newColor
        return "The color has been changed."
    
    #Sets the milage on the car
    def setMilage(self, newMilage):
        self.milage = newMilage
        return "The milage has been changed."
    
    #Sets the engine status on the car
    def setisRunning(self, status):
        self.isRunning = status
        return "The car status has been changed."
    
    #Starts car using remote start feature
    def remoteStart(self):
        self.running = True
        return "The car has been started using the remote start feature. Let's ride."
    

'''
Name: David Patton
email: pattondk@mail.uc.edu
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: I created a class for our group project to model a train 
transportation scenario 
Citations: David Patton
Anything else that's relevant: This is the module holding the train class.
'''
from _operator import truediv
class Train(): 
    def __init__(self, NumTrainCars, GuestCapacity):
        self.NumTrainCars = NumTrainCars
        self.validateGuestCapacity(GuestCapacity)
        self.BlowWhistle = False 
    
    def __repr__(self):
        return "There are " + self.NumTrainCars
    
    def __str__(self):
        return ("The number of cars in the train is " + str(self.NumTrainCars) + " And the number of people on the train is " 
                + str(self.GuestCapacity))
       
    def getGuestCapacity(self):
        return self.GuestCapacity
    
    def getNumTrainCars(self):
        return self.NumTrainCars
    
    def getBlowWhistle(self):
        return self.BlowWhistle
        
    def setGuestCapacity(self, GuestCapacity):
        self.validateGuestCapacity(GuestCapacity)
     
    def validateGuestCapacity(self, GuestCapacity):
        if GuestCapacity > 300:
            print ("You are over capacity only 300 passengers can ride the train!")
        else:
            self.GuestCapacity = GuestCapacity 
    
    def setNumTrainCars (self, NumTrainCars):
        if NumTrainCars >= 15:
            print("The train has too many cars!")
        else:
            self.NumTrainCars = NumTrainCars
    
    def setBlowWhistle(self, status):
        self.BlowWhistle = status
        return "The train horn status has changed."
    
    def WhistleOn(self): 
        self.BlowWhistle = True 
        return("The whistle is blowing toot toot please move")

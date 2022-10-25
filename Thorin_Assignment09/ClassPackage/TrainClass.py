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
    def __init__(self, NumTrainCars, GuestCapacity, BlowWhistle):
        self.NumTrainCars = NumTrainCars
        self.BlowWhistle = BlowWhistle
        self.validateGuestCapacity(GuestCapacity)
       
    def getGuestCapacity(self):
        return self.GuestCapacity
        
    def setGuestCapacity(self, GuestCapacity):
        self.validateGuestCapacity(GuestCapacity)
     
    def validateGuestCapacity(self, GuestCapacity):
        if GuestCapacity > 300:
            print ("You are over capacity only 300 passengers can ride the train!")
        else:
            self.GuestCapacity = GuestCapacity 
    
    def setNumTrainCars (self, NumTrainCars):
        if NumTrainCars >= 15:
            print("The train has to many cars!")
        else:
            self.NumTrainCars = NumTrainCars
    
    def getNumTrainCars(self):
        return self.NumTrainCars
    
    def BlowWhistle(self): 
        self.BlowWhistle == True 
        print("The whistle is blowing")
        
        self.BlowWhistle == False
        print("You blew the whistle!")
       
    def __repr__(self):
        return "There are  " + self.NumTrainCars
    
    def __str__(self):
        return ("Wedding Date is = " + str(self.NumTrainCars) + " And the number of people attending is " 
                + str(self.GuestCapacity))
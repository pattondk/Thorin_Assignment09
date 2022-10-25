'''
Name: Mia Nguyen
email: nguye2m6@mail.uc.edu
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: I created a main module for the group project assignment 9
Citations: 
Anything else that's relevant: This is the module holding the main
'''
from ClassPackage.TrainClass import Train
train1 = Train(20,150,True)
#train1.BlowWhistle()
print(train1.__str__())
numGuest = train1.GuestCapacity
print(train1.validateGuestCapacity(numGuest))
train1.setNumTrainCars(25)

from ClassPackage.CarClass import Car
car1 = Car('C1','white',5400)
print(car1.__str__())
print(car1.setMilage(6000))
print(car1.setisRunning(True))
print(car1.remoteStart())
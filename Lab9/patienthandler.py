'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 04/25/2023
Lab: lab9
Last modified: 04/26/2023
Purpose: Contains a PatientHandler class. Organizes information in the input file.
'''

#patienthandler.py

#creates a patient handler class
class PatientHandler:

    #initializes first name, last name, age, illness, and severity
    def __init__(self, first_name, last_name, age, illness, severity):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.illness = illness
        self.severity = severity 

    #less than magic method
    def __lt__(self,other):
        return self.severity < other.severity

    #less than equal to magic method
    def __le__(self,other):
        return self.severity <= other.severity

    #greater than magic method
    def __gt__(self,other):
        return self.severity > other.severity 
    
    #greater than equal to magic method
    def __ge__(self,other):
        return self.severity >= other.severity
    
    #equal to magic method
    def __eq__(self,other):
        return self.severity == other.severity
    
    #string output magic method
    def __str__(self):
        return f"     Name: {self.last_name}, {self.first_name}. \n     Age: {self.age} \n     Suffers from: {self.illness} \n     Illness severity: {self.severity}"
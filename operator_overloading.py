# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 19:15:50 2024

@author: aasim
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May  3 00:37:21 2024

@author: aasim
"""

class Time:
    def __init__(self, hour, minutes):
        self.hour = hour
        self.minutes = minutes
    
    def __add__(self, other):
        total_minutes = self.minutes + other.minutes
        carry_hour = total_minutes // 60
        new_hour = self.hour + other.hour + carry_hour
        new_minutes = total_minutes % 60
        return Time(new_hour, new_minutes)
    
    def dis(self):
        print(self.hour,self.minutes)

# Creating instances of Time class
time1 = Time(4, 30)
time2 = Time(2, 45)

# Adding two time objects using overloaded +
total_time = time1 + time2

# Displaying the result
print("Total time:")

total_time.dis()
# 25) Write a python program to display factors of a number.# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 08:32:23 2024

@author: aasim
"""

num= int (input("number:"))

for i in range (1,num+1):
    if num%i == 0:
        print(i)

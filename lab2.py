#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 14:39:14 2022

@author: sjcet
"""

n=int(input("Enter the number whose reverse is to be found \n"))

s=int(0)

while n!=0:
    
         mod=n%10
         n//=10
         s=s*10+mod
         
print(s)

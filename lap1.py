#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 15:25:08 2022

@author: sjcet
"""

import numpy as np
# X IS A 3*3 MATRIX
x=np.array([[1,2,3],[4,2,6],[1,0,1]])
print("x =\n " , x,"\n")

#Y IS A 3*3 MATRIX
y=np.array([[1,5,2],[1,6,3],[0,2,4]])
print("y= \n", y,"\n")

#1. PERFORM OPERATIONS ON THE MATRIX
o=7*x + np.linalg.matrix_power(y,3)
print("7x+y^3 = \n", o,"\n")

#2. PERFORM MATRIX MULTIPLICATION
m=np.multiply(x,y)
print("x * y = \n " , m,"\n")

#RANK OF MATRIX X
rankx=np.linalg.matrix_rank(y)
print("Rank of matrix x= " , rankx)

#RANK OF MATRIX Y
ranky= np.linalg.matrix_rank(y)
print("Rank of Matrix y=" , ranky,"\n")

#PRINT DIAGONAL ELEMENTS 
digx =np.linalg.det(x)
print("Diagonal elements \n" ,digx , "\n")

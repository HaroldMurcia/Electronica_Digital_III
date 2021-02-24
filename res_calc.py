#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 17:45:17 2021

@author: hmurcia
"""

import numpy as np

R =[1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1]
R= np.array(R)
R_array = np.hstack([R,1e1*R, 1e2*R, 1e3*R, 1e4*R, 1e5*R, 1e6*R, 1e7*R])

def r2arreglo(ideal):
    R1=1
    R2=1
    R3=1
    error_min=1e3
    N = len(R_array)
    for k in range(0,N):
        R1=R_array[k]
        for i in range(0,N):
            R2=R_array[i]
            for j in range(0,N):
                R3=R_array[j]
                R=1/(1/R1+1/R2+1/R3) 
                error = abs(ideal-R)
                if error<error_min or error==0:
                    R1_out=R1
                    R2_out=R2
                    R3_out=R3
                    error_min=error
                    if error==0:
                        print(R1_out, R2_out, R3_out, error_min)
    return R1_out, R2_out, R3_out

if __name__ == "__main__":
    G=5/0.8
    Rg=50e3/(G-1)
    res_1,res_2,res_3 = r2arreglo(Rg)
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 16:54:53 2020

@author: mamer
"""

def checkNulls(myDF):
    return myDF.isnull().sum()[myDF.isnull().sum() > 0]
     
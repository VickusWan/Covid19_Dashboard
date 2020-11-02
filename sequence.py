#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 11:35:44 2020

@author: victoruong
"""

import c3aidatalake
import pandas as pd

def get_data(location):
    
    try:
        location[1]
        cases = "{province}_{country}.JHU_ConfirmedCases.data".format(province=location[0], country=location[1])
        deaths = "{province}_{country}.JHU_ConfirmedDeaths.data".format(province=location[0], country=location[1])    
        info = df2[['dates', cases, deaths]]
    except:
        cases = "{country}.JHU_ConfirmedCases.data".format(country=location[0])
        deaths = "{country}.JHU_ConfirmedDeaths.data".format(country=location[0])    
        info = df[['dates', cases, deaths]]
        
    return info

df = pd.read_csv(r"C:\Users\Victor\.spyder-py3\country_covid.csv")
df2 = pd.read_csv(r"C:\Users\Victor\.spyder-py3\province_covid.csv")





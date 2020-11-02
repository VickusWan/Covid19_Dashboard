# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 01:19:46 2020

@author: Victor
"""

import c3aidatalake
import pandas as pd

def get_count(location):
    df2 = c3aidatalake.evalmetrics(
    "outbreaklocation",
        {
          "spec": {
            "ids": location,
            "expressions":["JHU_ConfirmedCases","JHU_ConfirmedDeaths"],
            "interval":"DAY",
            "start":"2020-01-01",
            "end":"2020-10-31"
          }
    }, get_all=True
    )
    
    return df2

def remove_missing(df):
    
    for (colname, colvalues) in df.iteritems():
        if 'missing' in colname:
            df = df.drop([colname], axis=1)
    
    return df

csv = pd.read_csv(r"C:\Users\Victor\.spyder-py3\outbreaklocation.csv")
dummy1 = csv['Country id'].tolist()
dummy2 = csv['Province or State id'].tolist()

country = []
for i in dummy1:
    if type(i) != float:
        country.append(i)
    else:
        break

country_covid = get_count(country)
country_covid = remove_missing(country_covid)

province = []
for i in dummy2:
    if type(i) != float:
        province.append(i)
    else:
        break

province_covid = get_count(province)
province_covid = remove_missing(province_covid)

#country_covid.to_csv(r"C:\Users\Victor\.spyder-py3\country_covid.csv")
#province_covid.to_csv(r"C:\Users\Victor\.spyder-py3\province_covid.csv")

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt

province_cases = pd.read_csv("JHU_COVID19_data/time_series_covid19_confirmed_global.csv").drop(['Lat', 'Long'], axis=1)
province_deaths = pd.read_csv("JHU_COVID19_data/time_series_covid19_deaths_global.csv").drop(['Lat', 'Long'], axis=1)
province_recovered = pd.read_csv("JHU_COVID19_data/time_series_covid19_recovered_global.csv").drop(['Lat', 'Long'], axis=1)

country_case = province_cases.groupby(['Country/Region']).sum()

country_deaths = province_deaths.groupby(['Country/Region']).sum()

country_recovered = province_recovered.groupby(['Country/Region']).sum()

US_cases = pd.read_csv("JHU_COVID19_data/time_series_covid19_confirmed_US.csv").drop(['UID', 'iso2', 'iso3', 'code3', 'FIPS', 'Lat', 'Long_'], axis=1)
US_deaths = pd.read_csv("JHU_COVID19_data/time_series_covid19_deaths_US.csv").drop(['UID', 'iso2', 'iso3', 'code3', 'FIPS', 'Lat', 'Long_'], axis=1)

inputs = "Canada" 

case = country_case.loc[inputs]
deaths = country_deaths.loc[inputs]

fig, axes = plt.subplots(nrows=2, ncols=2)

case.plot(ax=axes[0,0], color='green')
deaths.plot(ax=axes[0,1], color='red')
case.plot(ax=axes[1,0], logy=True, color='green')
deaths.plot(ax=axes[1,1], logy = True, color='red')
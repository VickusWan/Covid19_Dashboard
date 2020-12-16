# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 00:27:43 2020

@author: Victor
"""

from tkinter import *
import data_extract as de
import matplotlib.pyplot as plt

root = Tk()
root.title('COVID19 - Dashboard')
root.geometry("400x400")

country_cases, country_deaths = de.get_covid_data()
total_cases, total_deaths, total_recovered = de.get_totals()
total_cases = "{:,}".format(total_cases)
total_deaths = "{:,}".format(total_deaths)
total_recovered = "{:,}".format(total_recovered)

def graph():
    
    inputs = clicked.get()
    
    cases = country_cases.loc[inputs]
    deaths = country_deaths.loc[inputs]
    
    fig, axes = plt.subplots(nrows=2, ncols=2)
    fig.suptitle('{country} COVID Cases'.format(country=inputs))
    axes[0,0].set_title('Confirmed Cases')
    axes[0,1].set_title('Confirmed Deaths')
    axes[1,0].set_title('Confirmed Cases LOG SCALE')
    axes[1,1].set_title('Confirmed Deaths LOG SCALE')
    
    cases.plot(ax=axes[0,0], color='green')
    deaths.plot(ax=axes[0,1], color='red')
    cases.plot(ax=axes[1,0], logy=True, color='green')
    deaths.plot(ax=axes[1,1], logy = True, color='red')
    
    return


label1 = Label(root, text='Global Corona Virus Total Cases')
label1.pack()
label2 = Label(root, text=str(total_cases))
label2.pack()
label3 = Label(root, text='Global Corona Virus Total Deaths')
label3.pack()
label4 = Label(root, text=str(total_deaths))
label4.pack()
label5 = Label(root, text='Global Corona Virus Recoveries')
label5.pack()
label6 = Label(root, text=str(total_recovered))
label6.pack()

clicked = StringVar()
clicked.set("Select a country")
country_list = de.get_countries()
drop = OptionMenu(root, clicked, *country_list)
drop.pack()


# =============================================================================
# e = Entry(root)
# e.pack()
# =============================================================================

button = Button(root, text="Graph", command=graph)
button.pack()

root.mainloop()
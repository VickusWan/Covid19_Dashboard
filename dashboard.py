# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 00:27:43 2020

@author: Victor
"""

from tkinter import *
import data_extract as de

root = Tk()
root.title('COVID19 - Dashboard')
root.geometry("400x400")

clicked = StringVar()
clicked.set("Select a country")
country_list = de.show_country()
drop = OptionMenu(root, clicked, *country_list)
drop.pack()

root.mainloop()
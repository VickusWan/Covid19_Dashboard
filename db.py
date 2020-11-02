# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 19:39:37 2020

@author: Victor
"""

from sqlalchemy import create_engine
import pymysql
import mysql.connector
import sequence as sq
import pandas as pd
import itertools


engine = create_engine('mysql://root:9988@localhost/test')
dbconnect = engine.connect()

df = pd.read_csv(r"C:\Users\Victor\.spyder-py3\province_covid.csv")

province = []
for (colname, colvalues) in df.iteritems():
    province.append(colname.split('_'))
    
province.pop(0)
province.pop(0)
dummy = []

for loc in province:
    country = loc[1].split('.')
    country = country[0]
    dummy.append([loc[0], country])

dummy = list(dummy for dummy,_ in itertools.groupby(dummy))

for i in dummy:

    df = sq.get_data([i[0], i[1]])

    try:
        frame = df.to_sql(i[0], dbconnect, if_exists='fail');
    
    except ValueError as vx:
        print(vx)
    
    except Exception as ex:   
        print(ex)
    

dbconnect.close()




# =============================================================================
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="9988",
#   database="test"
# )
# =============================================================================

#myc = mydb.cursor()
# USE LINE BELOW TO CREATE A DATABASE
#myc.execute("CREATE DATABASE COVID19")

# Initialize the table with the headers index values
# =============================================================================
# try:
#     myc.execute("CREATE TABLE Alberta (ID int PRIMARY KEY AUTO_INCREMENT, Date DATE, Confirmed_Cases int, Confirmed_deaths int)")
# except:
#     print('database exists')
# =============================================================================

#Describes the table - what are the index values
# =============================================================================
# myc.execute("DESCRIBE Person")
# 
# for x in myc:
#     print(x)
# =============================================================================





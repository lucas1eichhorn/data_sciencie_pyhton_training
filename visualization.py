#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 22:50:34 2021

@author: lucas
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Year = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
Temp_I = [0.72,0.61,0.65,0.68,0.75,0.90,1.02,0.93,0.85,0.99,1.02]
plt.plot(Year,Temp_I)
plt.xlabel('Year')
plt.ylabel('Temp')
plt.title('Gloabl Warming',{'fontsize':12,'horizontalalignment':'left'})
plt.show()


"""
Visualization 2

"""

Month= ['Jan','Feb','MArch','April','May','June','July','Aug','Sep','Oct','Nov','Dec']
Cust1 = [12,13,9,8,7,8,8,7,6,5,8,10]
Cust2 = [14,16,11,7,6,6,7,6,5,8,9,12]

plt.plot(Month,Cust1,color='red',label='Customer 1',marker='o')
plt.plot(Month,Cust2,color='blue',label='Customer 2',marker='^')
plt.xlabel('Months')
plt.ylabel('Electicity Consumption')
plt.title("Building Consumption",{'fontsize':18,'horizontalalignment':'left'})
plt.legend(loc='lower left')
plt.show()

#subplots : multiple plots (rows, colums, number of graph)
plt.subplot(1,2,1)
plt.plot(Month,Cust1,color='red',label='Customer 1',marker='o')
plt.xlabel('Months')
plt.ylabel('Electicity Consumption')
plt.title("Building Consumption of Cust1",{'fontsize':10,'horizontalalignment':'center'})



plt.subplot(1,2,2)
plt.plot(Month,Cust2,color='blue',label='Customer 2',marker='^')
plt.xlabel('Months')
plt.title("Building Consumption of Cust2",{'fontsize':10,'horizontalalignment':'center'})

#scatter dispersion - punteado y en grilla
plt.scatter(Month,Cust1,color='red',label='Customer 1')
plt.scatter(Month,Cust2,color='blue',label='Customer 2')
plt.xlabel('Month')
plt.ylabel("electicity consumption")
plt.title("Scatter plot")
plt.grid()
plt.legend(loc='best')
plt.show()

#histograma - muestra distibucion de valores
plt.hist(Cust1,bins=10,color='green')
plt.xlabel("Months")
plt.ylabel("Elec Consumption")
plt.title("Histogram")
plt.show()
#diagrama de barra - muestra valores
plt.bar(Month,Cust1,width=0.9,color='blue')
plt.show()


#Barra - multiple 
plt.bar(Month,Cust1,color='red',label='Customer 1')
plt.bar(Month,Cust2,color='blue',label='Customer 2')
plt.xlabel('Month')
plt.ylabel("Electicity consumption")
plt.title("Bar chart plot")
plt.grid()
plt.legend(loc='best')
plt.show()

bar_width= 0.4
Month_b = np.arange(12)

plt.bar(Month_b,Cust1,bar_width,color='green', label="Customer 1")
plt.bar(Month_b+bar_width,Cust2,bar_width,color='pink',label="Customer 2")

plt.xlabel('Month')
plt.ylabel("Electicity consumption")
plt.legend(loc='best')


plt.xticks(Month_b+(bar_width)/12,('Jan','Feb','MArch','April','May','June','July','Aug','Sep','Oct','Nov','Dec'))
plt.show()

plt.boxplot(Cust1, notch=True,vert = True)
plt.boxplot([Cust1,Cust2],patch_artist=True,
            boxprops = dict(facecolor='red',color='blue'),
            whiskerprops=dict(color='green'),
            capprops=dict(color='pink'),
            medianprops=dict(color='yellow'))
plt.show()



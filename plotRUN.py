# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 09:13:56 2018

@author: chris_000
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

currDF = pd.read_csv('2018-05-31_16-00-39.csv')
print(currDF)

upDF = currDF[:-900]
print(upDF)

readTime = upDF.iloc[:,2]
print(readTime)

BlankVolts = [9.26304, 9.50600, 10.960, 10.8131, 10.1751, 11.1569, 10.4123, 10.18626]
logBlankVolts = np.log10(BlankVolts)

morbido1 = upDF.iloc[:,3].tolist()
morbido2 = upDF.iloc[:,4].tolist()
morbido3 = upDF.iloc[:,5].tolist()
morbido4 = upDF.iloc[:,6].tolist()
morbido5 = upDF.iloc[:,7].tolist()
morbido6 = upDF.iloc[:,8].tolist()
morbido7 = upDF.iloc[:,9].tolist()
morbido8 = upDF.iloc[:,10].tolist()

OD1 = (((np.log10(morbido1)/logBlankVolts[0]) - .71891) / -2.1235).tolist()
OD2 = (((np.log10(morbido2)/logBlankVolts[1]) - .71891) / -2.1235).tolist()
OD3 = (((np.log10(morbido3)/logBlankVolts[2]) - .71891) / -2.1235).tolist()
OD4 = (((np.log10(morbido4)/logBlankVolts[3]) - .71891) / -2.1235).tolist()
OD5 = (((np.log10(morbido5)/logBlankVolts[4]) - .71891) / -2.1235).tolist()
OD6 = (((np.log10(morbido6)/logBlankVolts[5]) - .71891) / -2.1235).tolist()
OD7 = (((np.log10(morbido7)/logBlankVolts[6]) - .71891) / -2.1235).tolist()
OD8 = (((np.log10(morbido8)/logBlankVolts[7]) - .71891) / -2.1235).tolist()

fig = plt.figure(num=None, figsize=(20,15), dpi=100, facecolor='w', edgecolor='k')
#figure(num=None, figsize=(5,5), dpi=80, facecolor='w', edgecolor='k')
ax1 = fig.add_subplot(111)
#ax1.set_xticks(np.arange(0, 600, 100))
#ax1.set_yticks(np.arange(0, 10., 0.5))
ax1.scatter(readTime, morbido1, s=10, c='b', marker="s", label='Culture#1')
ax1.scatter(readTime, morbido2, s=10, c='g', marker="o", label='Culture#2')
ax1.scatter(readTime, morbido3, s=10, c='r', marker="^", label='Culture#3')
ax1.scatter(readTime, morbido4, s=10, c='c', marker="p", label='Culture#4')
ax1.scatter(readTime, morbido5, s=10, c='m', marker="D", label='Culture#5')
ax1.scatter(readTime, morbido6, s=10, c='y', marker="v", label='Culture#6')
ax1.scatter(readTime, morbido7, s=10, c='k', marker="h", label='Culture#7')
ax1.scatter(readTime, morbido8, s=10, c='violet', marker="8", label='Culture#8')
plt.ylabel('Voltage')
plt.xlabel('Time (min)')
plt.title('25hr. Turbidostat run (OD=.6) VOLTS')
plt.grid()
plt.legend(loc='upper right')
plt.show()


fig = plt.figure(num=None, figsize=(20,15), dpi=100, facecolor='w', edgecolor='k')
ax1 = fig.add_subplot(111)
ax1.scatter(readTime, OD1, s=10, c='b', marker="s", label='Culture#1')
ax1.scatter(readTime, OD2, s=10, c='g', marker="o", label='Culture#2')
ax1.scatter(readTime, OD3, s=10, c='r', marker="^", label='Culture#3')
ax1.scatter(readTime, OD4, s=10, c='c', marker="p", label='Culture#4')
ax1.scatter(readTime, OD5, s=10, c='m', marker="D", label='Culture#5')
ax1.scatter(readTime, OD6, s=10, c='y', marker="v", label='Culture#6')
ax1.scatter(readTime, OD7, s=10, c='k', marker="h", label='Culture#7')
ax1.scatter(readTime, OD8, s=10, c='violet', marker="8", label='Culture#8')
plt.ylabel('OD600')
plt.xlabel('Time (min)')
plt.title('25hr. Turbidostat run (OD=.6) OD')
plt.grid()
plt.legend(loc='lower right')
plt.show()
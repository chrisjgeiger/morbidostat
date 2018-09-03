# -*- coding: utf-8 -*-
"""
Created on Thu May 31 13:13:50 2018

@author: chris_000
"""

# -*- coding: utf-8 -*-

import time
import piplates.DAQC2plate as DAQC2
import matplotlib.pyplot as plt
from datetime import datetime
import sys
import csv
import pandas as pd
import numpy as np

###########################################################################################################################################
###########################################################################################################################################
###########################################################################################################################################
#functions


#takes OD for morbidostat connected to the given channel and stores values
def readOD(): 
    DAQC2.setDOUTbit(0,7)
    time.sleep(1)
    rowVolts = []
    j = 0
    k = 0
    num = 1
    while(k <= 5):
        tempVolt = []
        tEnd = time.time() + .5
        while(time.time() < tEnd):
            tempVolt.append(DAQC2.getADC(j,k))
        currAvgVolt = sum(tempVolt) / len(tempVolt)
        rowVolts.append(currAvgVolt)
        print("Avg voltage for ", num, ": ", currAvgVolt)
        k = k+1
        num = num + 1
        if(k == 6 and j == 0): 
            j = 1
            k = 0
        elif(k ==2 and j==1): 
            k = 10
    DAQC2.clrDOUTbit(0,7)

#plots the stored values 
def plotOD(): 
    readTime = globalDF[:,1]
    morbido1 = globalDF[:,2]
    morbido2 = globalDF[:,3]
    morbido3 = globalDF[:,4]
    morbido4 = globalDF[:,5]
    morbido5 = globalDF[:,6]
    morbido6 = globalDF[:,7]
    morbido7 = globalDF[:,8]
    morbido8 = globalDF[:,9]
    
    #for plot data function
    OD1 = globalDF[:,10]
    OD2 = globalDF[:,11]
    OD3 = globalDF[:,12]
    OD4 = globalDF[:,13]
    OD5 = globalDF[:,14]
    OD6 = globalDF[:,15]
    OD7 = globalDF[:,16]
    OD8 = globalDF[:,17]    


    fig = plt.figure()
    ax1 = fig.add_subplot(111)
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
    Volttitle = datetime.now().strftime('%Y-%m-%d_%H-%M') + ' Voltage plot'
    plt.title(Volttitle)
    plt.legend(loc='upper right')
    plt.show()

    fig = plt.figure()
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
    ODtitle = datetime.now().strftime('%Y-%m-%d_%H-%M') + ' OD plot'
    plt.title(ODtitle)
    plt.legend(loc='upper left')
    plt.show()
    

#export data to a csv file 
def exportData():
    csvTitle = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.csv'
    globalDF.to_csv(csvTitle, index = True, header = ['DateTime', 'Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8'])
    print(globalDF)
    print()
    print("new csv file on Desktop: ", csvTitle)
    

#set measured voltages for blank media
def blankVoltages():
    print("Insert voltage for blank media.")
    num = 1
    while(num <= 8):
        print("\n")
        print(num)
        var = input(": ")
        tempVal = float(var)
        blankVolts.append(tempVal)
        tempLog = np.log10(tempVal)
        logBlankVolts.append(tempLog)
        num = num + 1
    print(blankVolts)
    print(logBlankVolts)
        
        
#prime tubes with media before expt.
def sysPrime(): 
    print("priming pumps...")
    #open all valves and turn on both pumps for 10s

    DAQC2.setDOUTbit(0,0)
    DAQC2.setDOUTbit(0,1)
    DAQC2.setDOUTbit(0,2)
    DAQC2.setDOUTbit(0,3)
    DAQC2.setDOUTbit(0,4)
    DAQC2.setDOUTbit(0,5)
    DAQC2.setDOUTbit(1,0)
    DAQC2.setDOUTbit(1,1)
    DAQC2.setDOUTbit(1,2)
    DAQC2.setDOUTbit(1,3)
    DAQC2.setDOUTbit(1,4)
    DAQC2.setDOUTbit(1,5)
    DAQC2.setDOUTbit(0,6)
    DAQC2.setDOUTbit(1,6)
    time.sleep(10)

    #pumps off 
    DAQC2.clrDOUTbit(0,6)
    DAQC2.clrDOUTbit(1,6)


    i = 0
    while(i < 1):
        print("\n")
        print("turn off pump#1: 13")
        print("turn pump#1 on: 14")
        print("turn on pump#2: 15")
        print("turn off pump#2: 16")
        print("close valve: 1-12")
        print("quit: 0")
        var = input(": ")
        currInput = int(var)
        print("current input: ", currInput)
        
        if(currInput == 0):
            print("turning off pump, closing all valves, quitting")
            DAQC2.clrDOUTbit(0,6)
            DAQC2.clrDOUTbit(1,6)
            DAQC2.clrDOUTbit(0,0)
            DAQC2.clrDOUTbit(0,1)
            DAQC2.clrDOUTbit(0,2)
            DAQC2.clrDOUTbit(0,3)
            DAQC2.clrDOUTbit(0,4)
            DAQC2.clrDOUTbit(0,5)
            DAQC2.clrDOUTbit(1,0)
            DAQC2.clrDOUTbit(1,1)
            DAQC2.clrDOUTbit(1,2)
            DAQC2.clrDOUTbit(1,3)
            DAQC2.clrDOUTbit(1,4)
            DAQC2.clrDOUTbit(1,5)
            i = 5
            print("quitting")
            break
    
        if(currInput == 13): 
            print("turning off pump#1")
            DAQC2.clrDOUTbit(0,6)
        
        elif(currInput == 14): 
            print("turning on pump#1")
            DAQC2.setDOUTbit(0,6)
        
        if(currInput == 16): 
            print("turning off pump#6")
            DAQC2.clrDOUTbit(1,6)
        
        elif(currInput == 15): 
            print("turning on pump#6")
            DAQC2.setDOUTbit(1,6)
    
        elif(currInput == 1): 
            print("closing valve #1")
            DAQC2.clrDOUTbit(0,0)
    
        elif(currInput == 2): 
            print("closing valve #2")
            DAQC2.clrDOUTbit(0,1)
   
        elif(currInput == 3): 
            print("closing valve #3")
            DAQC2.clrDOUTbit(0,2)
    
        elif(currInput == 4): 
            print("closing valve #4")
            DAQC2.clrDOUTbit(0,3)
   
        elif(currInput == 5): 
            print("closing valve #5")
            DAQC2.clrDOUTbit(0,4)
    
        elif(currInput == 6): 
            print("closing valve #6")
            DAQC2.clrDOUTbit(0,5)
   
        elif(currInput == 7): 
            print("closing valve #7")
            DAQC2.clrDOUTbit(1,0)
   
        elif(currInput == 8): 
            print("closing valve #8")
            DAQC2.clrDOUTbit(1,1)
   
        elif(currInput == 9): 
            print("closing valve #9")
            DAQC2.clrDOUTbit(1,2)
    
        elif(currInput == 10): 
            print("closing valve #10")
            DAQC2.clrDOUTbit(1,3)
    
        elif(currInput == 11): 
            print("closing valve #11")
            DAQC2.clrDOUTbit(1,4)
        
        elif(currInput == 12): 
            print("closing valve #12")
            DAQC2.clrDOUTbit(1,5)
    
#test individual parts of the morbidostat
def sysTest(): 
    print("testing parts")
    i = 0
    while(i < 1):
        print("\n")
        print("quit: 0")
        print("pumps: 1")
        print("valves:2")
        print("Photodiodes: 3")
        print("lasers: 4")
        var = input(": ")
        currInput = int(var)
        print("current input: ", currInput)
   
        if(currInput == 0):
            print("turning off pump, closing all valves, turning off lasers, quitting")
            DAQC2.clrDOUTbit(0,6)     #turn off pump1
            DAQC2.clrDOUTbit(1,6)     #turn off pump2
            DAQC2.clrDOUTbit(0,0)     #turn off valves
            DAQC2.clrDOUTbit(0,1)
            DAQC2.clrDOUTbit(0,2)
            DAQC2.clrDOUTbit(0,3)
            DAQC2.clrDOUTbit(0,4)
            DAQC2.clrDOUTbit(0,5)
            DAQC2.clrDOUTbit(1,0)
            DAQC2.clrDOUTbit(1,1)
            DAQC2.clrDOUTbit(1,2)
            DAQC2.clrDOUTbit(1,3)
            DAQC2.clrDOUTbit(1,4)
            DAQC2.clrDOUTbit(1,5)
            DAQC2.clrDOUTbit(0,7)   #turn off lasers
            i = 5
            print("quitting")
            break       
    
        elif(currInput == 1): 
            print("pumps")
            j = 0
            while(j < 1): 
                print("\n")
                print("to go back: 0")
                print("turn on pump#1: 1")
                print("turn on pump#2: 2")
                print("turn off pump#1: 3")
                print("turn off pump#2: 4")
                var = input(": ")
                currInput1 = int(var)
                print("current input: ", currInput1)
            
                if(currInput1 == 0): 
                    print("back to main test menu")
                    j = 5
            
                elif(currInput1 == 1): 
                    print("turning on pump#1")
                    DAQC2.setDOUTbit(0,6)

                elif(currInput1 == 2): 
                    print("turning on pump#2")
                    DAQC2.setDOUTbit(1,6)

                elif(currInput1 == 3): 
                    print("turning off pump#1")
                    DAQC2.clrDOUTbit(0,6)
                
                elif(currInput1 == 4): 
                    print("turning off pump#1")
                    DAQC2.clrDOUTbit(1,6)
    
        elif(currInput == 4): 
            print("Lasers")
            j=0
            while(j<1): 
                print("\n")
                print("turn lasers on: 1")
                print("turn lasers off: 2")
                print("go back to test menu: 0")
                var = input(": ")
                currInput2 = int(var)
                print("current input: ", currInput2)        
            
                if(currInput2 == 0): 
                    print("back to main test menu")
                    j = 5   
                
                elif(currInput2 == 1): 
                    print("lasers on")
                    DAQC2.setDOUTbit(0,7)
                
                elif(currInput2 == 2): 
                    print("lasers off")
                    DAQC2.clrDOUTbit(0,7)
    
        elif(currInput == 2): 
            print("Valves")
            j = 0
            while(j < 1): 
                print("\n")
                print("to go back: 0") 
                print("to open individual valves: 1-12")
                print("to close individual valves 21-32")
                print("to open all valves: 13")
                print("to close all valves: 14")
                var = input(": ")
                currInput3 = int(var)
                print("current input: ", currInput3)                    
    
                if(currInput3 == 0): 
                    print("back to main test menu")
                    j = 5   
                
                elif(currInput3 == 13): 
                    print("opening all valves")
                    DAQC2.setDOUTbit(0,0)     #open all valves
                    DAQC2.setDOUTbit(0,1)
                    DAQC2.setDOUTbit(0,2)
                    DAQC2.setDOUTbit(0,3)
                    DAQC2.setDOUTbit(0,4)
                    DAQC2.setDOUTbit(0,5)
                    DAQC2.setDOUTbit(1,0)
                    DAQC2.setDOUTbit(1,1)
                    DAQC2.setDOUTbit(1,2)
                    DAQC2.setDOUTbit(1,3)
                    DAQC2.setDOUTbit(1,4)
                    DAQC2.setDOUTbit(1,5)
            
                elif(currInput3 == 14): 
                    print("closing all valves")
                    DAQC2.clrDOUTbit(0,0)     #close all valves
                    DAQC2.clrDOUTbit(0,1)
                    DAQC2.clrDOUTbit(0,2)
                    DAQC2.clrDOUTbit(0,3)
                    DAQC2.clrDOUTbit(0,4)
                    DAQC2.clrDOUTbit(0,5)
                    DAQC2.clrDOUTbit(1,0)
                    DAQC2.clrDOUTbit(1,1)
                    DAQC2.clrDOUTbit(1,2)
                    DAQC2.clrDOUTbit(1,3)
                    DAQC2.clrDOUTbit(1,4)
                    DAQC2.clrDOUTbit(1,5)
    
                elif(currInput3 == 1): 
                    print("opening valve #1")
                    DAQC2.setDOUTbit(0,0)
    
                elif(currInput3 == 2): 
                    print("opening valve #2")
                    DAQC2.setDOUTbit(0,1)
   
                elif(currInput3 == 3): 
                    print("opening valve #3")
                    DAQC2.setDOUTbit(0,2)
    
                elif(currInput3 == 4): 
                    print("opening valve #4")
                    DAQC2.setDOUTbit(0,3)
   
                elif(currInput3 == 5): 
                    print("opening valve #5")
                    DAQC2.setDOUTbit(0,4)
    
                elif(currInput3 == 6): 
                    print("opening valve #6")
                    DAQC2.setDOUTbit(0,5)
   
                elif(currInput3 == 7): 
                    print("opening valve #7")
                    DAQC2.setDOUTbit(1,0)
   
                elif(currInput3 == 8): 
                    print("opening valve #8")
                    DAQC2.setDOUTbit(1,1)
   
                elif(currInput3 == 9): 
                    print("opening valve #9")
                    DAQC2.setDOUTbit(1,2)
    
                elif(currInput3 == 10): 
                    print("opening valve #10")
                    DAQC2.setDOUTbit(1,3)
    
                elif(currInput3 == 11): 
                    print("opening valve #11")
                    DAQC2.setDOUTbit(1,4)
        
                elif(currInput3 == 12): 
                    print("opening valve #12")
                    DAQC2.setDOUTbit(1,5)
            
                elif(currInput3 == 21): 
                    print("closing valve #1")
                    DAQC2.clrDOUTbit(0,0)
    
                elif(currInput3 == 22): 
                    print("closing valve #2")
                    DAQC2.clrDOUTbit(0,1)
   
                elif(currInput3 == 23): 
                    print("closing valve #3")
                    DAQC2.clrDOUTbit(0,2)
    
                elif(currInput3 == 24): 
                    print("closing valve #4")
                    DAQC2.clrDOUTbit(0,3)
   
                elif(currInput3 == 25): 
                    print("closing valve #5")
                    DAQC2.clrDOUTbit(0,4)
    
                elif(currInput3 == 26): 
                    print("closing valve #6")
                    DAQC2.clrDOUTbit(0,5)
   
                elif(currInput3 == 27): 
                    print("closing valve #7")
                    DAQC2.clrDOUTbit(1,0)
   
                elif(currInput3 == 28): 
                    print("closing valve #8")
                    DAQC2.clrDOUTbit(1,1)
   
                elif(currInput3 == 29): 
                    print("closing valve #9")
                    DAQC2.clrDOUTbit(1,2)
    
                elif(currInput3 == 30): 
                    print("closing valve #10")
                    DAQC2.clrDOUTbit(1,3)
    
                elif(currInput3 == 31): 
                    print("closing valve #11")
                    DAQC2.clrDOUTbit(1,4)
        
                elif(currInput3 == 32): 
                    print("closing valve #12")
                    DAQC2.clrDOUTbit(1,5)  
    
        elif(currInput == 3): 
            print("Photodiodes")
            j = 0
            while(j < 1): 
                print("\n")
                print("to go back: 0") 
                print("to take a reading from a single morbidostat: 1-12")
                print("to take a reading from all morbidostats: 13")
                var = input(": ")
                currInput4 = int(var)
                print("current input: ", currInput4)                    
    
                if(currInput4 == 0): 
                    print("back to main test menu")
                    j = 5   
                
                elif(currInput4 == 13): 
                    print("reading from all morbidostats")
                    plate1 = DAQC2.getADCall(0)
                    plate2 = DAQC2.getADCall(1)
                    j = 0
                    k =0
                    num = 1
                    while(k < 12): 
                        if(k <= 5): 
                            currVolt = plate1[k]
                            print(num, ": ", currVolt)
                            k = k + 1
                            num = num + 1
                        elif(k>5): 
                            a = k - 6
                            currVolt = plate2[a]
                            print(num, ": ", currVolt)
                            k = k + 1
                            num = num + 1
                       
                elif(currInput4 == 1):
                    currVolt = DAQC2.getADC(0,0)
                    print("Morbidostat#1: ", currVolt)
                       
                elif(currInput4 == 2):
                    currVolt = DAQC2.getADC(0,1)
                    print("Morbidostat#2: ", currVolt)
                       
                elif(currInput4 == 3):
                    currVolt = DAQC2.getADC(0,2)
                    print("Morbidostat#3: ", currVolt)
                                             
                elif(currInput4 == 4):
                    currVolt = DAQC2.getADC(0,3)
                    print("Morbidostat#4: ", currVolt)
                                             
                elif(currInput4 == 5):
                    currVolt = DAQC2.getADC(0,4)
                    print("Morbidostat#4: ", currVolt)
                                             
                elif(currInput4 == 6): 
                    currVolt = DAQC2.getADC(0,5)
                    print("Morbidostat#6: ", currVolt)
                                             
                elif(currInput4 == 7):
                    currVolt = DAQC2.getADC(1,0)
                    print("Morbidostat#7: ", currVolt)
                                             
                elif(currInput4 == 8):
                    currVolt = DAQC2.getADC(1,1)
                    print("Morbidostat#8: ", currVolt)
                                             
                elif(currInput4 == 9):
                    currVolt = DAQC2.getADC(1,2)
                    print("Morbidostat#9: ", currVolt)
                                             
                elif(currInput4 == 10):
                    currVolt = DAQC2.getADC(1,3)
                    print("Morbidostat#10: ", currVolt)
                                             
                elif(currInput4 == 11):
                    currVolt = DAQC2.getADC(1,4)
                    print("Morbidostat#11: ", currVolt)
                                             
                elif(currInput4 == 12):
                    currVolt = DAQC2.getADC(1,5)
                    print("Morbidostat#12: ", currVolt)
    
    
    
#test a photodiode
def photoTest():
    elapsedTime = 0
    tMax = 25
    startReadTime = time.time()
    onVolt = []
    offVolt = []
##    tRead = 0
    
    
    while(tMax >= elapsedTime): 
        DAQC2.setDOUTbit(0,7) #turn laser on
        time.sleep(1)
        tempVolt1 = []
        tEnd1 = time.time() + 1
        while(time.time() < tEnd1):
            tempVolt1.append(DAQC2.getADC(0,0))
        DAQC2.clrDOUTbit(0,7)
        anaVolt = sum(tempVolt1)/len(tempVolt1)
        print("number of reads: ", len(tempVolt1))
        print("Voltage('ON'): ", anaVolt)
        onVolt.append(anaVolt)

        tempVolt2 = []
        tEnd2 = time.time() + 1
        while(time.time() < tEnd2):
            tempVolt2.append(DAQC2.getADC(0,0))
        anaVolt = sum(tempVolt2)/len(tempVolt2)
        print("number of reads: ", len(tempVolt2))
        print("Voltage('OFF'): ", anaVolt)
        offVolt.append(anaVolt)
            
        elapsedTime = time.time() - startReadTime
        
    
    print()
    avgON = sum(onVolt) / len(onVolt)
    avgOFF = sum(offVolt) / len(offVolt)
    print("average ON volt: ", avgON)
    print("avgerage OFF volt: ", avgOFF)
    print()


#OD based chemostat run
def Turbido(timeL, pumpPeriod, NormVolt):
    elapsedTime = 0
    tMax = timeL + 45
    min = timeL / 60
    pumpTime = pumpPeriod
    startReadTime = time.time()
    tStart = 0
    tPump = time.time()
    volts = np.zeros(shape=(min+1,8))
    setVolt = NormVolt
    counter = 0
    currTime = time.time()
    print("\n")
    
    currVolts = []
    
    
    while(tMax >= elapsedTime):
        
        if(currTime - tStart > 60):  
            tStart = time.time()
            readTimeS = (currTime - startReadTime) / 60
            print("Read ", counter, " at ", readTimeS, " min.")
            DAQC2.setDOUTbit(0,7)
            time.sleep(1)
            rowVolts = []
            j = 0
            k = 0
            num = 1
            while(k <= 5):
                tempVolt = []
                tEnd = time.time() + .5
                while(time.time() < tEnd):
                    tempVolt.append(DAQC2.getADC(j,k))
                currAvgVolt = sum(tempVolt) / len(tempVolt)
                rowVolts.append(currAvgVolt)
                print("Avg voltage for ", num, ": ", currAvgVolt)
                k = k+1
                num = num + 1
                if(k == 6 and j == 0): 
                    j = 1
                    k = 0
                elif(k ==2 and j==1): 
                    k = 10
            DAQC2.clrDOUTbit(0,7)
            
            currVolts = rowVolts
            volts[counter] = rowVolts

            counter = counter + 1
            measureTime = (tStart - startReadTime) / 60.0 
            measureDateTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            dateTime.append(measureDateTime)
            readTime.append(measureTime)
            print("\n")

        if((currTime - tPump - .05) > pumpTime*60):
            tPump = time.time()
            timePump = (currTime - startReadTime) / 60
            print("pump check at: ", timePump)
            tempLog = 0
            currLogVolts = []
            f = 0
            while(f<8):
                print(f)

                tempLog = np.log10(currVolts[f]) / logBlankVolts[f]
                print(tempLog)
                currLogVolts.append(tempLog)
                f = f+1
            print("CurrLogVolts: ", currLogVolts)
            j = 0
            i = 0
            iter = 0
            currHighVolt = 10
            while(iter<8):
                print("iter: ", iter)
                currHighVolt = currLogVolts[iter]
                if(currHighVolt < setVolt):

                    count=0
                    while(currHighVolt < setVolt):
                        DAQC2.setDOUTbit(j,i)
                        DAQC2.setDOUTbit(0,6)

                        DAQC2.setDOUTbit(0,7)
                        time.sleep(.25)
                        count = count+1
                        avgV = 0
                        currHighVolt = 0
                        tVolt = []
                        tEnd = time.time() + .25
##                        print("tmie read:  ", tEnd)
                        while(time.time() < tEnd):
                            tVolt.append(DAQC2.getADC(j,i))
                        avgV = sum(tVolt) / len(tVolt)
                        print("avg. volt: ", avgV)
                        currHighVolt = np.log10(avgV) / logBlankVolts[iter]
                        print("New currHighVolt: ", currHighVolt)
                        
                        print(count)
                        DAQC2.clrDOUTbit(0,7)
                DAQC2.clrDOUTbit(0,6)
                DAQC2.clrDOUTbit(j,i)
                iter = iter + 1
                i = i + 1
                if(i == 6 and j == 0):
                    j = 1
                    i = 0
                elif(i == 2 and j == 1):
                    i = 10
                        

                    
            print("pump off \n")

        currTime = time.time()
        elapsedTime = time.time() - startReadTime
    
    
    morbido1 = volts[:,0].tolist()
    morbido2 = volts[:,1].tolist()
    morbido3 = volts[:,2].tolist()
    morbido4 = volts[:,3].tolist()
    morbido5 = volts[:,4].tolist()
    morbido6 = volts[:,5].tolist()
    morbido7 = volts[:,6].tolist()
    morbido8 = volts[:,7].tolist()
    
    OD1 = (((np.log10(morbido1)/logBlankVolts[0]) - .71891) / -2.1235).tolist()
    OD2 = (((np.log10(morbido2)/logBlankVolts[1]) - .71891) / -2.1235).tolist()
    OD3 = (((np.log10(morbido3)/logBlankVolts[2]) - .71891) / -2.1235).tolist()
    OD4 = (((np.log10(morbido4)/logBlankVolts[3]) - .71891) / -2.1235).tolist()
    OD5 = (((np.log10(morbido5)/logBlankVolts[4]) - .71891) / -2.1235).tolist()
    OD6 = (((np.log10(morbido6)/logBlankVolts[5]) - .71891) / -2.1235).tolist()
    OD7 = (((np.log10(morbido7)/logBlankVolts[6]) - .71891) / -2.1235).tolist()
    OD8 = (((np.log10(morbido8)/logBlankVolts[7]) - .71891) / -2.1235).tolist()
    
    df = [dateTime, readTime, morbido1, morbido2, morbido3, morbido4, morbido5, morbido6, morbido7, morbido8, OD1, OD2, OD3, OD4, OD5, OD6, OD7, OD8]
    my_df = pd.DataFrame(df)
    my_df = my_df.T
    global globalDF 
    globalDF = my_df    
    csvTitle = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.csv'
    my_df.to_csv(csvTitle, index = True, header = ['DateTime', 'Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'OD1', 'OD2', 'OD3', 'OD4', 'OD5', 'OD6', 'OD7', 'OD8'])
    print(my_df)
    print()
    print("new csv file on Desktop: ", csvTitle)

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
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
    Volttitle = datetime.now().strftime('%Y-%m-%d_%H-%M') + ' Voltage plot'
    plt.title(Volttitle)
    plt.legend(loc='upper right')
    plt.show()

    fig = plt.figure()
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
    ODtitle = datetime.now().strftime('%Y-%m-%d_%H-%M') + ' OD plot'
    plt.title(ODtitle)
    plt.legend(loc='upper left')
    plt.show()
    
    

#take reading every minute for a set time
def contRead(timeL):
    elapsedTime = 0
    tMax = timeL + 11
    min = timeL / 60
    startReadTime = time.time()
    tStart = 0
    volts = np.zeros(shape=(min+1,8))
    counter = 0
    currTime = time.time()
    print("\n")
    
    currVolts = []
    
    
    while(tMax >= elapsedTime):
        
        if(currTime - tStart > 60):  #58 b/c lose two seconds with sleep and measure
            tStart = time.time()
            readTimeS = (currTime - startReadTime) / 60
            print("Read ", counter, " at ", readTimeS, " min.")
            DAQC2.setDOUTbit(0,7)
            time.sleep(1)
            rowVolts = []
            j = 0
            k = 0
            num = 1
            while(k <= 5):
                tempVolt = []
                tEnd = time.time() + .5
                while(time.time() < tEnd):
                    tempVolt.append(DAQC2.getADC(j,k))
                currAvgVolt = sum(tempVolt) / len(tempVolt)
                rowVolts.append(currAvgVolt)
                print("Avg voltage for ", num, ": ", currAvgVolt)
                k = k+1
                num = num + 1
                if(k == 6 and j == 0): 
                    j = 1
                    k = 0
                elif(k ==2 and j==1): 
                    k = 10
            DAQC2.clrDOUTbit(0,7)
            
            currVolts = rowVolts
            volts[counter] = rowVolts

            counter = counter + 1
            measureTime = (tStart - startReadTime) / 60.0 
            measureDateTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            dateTime.append(measureDateTime)
            readTime.append(measureTime)
            print("\n")



        currTime = time.time()
        elapsedTime = time.time() - startReadTime
    
    morbido1 = volts[:,0].tolist()
    morbido2 = volts[:,1].tolist()
    morbido3 = volts[:,2].tolist()
    morbido4 = volts[:,3].tolist()
    morbido5 = volts[:,4].tolist()
    morbido6 = volts[:,5].tolist()
    morbido7 = volts[:,6].tolist()
    morbido8 = volts[:,7].tolist()
    
    OD1 = (((np.log10(morbido1)/logBlankVolts[0]) - .71891) / -2.1235).tolist()
    OD2 = (((np.log10(morbido2)/logBlankVolts[1]) - .71891) / -2.1235).tolist()
    OD3 = (((np.log10(morbido3)/logBlankVolts[2]) - .71891) / -2.1235).tolist()
    OD4 = (((np.log10(morbido4)/logBlankVolts[3]) - .71891) / -2.1235).tolist()
    OD5 = (((np.log10(morbido5)/logBlankVolts[4]) - .71891) / -2.1235).tolist()
    OD6 = (((np.log10(morbido6)/logBlankVolts[5]) - .71891) / -2.1235).tolist()
    OD7 = (((np.log10(morbido7)/logBlankVolts[6]) - .71891) / -2.1235).tolist()
    OD8 = (((np.log10(morbido8)/logBlankVolts[7]) - .71891) / -2.1235).tolist()
    
    df = [dateTime, readTime, morbido1, morbido2, morbido3, morbido4, morbido5, morbido6, morbido7, morbido8, OD1, OD2, OD3, OD4, OD5, OD6, OD7, OD8]
    my_df = pd.DataFrame(df)
    my_df = my_df.T
    global globalDF 
    globalDF = my_df    
    csvTitle = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.csv'
    my_df.to_csv(csvTitle, index = True, header = ['DateTime', 'Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'OD1', 'OD2', 'OD3', 'OD4', 'OD5', 'OD6', 'OD7', 'OD8'])
    print(my_df)
    print()
    print("new csv file on Desktop: ", csvTitle)

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
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
    Volttitle = datetime.now().strftime('%Y-%m-%d_%H-%M') + ' Voltage plot'
    plt.title(Volttitle)
    plt.legend(loc='upper right')
    plt.show()

    fig = plt.figure()
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
    ODtitle = datetime.now().strftime('%Y-%m-%d_%H-%M') + ' OD plot'
    plt.title(ODtitle)
    plt.legend(loc='upper left')
    plt.show()
    

#do a chemostat run, pump on a set time
def chemostat(timeL, pumpPeriod):
    elapsedTime = 0
    tMax = timeL + 11
    min = timeL / 60
    pumpTime = pumpPeriod
    startReadTime = time.time()
    tStart = 0
    tPump = time.time()
    volts = np.zeros(shape=(min+1,8))
    counter = 0
    currTime = time.time()
    print("\n")
    
    
    while(tMax >= elapsedTime): 
        if(currTime - tStart > 60):  #58 b/c lose two seconds with sleep and measure
            tStart = time.time()
            readTimeS = (tStart - startReadTime) / 60
            print("Read ", counter, " at ", readTimeS, " min.")
            ###

            DAQC2.setDOUTbit(0,7)
            time.sleep(1)
            rowVolts = []
            j = 0
            k = 0
            num = 1
            while(k <= 5):
                tempVolt = []
                tEnd = time.time() + .5
                while(time.time() < tEnd):
                    tempVolt.append(DAQC2.getADC(j,k))
                currAvgVolt = sum(tempVolt) / len(tempVolt)
                rowVolts.append(currAvgVolt)
                print("Avg voltage for ", num, ": ", currAvgVolt)
                k = k+1
                num = num + 1
                if(k == 6 and j == 0): 
                    j = 1
                    k = 0
                elif(k ==2 and j==1): 
                    k = 10
            DAQC2.clrDOUTbit(0,7)
            print("\n")
            volts[counter] = rowVolts
            counter = counter + 1
            ###
            measureTime = (tStart - startReadTime) / 60.0 
            measureDateTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
    

          
            dateTime.append(measureDateTime)
            readTime.append(measureTime)

        if((currTime - tPump - 1) > pumpTime*60):
            print("pump on/valves open")
            tPump = (time.time() - startReadTime) / 60
            print("pump on at: ", tPump)
            j = 0
            i = 0
            while(i <= 5): 
                DAQC2.setDOUTbit(j,i)
                DAQC2.setDOUTbit(0,6)
                
                time.sleep(2)
                DAQC2.clrDOUTbit(0,6)
                DAQC2.clrDOUTbit(j,i)
                time.sleep(.5)
                i = i+1
                if(i == 6 and j == 0): 
                    j = 1
                    i = 0
                elif(i==2 and j==1): 
                    i = 10
   

            tPump = time.time()
            print("pump off \n")
            
        
        currTime = time.time()
        elapsedTime = time.time() - startReadTime
    
    morbido1 = volts[:,0].tolist()
    morbido2 = volts[:,1].tolist()
    morbido3 = volts[:,2].tolist()
    morbido4 = volts[:,3].tolist()
    morbido5 = volts[:,4].tolist()
    morbido6 = volts[:,5].tolist()
    morbido7 = volts[:,6].tolist()
    morbido8 = volts[:,7].tolist()
    
    OD1 = (((np.log10(morbido1)/logBlankVolts[0]) - .71891) / -2.1235).tolist()
    OD2 = (((np.log10(morbido2)/logBlankVolts[1]) - .71891) / -2.1235).tolist()
    OD3 = (((np.log10(morbido3)/logBlankVolts[2]) - .71891) / -2.1235).tolist()
    OD4 = (((np.log10(morbido4)/logBlankVolts[3]) - .71891) / -2.1235).tolist()
    OD5 = (((np.log10(morbido5)/logBlankVolts[4]) - .71891) / -2.1235).tolist()
    OD6 = (((np.log10(morbido6)/logBlankVolts[5]) - .71891) / -2.1235).tolist()
    OD7 = (((np.log10(morbido7)/logBlankVolts[6]) - .71891) / -2.1235).tolist()
    OD8 = (((np.log10(morbido8)/logBlankVolts[7]) - .71891) / -2.1235).tolist()
    
    df = [dateTime, readTime, morbido1, morbido2, morbido3, morbido4, morbido5, morbido6, morbido7, morbido8, OD1, OD2, OD3, OD4, OD5, OD6, OD7, OD8]
    my_df = pd.DataFrame(df)
    my_df = my_df.T
    global globalDF 
    globalDF = my_df    
    csvTitle = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.csv'
    my_df.to_csv(csvTitle, index = True, header = ['DateTime', 'Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'OD1', 'OD2', 'OD3', 'OD4', 'OD5', 'OD6', 'OD7', 'OD8'])
    print(my_df)
    print()
    print("new csv file on Desktop: ", csvTitle)

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
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
    Volttitle = datetime.now().strftime('%Y-%m-%d_%H-%M') + ' Voltage plot'
    plt.title(Volttitle)
    plt.legend(loc='upper right')
    plt.show()

    fig = plt.figure()
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
    ODtitle = datetime.now().strftime('%Y-%m-%d_%H-%M') + ' OD plot'
    plt.title(ODtitle)
    plt.legend(loc='upper left')
    plt.show()
    

###########################################################################################################################################
###########################################################################################################################################
###########################################################################################################################################
#main code
    
    
#def main(): 
experimentTime = time.time()
analogVolt1 = []
analogVolt2 = []
logBlankVolts = []
blankVolts = []
dateTime = []
readTime = []
condition = 1
global globalDF

while(condition):
    print("\n")
    print("Type '0' to quit the program.")
    print("Type '1' to measure OD.")
    print("Type '2' to plot Voltage vs. Time.")
    print("Type '3' for a batch culture run.")
    print("Type '4' to export data as a csv.")
    print("Type '5' for a fixed chemostat run.")
    print("Type '6' to test the photodiode")
    print("Type '7' to prime morbidostat")
    print("Type '8' to test morbidostat parts")
    print("Type '9' to set blank media voltages")
    print("Type '10' for a turbidostat run")
    var = input(": ")
#    print("You entered " + str(var))
        
    try: 
        currInput = int(var)
        print("current input: ", currInput)
            
        if(currInput == 0):
            print("quitting")
            condition = 0
            print("condition is 0")
            break
            
        elif(currInput == 2): 
            print("plotting...")
            plotOD()
            #break
                
        elif(currInput == 3): 
            print("continuous read")
            timeLimit = input("enter the length of time (in min) to read the culture: ")
            print("set time in min: ", timeLimit)
            timeLimit = timeLimit * 60
            contRead(timeLimit)
            
        elif(currInput == 4):
            print("exporting data...")
            exportData()
            
        elif(currInput == 5):
            print("chemostat mode")
            timeLim = input("enter the length of time (in min) to read the culture: ")
            pumpTime = input("enter time interval (in min) between turning on the pump: ")
            print("time limit(min): ", timeLim)
            print("pump period(min): ", pumpTime)
            timeLim = timeLim * 60
            chemostat(timeLim, pumpTime)
            
        elif(currInput == 6):
            print("Testing photodiode")
            photoTest()
            
            
        elif(currInput == 1): 
            #chan = input("Enter the channel number of the morbidostat to read its OD: ")
            try:
                #currChan = int(chan)
                readOD()
                #break
            except ValueError: 
                print("please enter a valid channel")
        
        elif(currInput == 8): 
            print("testing system")
            sysTest()
            
        elif(currInput == 7): 
            print("priming system")
            sysPrime()
            
        elif(currInput == 9):
            print(blankVolts)
            print(logBlankVolts)
            print("set blanks")
            blankVoltages()
                
        elif(currInput == 10):
            print("Turbidostat Mode")
            timeLim = input("enter the length of time (in min) to read the culture: ")
            pumpTime = input("enter time interval (in min) between turning on the pump: ")
            ODnum = input("input fixed OD: ")
            OD = float(ODnum)
            print("time limit(min): ", timeLim)
            print("pump period(min): ", pumpTime)
            print("OD: ", OD)
            timeLim = timeLim * 60
            NormVolt = -2.1235*OD+.71891
            print("Normalized Voltage: ", NormVolt)
            Turbido(timeLim, pumpTime, NormVolt)         
        

    except ValueError: 
        print("Not a valid input, please try again: ")
        

#if __name__ == "__main__": main()












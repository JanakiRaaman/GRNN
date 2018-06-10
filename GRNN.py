import csv
#import numpy as np
#from sklearn import linear_model
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib import pyplot
from math import *
now = datetime.now()
dates = []
prices = []
df=[]
c=0
bias=[]


def graph(x,y,sname):
    pyplot.plot(x, y, color='blue', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='red', markersize=14)
    pyplot.xlabel('Date')
    pyplot.ylabel('Stock price')
    pyplot.title(sname+" VARIATION GRAPH")
    pyplot.show()

    
def get_data(filename,z,sname):
    with open(filename,'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            if(row[6]==sname):
                dates.append(z)
                df.append(row[0])
                prices.append(float(row[4]))
                z=z+1            
        return z
def calcden(arr):
    sum=0
    c=0
    gaussiankernel=0
    for i in arr:
        sum=sum+i
        c+=1
        mean=round((i-(sum/c))**2,2)
        if mean>0:
            gaussiankernel+=exp(1/(mean/(2*gamma)))
    return gaussiankernel

def calbias(x):
    for i in range(len(x)-1):
        bias.append(float(x[i+1])-float(x[i]))

def mean(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum/len(arr)

def calnum(arr,bias,meanbias):
    sum=0
    c=0
    numerator=0
    for i in arr:
        sum+=i
        c+=1
        if(c==len(bias)):
            break
        elif bias[c]>0:
            num=(bias[c]*round((i-(sum/c))**2,2))+float(meanbias)
        elif bias[c]<0:
            num=(bias[c]*round((i-(sum/c))**2,2))-float(meanbias)                
        if(num>0):
            numerator+=num
    return numerator

def biascount(arr):
    neg=0
    pos=0
    for i in arr:
        if(i<0):
            neg+=1
        else:
            pos+=1
    if(neg>pos):
        return 0
    else:
        return 1
z=1
sname=input("Enter the stock name\n")
z=get_data('stock.csv',z,sname)
gamma=.06
denominator=calcden(prices)
calbias(prices)
meanbias=mean(bias)
numerator=calnum(prices,bias,meanbias)
if(biascount(bias)):
    val=prices[len(prices)-1]+(numerator/denominator)
else:
    val=prices[len(prices)-1]-(numerator/denominator)
prices.append(val)
df.append(str(now.day)+"-"+str(now.month)+"-"+str(now.year))
print("Predicted Closing Stock price for "+sname+" is",str(val))
graph(df[-8:],prices[-8:],sname)

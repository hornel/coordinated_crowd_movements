# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 15:31:01 2017

@author: Johanna
"""



from numpy import *
from matplotlib.pylab import *
from counter import n , m
def analyse():
    maxDanger_TimeEvolution=zeros((n,m))
    averageDanger_TimeEvolution=zeros((n,m))
    
    t=linspace(0,1,n)

    figure()    
    title('Maximum Danger for given Configuration')
    
    for j in range(0,m):        #iterating over different seeds
        for k in range(0,n):    #iterating over time steps
            filename='out_%s_%s' %(j,k)
            exec("from %s import *" %filename, globals())   #importing data for given seed and time steps
            maxDanger_TimeEvolution[k,j]+=maxDanger
        plot(t,maxDanger_TimeEvolution[:,j],'--',linewidth=0.2)   #creating plot
    
    plot(t,mean(maxDanger_TimeEvolution,axis=1),linewidth=1.5,label='mean for different seeds')
    legend()
    savefig('maxDanger_timeEvolution.jpg')
    show()    
    
    
    figure()    
    title('Average Danger for given Configuration')
    
    for j in range(0,m):        #iterating over different seeds
        for k in range(0,n):    #iterating over time steps
            filename='out_%s_%s' %(j,k)
            exec("from %s import *" %filename, globals())   #importing data for given seed and time steps
            averageDanger_TimeEvolution[k,j]+=averageDanger
        plot(t,averageDanger_TimeEvolution[:,j],'--',linewidth=0.2)
    
    plot(t,mean(averageDanger_TimeEvolution,axis=1),linewidth=1.5,label='mean for different seeds')
    legend()
    savefig('averageDanger_timeEvolution.jpg')
    show()

analyse()

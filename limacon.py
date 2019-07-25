import matplotlib
from matplotlib import pyplot as pl
import numpy as np
#a=np.arange(0.8,1.4,0.2)
for i in range(-360,360):
    r=0.8+np.cos(i)
    x=r*np.cos(i)
    y=r*np.sin(i)
    pl.scatter(x,y,color='c')
    pl.text(2.12,1.5,'r=0.8',color='c')
    r1=1.0+np.cos(i)
    x1=r1*np.cos(i)
    y1=r1*np.sin(i)
    pl.scatter(x1,y1,color='g')
    pl.text(2.12,1.4,'r=1.0',color='g')
    r2=1.2+np.cos(i)
    x2=r2*np.cos(i)
    y2=r2*np.sin(i)
    pl.scatter(x2,y2,color='m')
    pl.text(2.12, 1.3, 'r=1.2',color='m')
pl.show()

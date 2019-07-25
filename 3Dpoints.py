import pandas as pd
import matplotlib
from matplotlib import pyplot as pl,style
from mpl_toolkits.mplot3d import Axes3D
style.use('dark_background')
fig=pl.figure()
ax=fig.add_subplot(111,projection='3d')
x=[2,3,7,8,9]
y=[4,6,8,4,3]
z=[3,7,6,9,2]
ax.scatter(x,y,z,c='r',marker='o')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
pl.show()

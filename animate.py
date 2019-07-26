import matplotlib.pyplot as pl
import numpy as np
import matplotlib.animation as an
fig, ax=pl.subplots()
x=np.arange(0,2*np.pi,0.01)
line1, =ax.plot(x,np.sin(x))
line2,=ax.plot(x,np.cos(x))
def animate(i):
    line1.set_ydata(np.sin(x+i/10.0))
    line2.set_ydata(np.cos(x+i/10.0))
    return line1,line2,
def init():
    line1.set_ydata(np.ma.array(x,mask=True))
    line2.set_ydata(np.ma.array(x, mask=True))
    return line1,line2,
ani=an.FuncAnimation(fig,animate,np.arange(1,200),init_func=init,interval=25,blit=True)
pl.show()


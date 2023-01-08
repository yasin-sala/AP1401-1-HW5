import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image
import matplotlib.image as mping
import os
import numpy as np
from matplotlib.animation import FuncAnimation 

filename = './resources/image.jpeg'
primary = mping.imread(filename)
bw = primary.copy()
bw[:,:,0] = bw[:,:,1] = bw[:,:,2] = np.dot(bw, [0.4, 0.5, 0.01])
####################################################### making figure
fig = plt.figure(1,figsize=(8,5),facecolor='r')
####################################################### making middle image
ax1 = fig.add_axes([0.1, 0.1, 0.9, 0.9],frame_on = False)
ax1.set_facecolor('red')
ax1.axis('off')
ax1.imshow(primary)
####################################################### making sine wave
ax2=fig.add_axes([0.29,0.4,0.51,0.05],frame_on=False)
ax2.axis('off')
# creating a plot
lines_plotted = ax2.plot([],color='black',lw = 2)	
# putting limits on x axis since
# it is a trigonometry function
# (0,2∏)
line_plotted = lines_plotted[0]
plt.xlim(0,2*np.pi)
# putting limits on y since it is a
# cosine function
plt.ylim(-1.1,1.1)
# initialising x from 0 to 2∏
x = np.linspace(0,2*np.pi,1000)
#initially
y = 0
# function takes frame as an input
def AnimationFunction(i):
  y = np.cos(10* np.pi * (x - 0.01 * i))
  line_plotted.set_data((x, y))
anim = FuncAnimation(fig, AnimationFunction, frames=100, interval=25)
############################################ makeing gray image of first image
ax3 = fig.add_axes([0.5 ,0.5 ,0.7 ,0.5])
ax3.imshow(bw)
ax3.axis('off')
############################################ add text box
plt.text(-2000,2200,"DAEMON",fontsize=38,bbox = dict(facecolor = 'white'))
## saveing as a gif file
#fig.savefig('plot.jpeg')
anim.save('continuousSineWave.gif', fps = 30)
plt.show()
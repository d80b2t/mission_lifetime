
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from matplotlib.patches import Rectangle
from matplotlib         import colors as mcolors
from matplotlib import colormaps

from astropy.io import ascii
from astropy.io import fits


data = pd.read_csv('../data/mission_lifetime.dat')

length_of_mission = data['Mission_End_Year']-data['Mission_Start_Year']
cost              = data['Cost_in_millions'] 

## Setting up the plot
fig, ax = plt.subplots(figsize=(10, 6), dpi=80, facecolor='w', edgecolor='k')

## Adjusting the Whitespace for the plots
left   = 0.18   # the left side of the subplots of the figure
right  = 0.98   # the right side of the subplots of the figure
bottom = 0.18   # the bottom of the subplots of the figure
top    = 0.96   # the top of the subplots of the figure
wspace = 0.26   # the amount of width reserved for blank space between subplots
hspace = 0.06   # the amount of height reserved for white space between subplots
plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)
 
## Some NPR defaults
alpha           = 1.0
fontsize        = 16
labelsize       = fontsize
tickwidth       = 2.0
linewidth       = 2.4
tickwidth       = 2.0
ticklength      = 6.0
ticklabelsize   = labelsize
majorticklength = 12
minorticklength = 6

# COLOR MAP
colormaps['hsv']

## Some general links/tips on stylings::
##
## https://matplotlib.org/3.1.0/tutorials/introductory/customizing.html
## https://stackoverflow.com/questions/25451294/best-way-to-display-seaborn-matplotlib-plots-with-a-dark-ipython-notebook-profil
## https://smashingtheory.blogspot.com/search/label/matplotlib
## https://earthobservatory.nasa.gov/blogs/elegantfigures/2013/08/05/subtleties-of-color-part-1-of-6/


## Axes limits
xmin =    1980.
xmax =    2830.0
ymin =     0.1
ymax = 45.
ax.set_xlim([xmin,xmax])
ax.set_ylim([ymin, ymax])
#ax.set_yscale('log')


## 0 = Gamma Ray; 1 = Xray; 2 = Ultraviolet, 3 = optical, 4= nearinfrared, 5=midinfrared, 6=farinfrared, 7=submm

##  https://stackoverflow.com/questions/76406816/how-to-set-broken-bar-order-after-grouping-the-dataframe

##  https://www.geeksforgeeks.org/matplotlib-pyplot-broken_barh-in-python/
##  Syntax: matplotlib.pyplot.broken_barh(xranges, yrange, *, data=None, **kwargs)
'''
Parameters:    

xranges : sequence of tuples (xmin, xwidth)
Each tuples gives the position(xmin) of the rectangle and it’s horizontal extension(xwidth) from that position.

yranges : (ymin, ymax)
In the above attribute, ymin gives the position of the rectangle and ymax gives the vertical extension from ymin.
'''
#plt.barh(cost, width=length_of_mission, height=20.2, left=data['Mission_Start_Year']) #, color=data['wavelength'])  
plt.barh(length_of_mission, cost, left=data['Mission_Start_Year'])  

##https://stackoverflow.com/questions/53531429/valueerror-invalid-rgba-argument-what-is-causing-this-error


## Axes labels
ax.set_xlabel(r'Year')
ax.set_ylabel(r'Cost in \$ millions')

## Axes style
ax.tick_params(axis='both', which='major', labelsize=labelsize, top=True, right=True, direction='in', length=ticklength,   width=tickwidth)
ax.tick_params(axis='both', which='minor', labelsize=labelsize, top=True, right=True, direction='in', length=ticklength/2, width=tickwidth)


plt.savefig('mission_lifetime_temp.png', format='png')
plt.close(fig)

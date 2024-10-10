
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
cost_per_year     = cost/length_of_mission 

## Setting up the plot
fig, ax = plt.subplots(figsize=(6, 12), dpi=80, facecolor='w', edgecolor='k')

## Adjusting the Whitespace for the plots
left   = 0.18   # the left side of the subplots of the figure
right  = 0.94   # the right side of the subplots of the figure
bottom = 0.12   # the bottom of the subplots of the figure
top    = 0.90   # the top of the subplots of the figure
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
markersize      = 16.0
ticklabelsize   = labelsize
majorticklength = 12
minorticklength = 6

# COLOR MAP
colormaps['hsv']

## Axes limits
xmin =    0.
xmax =    40
ymin =     0.1
ymax =   500.0 # 4000. for Webb
ax.set_xlim([xmin,xmax])
ax.set_ylim([ymin, ymax])
#ax.set_yscale('log')

## 0 = Gamma Ray; 1 = Xray; 2 = Ultraviolet, 3 = optical, 4= nearinfrared, 5=midinfrared, 6=farinfrared, 7=submm


#plt.plot(length_of_mission, (cost/length_of_mission), 
plt.scatter(length_of_mission, cost_per_year, 
    marker='o',
    s=    markersize*4., linewidth=linewidth)
#    color=data['wavelength']) 
#    markerfacecolor='white',
 #   markeredgecolor='gray',
  #  markeredgewidth=2)


n= data['Mission']
for i, txt in enumerate(n):
    ax.annotate(txt, (length_of_mission[i], cost_per_year[i]), 
                fontsize=fontsize/1.4, 
                xytext=(5, 5), 
                textcoords='offset points',  # Offset the annotation
                arrowprops=dict(arrowstyle='-', lw=0.5))  # Optional: arrows to point to data points


## Axes labels
ax.set_xlabel(r'Mission length [Years]')
ax.set_ylabel(r'Cost per year [\$ millions]')

## Axes style
ax.tick_params(axis='both', which='major', labelsize=labelsize, top=True, right=True, direction='in', length=ticklength,   width=tickwidth)
ax.tick_params(axis='both', which='minor', labelsize=labelsize, top=True, right=True, direction='in', length=ticklength/2, width=tickwidth)


plt.savefig('mission_lifetime_peryear_temp.png', format='png')
plt.close(fig)

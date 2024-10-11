import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('../data/mission_lifetime.dat') 

# Create column with mission length
df['Mission_Length']= df['Mission_End_Year']-df['Mission_Start_Year']

# Create column with colors
df['color'] = ['xkcd:pink',         ## R
                 'xkcd:baby blue',  ## B 
                 'xkcd:mint',       ## G
                 'xkcd:red', 
                 'xkcd:blue', 
                 'xkcd:green', 
                 'xkcd:orange', 
                 'xkcd:aqua', 
                 'xkcd:lavender', 
                 ]

## Setting up the plot
#fig, ax = plt.subplots(figsize=(8, 8), dpi=80, facecolor='w', edgecolor='k')

## Adjusting the Whitespace for the plots
left   = 0.14   # the left side of the subplots of the figure
right  = 0.94   # the right side of the subplots of the figure
bottom = 0.14   # the bottom of the subplots of the figure
top    = 0.90   # the top of the subplots of the figure
wspace = 0.26   # the amount of width reserved for blank space between subplots
hspace = 0.06   # the amount of height reserved for white space between subplots
#plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)
 
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

## Axes limits
xmin, xmax = 1980, 2040
ymin, ymax = 0.0, 500   # 4000. for Webb
#ax.set_xlim([xmin, xmax])
#ax.set_ylim([ymin, ymax])

# Basic plot, save Barcontainer in variable fig
fig = plt.barh(df['Cost_in_millions'],
               df['Mission_Length'],
               height=50,
               left=df['Mission_Start_Year'],
               color=df['color']
              )

# Custom tickmarks
plt.xticks(np.arange(min(df['Mission_Start_Year']) - 5, max(df['Mission_Start_Year']) + 10, 3.0))

# Add labels inside
plt.bar_label(fig,
              labels=df['Mission'],
              label_type='center'
             )

#plt.savefig('mission_lifetime_joao_temp.png', format='png')
#plt.close(fig)

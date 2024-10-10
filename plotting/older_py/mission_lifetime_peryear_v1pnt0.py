
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches

from matplotlib         import colors as mcolors
from matplotlib import colormaps

df = pd.read_csv('../data/mission_lifetime.dat')

length_of_mission = df['Mission_End_Year']-df['Mission_Start_Year']
cost              = df['Cost_in_millions'] 
cost_per_year     = cost/length_of_mission 

## Setting up the plot
fig, ax = plt.subplots(figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')

## Adjusting the Whitespace for the plots
left   = 0.14   # the left side of the subplots of the figure
right  = 0.94   # the right side of the subplots of the figure
bottom = 0.14   # the bottom of the subplots of the figure
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
xmin, xmax = 0, 40
ymin, ymax = 0.1, 500   # 4000. for Webb
ax.set_xlim([xmin, xmax])
ax.set_ylim([ymin, ymax])

## 0 = Gamma Ray; 1 = Xray; 2 = Ultraviolet, 3 = optical, 4= nearinfrared, 5=midinfrared, 6=farinfrared, 7=submm
# Custom color mapping based on wavelength
color_map = {
    0: 'black',      # Gamma Ray
    1: 'grey',       # X-ray
    2: 'royalblue',  # Ultraviolet
    3: 'green',      # Optical
    4: 'orange',     # Near Infrared
    5: 'red',        # Mid Infrared
    6: 'purple',     # Far Infrared
    7: 'brown'       # Submm
}

# Assign colors based on the 'wavelength' column
#cmap = colormaps['viridis']  # Using 'viridis' colormap
#norm = plt.Normalize(df['wavelength'].min(), df['wavelength'].max())
#colors = cmap(norm(df['wavelength']))

# Apply color mapping to the 'wavelength' column
point_colors = df['wavelength'].map(color_map)


#plt.plot(length_of_mission, (cost/length_of_mission), 
scatter = ax.scatter(length_of_mission, cost_per_year, 
                     marker='o', s=markersize*16., linewidth=linewidth, 
                     c=point_colors, edgecolor='gray')

#cbar = fig.colorbar(scatter, ax=ax)
#cbar.set_label('Wavelength', fontsize=fontsize)

# Create custom legend
legend_labels = {
    0: 'Gamma Ray', 
    1: 'X-ray', 
    2: 'Ultraviolet',
    3: 'Optical', 
    4: 'Near Infrared', 
    5: 'Mid Infrared',
    6: 'Far Infrared',
    7: 'Submm'
}

# Create a list of Patch objects (one for each wavelength type)
legend_patches = [mpatches.Patch(color=color_map[w], label=legend_labels[w]) for w in legend_labels]

# Add the legend to the plot
ax.legend(handles=legend_patches, 
          title='Wavelength', fontsize=fontsize/1.4, title_fontsize=fontsize, 
          frameon=True, framealpha=1.0, fancybox=True, ncol=1)

# Annotating each mission individually
ax.annotate('Hubble Space Telescope', (length_of_mission[0], cost_per_year[0]), 
            fontsize=fontsize/1.4, xytext=(-155, 10), textcoords='offset points',
            style='italic', weight='bold' )

ax.annotate('James Webb Space Telescope', (length_of_mission[1], cost_per_year[1]), 
            fontsize=fontsize/1.4, xytext=(-40, -10), textcoords='offset points', 
            style='italic', weight='bold' )

ax.annotate('ESA ISO', (length_of_mission[2], cost_per_year[2]), 
            fontsize=fontsize/1.4, xytext=(5, 10), textcoords='offset points',
            style='italic', weight='bold' )

ax.annotate('ESA Herschel', (length_of_mission[3], cost_per_year[3]), 
            fontsize=fontsize/1.4, xytext=(5, 8), textcoords='offset points', 
            style='italic', weight='bold' )

ax.annotate('ESA Planck', (length_of_mission[4], cost_per_year[4]), 
            fontsize=fontsize/1.4, xytext=(5, 8), textcoords='offset points', 
            style='italic', weight='bold' )

ax.annotate('NASA Compton GRO', (length_of_mission[5], cost_per_year[5]), 
            fontsize=fontsize/1.4, xytext=(5, 10), textcoords='offset points', 
            style='italic', weight='bold' )

ax.annotate('NASA Kepler', (length_of_mission[6], cost_per_year[6]), 
            fontsize=fontsize/1.4, xytext=(5, -10), textcoords='offset points',
             style='italic', weight='bold' )

ax.annotate('NASA Spitzer', (length_of_mission[7], cost_per_year[7]), 
            fontsize=fontsize/1.4, xytext=(5, 10), textcoords='offset points', 
            style='italic', weight='bold' )

ax.annotate('NASA WISE', (length_of_mission[8], cost_per_year[8]), 
            fontsize=fontsize/1.4, xytext=(5, -15), textcoords='offset points', 
            style='italic', weight='bold' )

# Add a subtle grey grid
ax.grid(color='grey', linestyle='--', linewidth=0.5, alpha=0.5)  # Adjust alpha for transparency


## Axes labels
ax.set_xlabel(r'Mission length [Years]',       fontsize=fontsize*1.2)
ax.set_ylabel(r'Cost per year  [\$ millions]', fontsize=fontsize*1.2)

## Axes style
ax.tick_params(axis='both', which='major', labelsize=labelsize*1.2, top=True, right=True, direction='in', length=ticklength,   width=tickwidth)
ax.tick_params(axis='both', which='minor', labelsize=labelsize*1.2, top=True, right=True, direction='in', length=ticklength/2, width=tickwidth)

# Set the title of the plot
ax.set_title('Astrophysics Missions', fontsize=fontsize, fontweight='bold')

# Add a watermark to the plot
ax.text(0.025, 0.85, '(c) Nic Ross', 
        fontsize=16, ha='left', va='bottom', 
        alpha=0.10, color='black', transform=ax.transAxes)

plt.savefig('mission_lifetime_peryear_temp.png', format='png')
plt.close(fig)

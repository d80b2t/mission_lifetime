import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../data/mission_lifetime.dat')

length_of_mission = df['Mission_End_Year']-df['Mission_Start_Year']
cost              = df['Cost_in_millions'] 
cost_per_year     = cost/length_of_mission 

# Data
missions      = df['Mission']
start_years   = df['Mission_Start_Year']
end_years     = df['Mission_End_Year']
mission_costs = df['Cost_in_millions']

# Calculate the mission lengths
mission_lengths = [end_years[i] - start_years[i] for i in range(len(missions))]

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

## Axes limits
xmin, xmax = 1990, 2030
ymin, ymax =    0,   500   # 4000. for Webb
#ax.set_xlim([xmin, xmax])
#ax.set_ylim([ymin, ymax])

# Plot each mission with its start year and duration
for i in range(len(missions)):
    ax.barh(missions[i], mission_lengths[i], left=start_years[i], color='skyblue')
#    ax.barh(mission_costs[i], mission_lengths[i], left=start_years[i], color='skyblue')



# Labeling the axes
ax.set_xlabel('Year')
ax.set_ylabel('Missions')

# Add a title
ax.set_title('Space Missions - Duration and Start Years')

# Add the costs as annotations
for i in range(len(missions)):
    ax.text(end_years[i] + 0.2, i, f"${mission_costs[i]:,.0f}M", va='center')

# Show the plot

plt.savefig('mission_lifetime_chat_temp.png', format='png')
plt.close(fig)

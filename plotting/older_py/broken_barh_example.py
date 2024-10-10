##
##
##  https://www.geeksforgeeks.org/matplotlib-pyplot-broken_barh-in-python/
##
##


# importing module 
import matplotlib.pyplot as plt 
  
  
# Adding title to the plot 
plt.title('GEEKSFORGEEKS - EXAMPLE') 
  
# adding x axis label to the plot 
plt.xlabel('x-label') 
  
# label for y axis  for the plot 
plt.ylabel('y-label') 
  
x_1 = [(1, 4), (10, 7)] 
y_1 = (2, 2) 
  
# Plotting the chart 
plt.broken_barh(x_1, y_1, facecolors ='green') 
  
x_2 = [(10, 1), (15, 4), (25, 6)] 
y_2 = (6, 2) 
  
# Plotting the chart 
plt.broken_barh(x_2, y_2, facecolors ='cyan') 
  
plt.show() 

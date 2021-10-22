# how to install libraries
# pip install [lib-name] or
# pip3 install [lib-name]
# Be careful: sometimes admin rights are needed (win: "run as administrator", mac: "sudo pip install ...")
# 
# pip install matplotlib
import matplotlib.pyplot as plt

# how to use visit: https://matplotlib.org/

##### start of exam knowledge #####

# Data for plotting
# 1st step: defining the values for the x-axis
x = range(-5, 6, 1)

# 2nd step: creating an array for values of the y-axis
# set every single value to 0
y = [0] * len(x)

# 3rd step: calculating the values of the y-axis using the x-axis
i = 0
for xx in x:
    y[i] = xx * xx
    i = i + 1

##### end of exam knowledge #####


##### start of practice knowledge ######

# 4nd step: defining the plot
# the figure fig
# the axes ax
fig, ax = plt.subplots()

# setting the data to plotted
ax.plot(x, y)

# setting the "user interface"
ax.set(xlabel='x-Wert', ylabel='Funktionswert',
       title='Eine Parabel')

# showing a grid 
ax.grid()

# show it
plt.show()

##### end of practice knowledge ######

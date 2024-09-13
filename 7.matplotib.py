# it gives us graphical representation of data and datapoints

# making plots

import matplotlib.pyplot as plt
# import numpy to get data for a plots
import numpy as np

# x=np.linspace(-15,10,100)
# y=np.sin(x)
# z=np.cos(x)

# ploting a data

# sin wave
# plt.plot(x,y)#this will create a empty figure
# plt.show()

# # cosin wave
# plt.plot(x,z)
# # adding x axis ,,y axis in plot
# plt.xlabel("angle")
# plt.ylabel("cosin value")
# plt.title("cosin wave")
# plt.show()

# parabola
# x1=np.linspace(-10,10,20)
# y2=x1**2
# ploting with different color and pattern
# plt.plot(x1,y2,'r+')
# plt.show()

# ploting two graphs 
# plt.plot(x,np.sin(x),"g-")
# plt.plot(x,np.cos(x),'r--')
# plt.show()

# # Bar plot
# fig=plt.figure()
# ax1 = fig.add_axes([0,0,1,1])# this will enclose out plot in rectriangle ,, 
#                             # frist 2 values represtents the co-ordanes ,,
#                             # next two represents hight and width of rectriangle
# lang=["java","python","javascript","c","c++"]
# people=[213,76,34,89,45]

# ax1.bar(lang,people)
# plt.xlabel("Language")
# plt.ylabel("People")

# plt.show()

# pie chart

# fig=plt.figure()
# ax1 = fig.add_axes([0,0,1,1])
# lang=["java","python","javascript","c","c++"]
# people=[213,76,34,89,45]
# ax1.pie(people,labels=lang,autopct='%1.1f%%')
# plt.show()

# scatter plot 
# x=np.linspace(0,10,10)
# y=np.sin(x)
# z=np.cos(x)
# fig3=plt.figure()
# ax=fig3.add_axes([0,0,1,1])
# ax.scatter(x,y,color='b')
# ax.scatter(x,z,color='g')
# plt.show()

# 3D Scatter plot

fig3=plt.figure()
ax=plt.axes(projection='3d')
z=20 * np.random.random(100)
x=np.sin(z)
y=np.cos(z)
ax.scatter(x,y,z,c=z,cmap='Blues')
plt.show()
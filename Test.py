from matplotlib import pyplot as plt
from Linear_Regression import *

# prep data
x = [i for i in range(1,100)]
y = [random.randint(0,1000) for i in x]
z = [x+y for x,y in zip(x,y)]
data = [[a] for a,b in zip(x,y)]

for i in data:
    i.append(y[data.index(i)])

#make a model
model = LinearRegression(data,v_m(z))
yn = model.predict(data)

print("Parameters: ",model.params,"There is small deviation in the intercept due to rounding errors")

#plot fancy graph (I like looking at graphs that say good things)
a = plt.axes(projection = "3d")
a.plot3D(x,y,yn,c="yellow")
a.scatter3D(x,y,z,c=z,cmap = "winter")

plt.show()

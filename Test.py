from matplotlib import pyplot as plt
from Linear_Regression import *

#test dataset of celsius to kelvin
x = [i for i in range(50)]
y = [a+273 for a in x]

testx = [i for i in range(51,100)]
testy = [i+273 for i in testx]

model = LinearRegression(v_m(x),v_m(y))
yn = model.predict(v_m(testx))

print("Parameters: ",model.params,"There is small deviation in the intercept due to rounding errors")

plt.scatter(testx,testy)
plt.plot(testx,yn,color='black')
plt.show()

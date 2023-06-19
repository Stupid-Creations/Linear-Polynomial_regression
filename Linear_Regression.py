from Matrix import *
# use v_m for 1D arrays
class LinearRegression:
    def __init__(self,X,Y,poly1=False,degree=1):
        self.fit(X,Y,poly1,degree)
    def change_input(self,X,poly=False,degree = 1):
        if poly==False:
            x = copy_matrix(X)
            for i in range(len(x)):
                x[i].insert(0,1)
            return x
        elif poly == True:
            a = self.change_ip(X,degree)
            return a
    def change_ip(self,X,degree):
        x = self.change_input(copy_matrix(X))
        for i in range(len(x)):
            for j in range(len(x[0])):
                x[i][j] = x[i][j]**(j+(degree-1))
        return x
    def predict(self,X,poly=False,degree=1):
        return m_v(dot(self.change_input(X,poly,degree),self.params))
    def gradient(self,X,Y,poly=False,degree=1):
        x = self.change_input(X,poly,degree)
        try:
            return dot(getMatrixInverse(dot(transpose(x),x)),dot(transpose(x),Y))
        except:
            raise ValueError("Input values dependent")
    def fit(self,X,Y,poly=False,degree=1):
        self.params = self.gradient(X,Y,poly,degree)
        print("The error of the model is: ",self.cost(X,Y,poly,degree))
    def cost(self,X,Y,poly=False,degree=1):
        return sum([(a-b)**2 for a,b in zip(self.predict(X,poly,degree),m_v(Y))])/len(Y)

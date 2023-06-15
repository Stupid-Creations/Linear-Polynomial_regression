from Matrix import *
class LinearRegression:
    def __init__(self,X,Y):
        self.fit(X,Y)
    def change_input(self,X):
        x = X
        for i in range(len(x)):
            x[i].insert(0,1)
        return x
    def predict(self,X):
        return m_v(dot(self.change_input(v_m(X)),self.params))
    def gradient(self,X,Y,oneindependent=True):
        if oneindependent:
            x,y = self.change_input(v_m(X)),v_m(Y)
        return dot(getMatrixInverse(dot(transpose(x),x)),dot(transpose(x),y))
    def fit(self,X,Y):
        self.params = self.gradient(X,Y)
        print("The error of the model is: ",self.cost(X,Y))
    def cost(self,X,Y):
        return sum([(a-b)**2 for a,b in zip(self.predict(X),Y)])/len(Y)

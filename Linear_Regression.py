from Matrix import *
#NOTE: YOU NEED TO USE v_m(data) IF YOU ARE USING DATA IN FORM OF 1D ARRAY
class LinearRegression:
    def __init__(self,X,Y):
        self.fit(X,Y)
    def change_input(self,X):
        x = copy_matrix(X)
        for i in range(len(x)):
            x[i].insert(0,1)
        return x
    def predict(self,X):
        return m_v(dot(self.change_input(X),self.params))
    def gradient(self,X,Y):
        x = self.change_input(X)
        return dot(getMatrixInverse(dot(transpose(x),x)),dot(transpose(x),Y))
    def fit(self,X,Y):
        self.params = self.gradient(X,Y)
        print("The error of the model is: ",self.cost(X,Y))
    def cost(self,X,Y):
        return sum([(a-b)**2 for a,b in zip(self.predict(X),m_v(Y))])/len(Y)

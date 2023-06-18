from Matrix import *
#NOTE: PLEASE USE v_m(data) IF ANY OF YOUR DATA IS A 1D ARRAY
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
        try:
            return dot(getMatrixInverse(dot(transpose(x),x)),dot(transpose(x),Y))
        except:
            raise ValueError("Input values dependent")
    def fit(self,X,Y):
        self.params = self.gradient(X,Y)
        print("The error of the model is: ",self.cost(X,Y))
    def cost(self,X,Y):
        return sum([(a-b)**2 for a,b in zip(self.predict(X),m_v(Y))])/len(Y)

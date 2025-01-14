import numpy as np
import sklearn.linear_model as scireg

def euclidean_distance(point1, point2):
    return np.linalg.norm(point1 - point2)

class Calibrator:

    def __init__(self):
        self.X = []
        self.Y_y = []
        self.Y_x = []
        self.reg = None
        self.reg_x = scireg.Ridge(alpha=1.0)
        self.reg_y = scireg.Ridge(alpha=1.0)
        self.fitted = False

    def add(self,x,y,ref_point,fit_point):
        self.X.append(x.flatten())
        self.Y_y.append(y[1])
        self.Y_x.append(y[0])

        __tmp_X =np.array(self.X)
        __tmp_Y_y =np.array(self.Y_y)
        __tmp_Y_x =np.array(self.Y_x)

        self.reg_x.fit(__tmp_X,__tmp_Y_x)
        self.reg_y.fit(__tmp_X,__tmp_Y_y)
        self.fitted = True

    def predict(self,x):
        if self.fitted:
            x = x.flatten()
            x = x.reshape(1, -1)
            y_x = self.reg_x.predict(x)[0]
            y_y = self.reg_y.predict(x)[0]
            return np.array([y_x,y_y])
        else:
            return np.array([0.0,0.0])

    def unfit(self):
        self.fitted = False

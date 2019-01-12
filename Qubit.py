import numpy as np

class Qubit:
    def __init__(self):
        self.state = np.array([[1+0j],
                               [0+0j]])
    def alpha(self):
        return (self.state[0][0])

    def beta(self):
        return (self.state[1][0])
    
    def __repr__(self):
        return str(self.state[0]) + " " + str(self.state[1])

# Identity Gate
class I():
    def __init__(self, qi):
        self.qubit_index = qi
        self.matrix = np.array([[1+0j, 0+0j],
                                [0+0j, 1+0j]])

# Hadamard's Gate
class H():
    def __init__(self, qubit_index):
        self.qubit_index = qubit_index
        self.matrix = 2**(-1/2) * np.array([[1.0, 1.0,],
                                            [1.0, -1.0]])
        
# Pauli's X gate (negation)
class X():
    def __init__(self, qubit_index):
        self.qubit_index = qubit_index
        self.matrix = np.array([[0+0j, 1+0j],
                                [1+0j, 0+0j]])
NOT = X
        
# Pauli's Z gate
class Z():
    def __init__(self, qubit_index):
        self.qubit_index = qubit_index
        self.matrix = np.array([[1+0j, 0+0j],
                                [0+0j, -1+0j]])
        
# Controled Gate
class C():
    def __init__(self, U, cq, tq):
        self.control_qubit = cq
        self.target_qubit = tq
        self.matrix = U(None).matrix

class CNOT(C):
    def __init__(self, cq, tq):
        super(CNOT, self).__init__(X,cq,tq)
import numpy as np

# Identity Gate
class I():
    def __init__(self, quantum_id):
        self.quantum_id = quantum_id
        self.matrix = np.array([[1+0j, 0+0j],
                                [0+0j, 1+0j]])

    def __repr__(self):
        return "-"

# Hadamard's Gate
class H():
    def __init__(self, quantum_id):
        self.quantum_id = quantum_id
        self.matrix = 2**(-1/2) * np.array([[1.0, 1.0,],
                                            [1.0, -1.0]])

    def __repr__(self):
        return "H"
        
# Pauli's X gate (negation)
class X():
    def __init__(self, quantum_id):
        self.quantum_id = quantum_id
        self.matrix = np.array([[0+0j, 1+0j],
                                [1+0j, 0+0j]])

    def __repr__(self):
        return "X"
NOT = X
        
# Pauli's Z gate
class Z():
    def __init__(self, quantum_id):
        self.quantum_id = quantum_id
        self.matrix = np.array([[1+0j, 0+0j],
                                [0+0j, -1+0j]])
    
    def __repr__(self):
        return "Z"

# Controled Gate
class C():
    def __init__(self, U, cq, tq):
        self.control_qubit = cq
        self.target_qubit = tq
        self.matrix = U(None).matrix

    def __repr__(self):
        return "{}→{}".format(self.control_qubit, self.target_qubit)

class CNOT(C):
    def __init__(self, cq, tq):
        super(CNOT, self).__init__(X,cq,tq)

    def __repr__(self):
        return "CNOT." + super(CNOT, self).__repr__()

g = CNOT(1,2)
print(g)
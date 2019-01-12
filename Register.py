from Qubit import Qubit

class Register:
    def __init__(self, n):
        self.size = n
        self.qubits = []
        for i in range(n):
            self.qubits.append(Qubit())
    
    def kroneckerize(self):
        last = self.qubits[0].state
        
        if self.size() == 1:
            return last
        
        for i in range(1,self.size()):
            last = np.kron(last, self.qubits[i].state)
            
        return last
    
    def __repr__(self):
        result = "{\n"
        for i in range(self.size):
            result += "\t{}: {}\n".format(i, self.qubits[i])
        result += "}"
        return result
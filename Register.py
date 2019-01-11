from Qubit import Qubit

class Register:
    def __init__(self, n):
        self.qubits = []
        for i in range(n):
            self.qubits.append(Qubit())
            
    def size(self):
        return len(self.qubits)
    
    def kroneckerize(self):
        last = self.qubits[0].state
        
        if self.size() == 1:
            return last
        
        for i in range(1,self.size()):
            last = np.kron(last, self.qubits[i].state)
            
        return last
    
    def __repr__(self):
        result = "["
        for i in range(self.size()):
            if not i == 0:
                result += " "
            result += "{}".format(self.qubits[i])
            if i < self.size()-1:
                result += "\n"
        result += "]"
        return result
class Step:
    def __init__(self, n):
        self.gates = []
        for i in range(n):
            self.gates.append(I())
        self.gates = np.array(self.gates)
        
    def size(self):
        return len(self.gates)
    
    def addGate(self, gate):
        if issubclass(g.__class__,C):
            cq = gate.control_qubit
            tq = gate.target_qubit
            self.gates[cq] = gate
            self.gates[tq] = gate
        else:
            self.gates[gate.qubit_id] = gate
        
    def kroneckerize(self):
        return kronekerize(0, 1)
    
    def kronekerize(i, last):
        g = self.gates[i]
        
        # TODO END CONDITION
#         if i == self.size()-1:
#             return last
        
        if issubclass(g.__class__,C):
            if i == g.control_qubit:
                # control qubit == 0 case:
                self.gates[g.target_qubit]
                a = kronekerize(i+1, np.kron(np.array([[1,0],[0,0]]), last))
                
                # control qubit == 1 case:
                b = kronekerize(i+1, np.kron(np.array([[0,0],[0,1]]), last))
                return a + b
            else:
                
            
        else:
            return kronekerize(i+1, np.kron(g.matrix, last))
        
    
    def __repr__(self):
        return str(s.gates)


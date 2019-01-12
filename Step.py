from Register import Register
from Gates.Gates import I, C


class Step:
    def __init__(self, n):
        self.gates = []
        for i in range(n):
            self.gates.append(I())

        self.possibilities = []
        
    def size(self):
        return len(self.gates)
    
    def addGate(self, gate):
        if isinstance(gate,C):
            cq = gate.control_qubit
            tq = gate.target_qubit
            self.gates[cq] = gate
            self.gates[tq] = gate
        else:
            self.gates[gate.qubit_index] = gate
    
    def kronekerize(self):
        possibilities = gen_possibilities()
        result = 0
        for possibility in possibilities:

            last = 1
            for i in range(self.size()):
                last = np.kron(last, possibility[i].state)
            result += last
        return result

    def gen_possibilities(self):
        raw_gates = list(self.gates)

        # Set all non-control-gates
        for i in range(self.size()):
            if not isinstance(raw_gates[i],C):
                raw_gates[i] = raw_gates[i].matrix

        # Parallely set control-gates
        return generate_possibilities(0, [raw_gates])

    def gen_possibilities(self, i, possibilities):
        # RECURSION END CONDITION
        if i >= self.size():
            return possibilities

        # Check if the gate of index i has been set before
        # (checking for one possibility is sufficient)
        # If has, skip it 
        if isinstance(possibilities[0][i], numpy.ndarray):
                return generate_possibilities(i+1, possibilities)

        # Because all non-control-gates have been set before,
        # only control-gates have to be set.
        new_possibilities = []
        for possibility in possibilities:
            gate = possibility[i]
            if i == gate.control_qubit:
                # Do not change control qubit
                possibility[gate.control_qubit] = I().matrix

                # control qubit == 0 case:
                # Do not change target qubit
                0_case = list(possibility)
                0_case[gate.target_qubit] = I().matrix
                
                # control qubit == 1 case:
                # Change target qubit
                1_case = list(possibility)
                1_case[gate.target_qubit] = gate.matrix

                # Parallely consider both cases
                new_possibilities.append(0_case)
                new_possibilities.append(1_case)
        return gen_possibilities(i+1, new_possibilities)
                
    def __repr__(self):
        return str(s.gates)
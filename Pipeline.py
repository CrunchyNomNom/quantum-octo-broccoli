class Pipeline:
    def __init__(self, register):
        self.register = register
        self.steps = []
    
    def addStep(self, step):
        rs = self.register.size()
        ss = step.size()
        if not rs == ss:
            raise ValueError("The size of added step ({}) is not equal to the size of the register ({})".format(rs, ss))
        self.steps.append(step)
    
    def execute(self):
        last = self.register.kroneckerize()

        if len(self.steps) == 0:
            return last

        for i in range(len(self.steps)):
            last = np.dot(self.steps[i].kroneckerize(), last)

        return last
    
    def __repr__(self):
        result = "Register:\n"
        result += str(self.register) + "\n"
        
        for i in range(len(self.steps)):
            result += "\nStep {}:".format(i)
            result += "\n" + str(self.steps[i])
        return result
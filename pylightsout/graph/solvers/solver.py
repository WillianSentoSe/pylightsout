class Solver:
    def __init__(self, G):
        self.G = G
        self.S = []

    def solve(self):
        pass

    def check(self):
        """ Checks if the solution is valid and adds to the solutions list. """
        if (self.G.check()):
            self.S.append(self.G.X)
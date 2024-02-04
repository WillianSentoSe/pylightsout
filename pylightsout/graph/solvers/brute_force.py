from .solver import Solver

class BruteForceSolver(Solver):
    def solve(self):
        """ Try every possibility and returns all possible solutions for the Graph """

        count = 1 << self.G.n   # Starting 'count' as 2 to the power of n.
        S = []                  # Solutions list.

        while count > 0:
            self.G.reset()

            # For each vertice i
            for i in range(0, self.G.n):
                # Press if the ith bit of 'count' is equal to 1
                if (count & (1 << i) != 0):
                    self.G.press(self.G.V[i])

            # Check if the graph is solved
            if (self.G.check()):
                S.append(self.G.X)

            count = count - 1

        return S

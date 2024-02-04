from .solver import Solver

class BruteForceSolver(Solver):
    def __init__(self, G):
        super(BruteForceSolver, self).__init__(G)
        self.V_d1 =  G.vertices_with_degree(1)
        self.V = G.vertices_with_degree_not(1)
        self.n = len(self.V)

    def solve(self):
        """ Try every possibility and returns all possible solutions for the Graph. (up to 32 vertices) """

        # Starts at 2 to the power of n, with n being the number of vertices with a degree greater than 1.
        current = 1 << self.n

        while current > 0:
            self.G.reset()

            # For each vertice with a degree greater than 1:
            for i, v in enumerate(self.V):
                if self.__should_press(current, i):
                    self.G.press(v)
                else:
                    self.__press_neighbours_with_degree_1(v)
            
            self.check()
            current = current - 1

        return self.S

    def __should_press(self, value, i):
        """ Returns true if the ith bit of the binary representation of 'value' is 1. """
        return value & (1 << i) != 0
    
    def __press_neighbours_with_degree_1(self, v):
        """ Press all the neighbours of v with degree equals to 1. """
        for u in self.G.N[v]:
            if u in self.V_d1:
                self.G.press(u)

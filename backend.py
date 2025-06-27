class Cube:
    def __init__(self):
        self.state = list(range(1, 55))

    def apply_move(self, cycles):
        for cycle in cycles:
            a, b, c, d = [i - 1 for i in cycle]  # convert to 0-based index
            self.state[d], self.state[a], self.state[b], self.state[c] = self.state[a], self.state[b], self.state[c], self.state[d]
            

    def move_F(self):
        print("F turn")
        F_cycles = [
            (1, 7, 9, 3), (2, 4, 8, 6), (12, 37, 34, 27), (15, 38, 31, 26), (18, 39, 28, 25)
        ]
        self.apply_move(F_cycles)

    def move_L(self):
        print("L turn")
        L_cycles = [
            (1, 19, 46, 37), (4, 22, 49, 40), (7, 25, 52, 43),
            (10, 16, 18, 12), (11, 13, 17, 15)
        ]
        self.apply_move(L_cycles)

    def move_U(self):
        print("U turn")
        U_cycles = [
            (1, 28, 54, 10), (2, 29, 53, 11), (3, 30, 52, 12),
            (19, 25, 27, 21), (20, 22, 26, 24)
        ]
        self.apply_move(U_cycles)

    def move_R(self):
        print("R turn")
        R_cycles = [
            (3, 39, 48, 21), (6, 42, 51, 24), (9, 45, 54, 27),
            (28, 34, 36, 30), (29, 31, 35, 33)
        ]
        self.apply_move(R_cycles)

    def move_D(self):
        print("D turn")
        D_cycles = [
            (7, 16, 48, 34), (8, 17, 47, 35), (9, 18, 46, 36),
            (37, 43, 45, 39), (38, 40, 44, 42)
        ]
        self.apply_move(D_cycles)

    def move_B(self):
        print("B turn")
        B_cycles = [
            (10, 21, 36, 43), (13, 20, 33, 44), (16, 19, 30, 45),
            (46, 52, 54, 48), (47, 49, 53, 51)
        ]
        self.apply_move(B_cycles)


    def display_net(self):

        # Define positions for each face
        U = [[18, 19, 20], [21, 22, 23], [24, 25, 26]]
        L = [[9, 10, 11], [12, 13, 14], [15, 16, 17]]
        F = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        R = [[27, 28, 29], [30, 31, 32], [33, 34, 35]]
        B = [[45, 46, 47], [48, 49, 50], [51, 52, 53]]
        D = [[36, 37, 38], [39, 40, 41], [42, 43, 44]]

        for i in range(3):
            print(" "*10,end="")
            print(' '.join(f"{self.state[j]:2}" for j in U[i]))
        print()

        for i in range(3):
            print(' '.join(f"{self.state[j]:2}" for j in L[i]), end='   ')
            print(' '.join(f"{self.state[j]:2}" for j in F[i]), end='   ')
            print(' '.join(f"{self.state[j]:2}" for j in R[i]))
        print()

        for i in range(3):
            print(" "*10,end="")
            print(' '.join(f"{self.state[j]:2}" for j in D[i]))
        print()

        for i in range(3):
            print(" "*10,end="")
            print(' '.join(f"{self.state[j]:2}" for j in B[i]))

        print("-------------------------------\n")

cube = Cube()
cube.display_net()
print(cube.state)

cube.move_F()
cube.display_net()

cube.move_U()
cube.display_net()

cube.move_L()
cube.display_net()

cube.move_R()
cube.display_net()


cube.move_B()
cube.display_net()


cube.move_D()
cube.display_net()
print(cube.state)

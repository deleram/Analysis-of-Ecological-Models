from numpy import array, linalg, max
import cmath

def Matrix_mul(a, b):
    n = len(a); m = len(b[0])
    ans = [[0 for i in range(m)]
        for j in range(n)]
    
    for i in range(n):
        for k in range(len(b)):
            for j in range(m):
                ans[i][j] += a[i][k] * b[k][j]

    return ans
def Matrix_pow(a, b):
    cur = 1; cur_matrix = a; n = len(a)
    ans = [[(i == j) for i in range(n)]
        for j in range(n)]

    while cur <= b:
        if (b & cur) != 0:
            ans = Matrix_mul(ans, cur_matrix)
        cur *= 2
        cur_matrix = Matrix_mul(cur_matrix, cur_matrix)

    return ans

class Leslie:
    def __init__(self):
        self.number_of_groups = int(input("Enter number of Groups:\n"))
        self.Matrix = [[0 for i in range(self.number_of_groups)]
            for j in range(self.number_of_groups)]

        for i in range(self.number_of_groups):
            self.Matrix[0][i] = float(
                input("Enter fertility rate number {}:\n".format(i + 1))
                )

        for i in range(self.number_of_groups - 1):
            self.Matrix[1 + i][i] = float(
                input("Enter survival rate number {}:\n".format(i + 1))
                )
        self.Matrix[self.number_of_groups - 1][self.number_of_groups - 1] = float(
                input("Enter survival rate number {}:\n".format(
                    self.number_of_groups))
            )
    def get_eigen_values(self):
        tmp = array(self.Matrix)
        ans, tmp = linalg.eig(tmp)
        for i in ans:
            print(i, end = ' ')
        print()
    def get_max_eigen_value(self):
        tmp = array(self.Matrix)
        ans, tmp = linalg.eig(tmp)
        print(ans.max().real)
    def get_population(self):
        n = int(input("Enter number of years: \n"))
        P = [[0] for i in range(self.number_of_groups)]
        for i in range(self.number_of_groups):
            P[i][0] = int(input("Enter current size of group number {}\n".format(i + 1)))
        NL = Matrix_pow(self.Matrix, n)
        ans = Matrix_mul(NL, P)
        for i in ans:
            print(i[0])
    def get_harvest_one(self):
        tmp = array(self.Matrix)
        ans, tmp = linalg.eig(tmp)
        l = ans.max().real
        l = 1 - (1 / l)
        H = [[0 for i in range(self.number_of_groups)]
            for j in range(self.number_of_groups)]
        for i in range(self.number_of_groups):
            H[i][i] = l

        H = Matrix_mul(H, self.Matrix)

        for i in range(self.number_of_groups):
            for j in range(self.number_of_groups):
                print(H[i][j], end = ' ')
            print()
        ans, tmp = linalg.eig(H)
        l = ans.max().real
        print(l)
            
    def get_harvest_two(self):
        R = self.Matrix[0][0]; tmp = 1
        for i in range(1, self.number_of_groups):
            tmp *= self.Matrix[i][i - 1]
            R += tmp * self.Matrix[0][i]
        h = 1 - (1 / R)
        H = [[0 for i in range(self.number_of_groups)]
            for j in range(self.number_of_groups)]
        H[0][0] = h

        H = Matrix_mul(H, self.Matrix)
        for i in range(self.number_of_groups):
            for j in range(self.number_of_groups):
                if i == j:
                    H[i][j] = 1
                print(H[i][j], end = ' ')
            print()
        ans, tmp = linalg.eig(H)
        l = ans.max().real
        print(l)
        

L = Leslie()

while True:
    q = int(input("""###################################
    1. Print all eigen values
    2. Print maximum eigen value
    3. Print population after n days
    4. Calculate HL (method one)
    5. Calculate HL (metod two)
    6. Quit\n"""))

    if q == 1:
        L.get_eigen_values()
    if q == 2:
        L.get_max_eigen_value()
    if q == 3:
        L.get_population()
    if q == 4:
        L.get_harvest_one()
    if q == 5:
        L.get_harvest_two()
    if q == 6:
        break

    

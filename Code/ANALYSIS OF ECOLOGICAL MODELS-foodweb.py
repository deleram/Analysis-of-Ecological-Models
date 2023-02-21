import numpy as np
def Matrix_mul(a, b):
    n = len(a); m = len(b[0])
    ans = [
        [0 for i in range(m)]
        for j in range(n)
        ]

    for i in range(n):
        for k in range(len(b)):
            for j in range(m):
                ans[i][j] += a[i][k] * b[k][j]

    return ans
def Matrix_pow(a, b):
    cur = 1; cur_matrix = a; n = len(a)
    ans = [
        [(i == j) for i in range(n)]
        for j in range(n)
        ]

    while cur <= b:
        if (b & cur) != 0:
            ans = Matrix_mul(ans, cur_matrix)
        cur *= 2
        cur_matrix = Matrix_mul(cur_matrix, cur_matrix)

    return ans


class World:
    def __init__(self):
        self.number_of_species = int(input("Enter number of species:\n"))
        self.name_to_number = {}
        self.adjacency_matrix = [
            [0 for i in range(self.number_of_species)]
            for j in range(self.number_of_species)
            ]
        
        for i in range(self.number_of_species):
            tmp = input("Enter description of species number {} :\n".format(i + 1))
            tmp = tmp.split(' ')
            
            self.name_to_number[tmp[0]] = i
            
            for t in tmp[1:]:
                v = int(t) - 1
                self.adjacency_matrix[i][v] = 1
                
    def food_list(self):
        for name in self.name_to_number:
            print("{} has {} foods to eat".format(
                name,
                sum(self.adjacency_matrix[self.name_to_number[name]])
                ))

    def eater_list(self):
        for name in self.name_to_number:
            sm = sum(
                [self.adjacency_matrix[i][self.name_to_number[name]]
                 for i in range(self.number_of_species)]
                )
            print("{} is eaten by {} species".format(
                name, sm))
            
    def number_of_paths(self):
        begin = input("Enter begining species\n")
        end = input("Enter ending species\n")
        k = int(input("Enter lenght of food chain\n"))
        tmp_matrix = Matrix_pow(self.adjacency_matrix, k)
        print("there are {} food chains from {} to {} with lenght of {}".format(
            tmp_matrix[self.name_to_number[begin]][self.name_to_number[end]],
            begin,
            end,
            k
            ))
    def eigenvalue(self):
        w, v = np.linalg.eig(np.array(self.adjacency_matrix))
        print((np.max(w).real))

    def eigenvector(self):
        tmp_matrix = Matrix_pow(self.adjacency_matrix, 50)
        U = [sum(tmp_matrix[i]) for i in range(self.number_of_species)]
        print(U/np.max(U)) 

    
        

A = World()

while True:
    q = int(input("""###################################
    1. Print food variety of all species
    2. Print hunter variety of all species
    3. Print number of food chains
    4. Print the eigenvalue
    5. Print the eigenvector
    6. Quit\n"""))

    if q == 1:
        A.food_list()
    if q == 2:
        A.eater_list()
    if q == 3:
        A.number_of_paths()
    if q == 4:
        A.eigenvalue()
    if q == 5:
        A.eigenvector()
    if q == 6:
        break

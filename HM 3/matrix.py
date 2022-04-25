"""
Student: Omer levi
ID: 203499090
Assignment no. 3
Program: matrix.py
"""



def print_matrix(matrix):
    for i in range(len(matrix)):
        print(*matrix[i])
    print()


def create_2matrix_from_file():
    A = []
    B = []
    l = []

    with open('matrix.txt', "r") as mat:
        for line in mat:
            line = line.replace('\n', '') 
            if line.replace(' ', '').isnumeric(): 
                l.append(line.split())

    for i in range(len(l[-1])):
        A.append(l[i])

    for i in range(len(l[-1]), len(l)):
        B.append(l[i])

    return A,B


def create_empty_matrix(size,height):
    return [[0 for i in range(size)] for j in range(height)] 


def transpose_matrixLC(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def transpose_matrix(matrix):
    transposed  = create_empty_matrix(len(matrix),len(matrix[0]))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed[j][i] =(matrix[i][j])

    return transposed


def add_matrix(matA, matB):
    combined = create_empty_matrix(len(matA[0]),len(matB))
    if len(matA)== len(matB):
       

        for i in range(len(matA)):
            for j in range(len(matA[0])):
                combined[i][j] = int(matA[i][j])+int(matB[i][j])
    print_matrix(combined)


def main():
    A,B= create_2matrix_from_file()
    add_matrix(transpose_matrix(A), B)
    R = [[9,-7,2],
         [11,8,3],
         [1,-6,5]]
    L = [[5,10,2],
         [3,-6,9],
         [-4,8,1]]
    add_matrix(R,L)
    print_matrix(transpose_matrix(R))


main()






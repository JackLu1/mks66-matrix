"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1   1       1
"""
import math



#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    print( str(len(matrix)) + ' by ' + str(len(matrix[0])) + ' matrix' )
    for i in range(0, len(matrix)):
        print ' '.join(str(x) for x in matrix[i])

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if i == j:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
    #return matrix

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
#return void
# m2 is 4xn
def matrix_mult( m1, m2 ):
    product = new_matrix(4, len(m2[0]))

    for m1_row in range(len(m1)):
        for m2_col in range(len(m2[0])):
            for m2_row in range(len(m2)):
                #print(m1[m1_row][m2_row])
                #print(m2[m2_row][m2_col])
                product[m1_row][m2_col] += m1[m1_row][m2_row] * m2[m2_row][m2_col]

    return product



def new_matrix(rows = 4, cols = 4):
    m = []
    for r in range( rows ):
        m.append( [] )
        for c in range( cols ):
            m[r].append( 0 )
    return m

A = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]

B = [
        [11, 12, 13, 14],
        [15, 16, 17, 18],
        [19, 20, 21, 22],
        [23, 24, 25, 26],
    ]

#print_matrix(A)
#print_matrix(B)
#matrix_mult(A, B)
#print_matrix(A)
#print_matrix(B)
#matrix_mult(B, A)
#print_matrix(A)
#print_matrix(B)
#ident(A)
#print_matrix(A)
#matrix_mult(A, B)

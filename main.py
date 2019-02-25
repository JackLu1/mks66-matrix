from display import *
from draw import *
from matrix import *

screen = new_screen()
green = [ 0, 255, 0 ]
red = [255, 0, 0]

#wack = new_matrix()
#matrix = new_matrix(4, 10)
#
#matrix_mult(wack, matrix)

#m = [
#        [200, 300, 300, 300, 300, 200, 200, 200],
#        [200, 200, 200, 300, 300, 300, 300, 200],
#        [0, 0, 0, 0, 0, 0, 0, 0],
#        [1, 1, 1, 1, 1, 1, 1, 1],
#    ]

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

i = new_matrix(4, 4)

B = matrix_mult(A, B)
print_matrix(A)
print_matrix(B)
A = matrix_mult(B, A)
print_matrix(A)
print_matrix(B)
ident(i)
A = matrix_mult(i, A)
print_matrix(A)

m = [
        [0, 100, 100, 100, 100, 0, 0, 0],
        [0, 0, 0, 100, 100, 100, 100, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ]

n = [
        [1, 2, 0, 0],
        [2, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ]

p = matrix_mult(n, m)

draw_lines( m, screen, green )
draw_lines( p, screen, red )
display(screen)


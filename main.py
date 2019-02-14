from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]

#wack = new_matrix()
#matrix = new_matrix(4, 10)
#
#matrix_mult(wack, matrix)

m = [
        [0, 250, 500],
        [0, 500, 000],
        [0, 0, 0],
        [1, 1, 1],
    ]

draw_lines( m, screen, color )
#display(screen)

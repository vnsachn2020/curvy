from display import *
from matrix import *

def add_circle( points, cx, cy, cz, r, step ):
    i = 0

    while i <= 1:
        theta = 2 * math.pi * i
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy
        theta1 = 2 * math.pi * (i + step)
        x1 = r * math.cos(theta1) + cx
        x2 = r * math.sin(theta1) + cy
        add_edge(points, x, y, 0, x1, x2, 0)

        i += step

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    xcoefs = generate_curve_coefs(x0, x1, x2, x3, curve_type)
    ax, bx, cx, dx = xcoefs[0], xcoefs[1], xcoefs[2], xcoefs[3]
    ycoefs = generate_curve_coefs(y0, y1, y2, y3, curve_type)
    ay, by, cy, dy = ycoefs[0], ycoefs[1], ycoefs[2], ycoefs[3]
    i = 0
    while i <= 1:
        xcor = ax * math.pow(i, 3) + bx * math.pow(i, 2) + cx * i + dx
        ycor = ay * math.pow(i, 3) + by * math.pow(i, 2) + cy * i + dy
        xcor1 = ax * math.pow(i + step, 3) + bx * math.pow(i + step, 2) + cx * (i + step) + dx
        ycor1 = ay * math.pow(i + step, 3) + by * math.pow(i + step, 2) + cy * (i + step) + dy
        add_edge(points, xcor, ycor, 0, xcor1, ycor1, 0)
        i += step


def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print('Need at least 2 points to draw')
        return

    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   screen, color)
        point+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )




def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line

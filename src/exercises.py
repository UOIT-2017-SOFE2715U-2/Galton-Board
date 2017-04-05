from galton_board import GaltonBoard
from datetime import  datetime
from draw_galton_board import *


def do_exercise(exercise_number, balls):
    print 'Exercise Number: ', str(exercise_number)
    print 'Number of Balls: ', str(balls)
    levels = 22
    print 'Levels = ', levels
    start_time = datetime.now()
    print start_time
    G = GaltonBoard(levels)
    print 'Galton Board created'

    q = G.fill(balls)
    fill_end_time = datetime.now()
    print 'Board filled'
    print 'Time to creat and fill the board = ', str(fill_end_time - start_time)

    simulate(q,levels)
    #print len(q)
    end_time = datetime.now()
    print end_time
    print 'Images generation time = ', str(end_time - fill_end_time)
    print 'run time =', str(end_time - start_time)
#i = 0
#for number_of_balls in [100, 1000, 10000, 50000, 100000, 1000000]:
#    i += 1
do_exercise(6, 1000000)

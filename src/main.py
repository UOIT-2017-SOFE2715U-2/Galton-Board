from galton_board import GaltonBoard
from datetime import  datetime
from draw_galton_board import *


marbles = 100000
start_time = datetime.now()
print start_time
print 'Number of balls = ', str(marbles)
levels = 13
print 'Levels = ', levels
print 'Marbles = ', marbles

G = GaltonBoard(levels)
print 'Galton Board created'

q = G.fill(marbles)
fill_end_time = datetime.now()
print 'Board filled'
print 'Time to creat and fill the board = ', str(fill_end_time - start_time)
simulate(q, levels)
# print len(q)
end_time = datetime.now()
print end_time
print 'Images generation time = ', str(end_time - fill_end_time)
print 'run time =', str(end_time - start_time)
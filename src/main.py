from galton_board import GaltonBoard
from datetime import  datetime

start_time = datetime.now()
print start_time
G = GaltonBoard(13)
q = G.fill(1000000)
print len(q)
end_time = datetime.now()
print end_time
print 'run time =', str(end_time - start_time)
